"""
kicau-mania.py
==============
Deteksi tangan pakai MediaPipe:
  - Jika tangan MENUTUP MULUT (near_face) DAN tangan lain MELAMBAIKAN tangan (moving)
    → tampilkan video kucing + teks "kicau 🎉 kicau" + putar audio

Dependensi:
    pip install opencv-python mediapipe numpy pygame

Cara pakai:
    1. Letakkan file video kucing dengan nama  kicau-mania.mp4  di folder yang sama.
    2. Letakkan file audio dengan nama  sound.mp3  di folder yang sama.
    3. Jalankan:  python kicau-mania.py
    4. Tekan  Q  untuk keluar.
"""

import cv2
import mediapipe as mp
import numpy as np
import time
import os
import sys
import pygame

# ──────────────────────────────────────────────
# Konfigurasi
# ──────────────────────────────────────────────
CAT_VIDEO_PATH = "kicau-mania.mp4"   # ganti nama file jika berbeda
AUDIO_PATH     = "sound.mp3"         # ganti nama file audio jika berbeda
WEBCAM_INDEX   = 0
SHOW_LANDMARKS = True                # True = tampilkan titik tangan di webcam
KICAU_DURATION = 4.0                 # detik video kucing ditampilkan setelah trigger


# ──────────────────────────────────────────────
# Inisialisasi MediaPipe
# ──────────────────────────────────────────────
mp_hands    = mp.solutions.hands
mp_face     = mp.solutions.face_detection
mp_drawing  = mp.solutions.drawing_utils

hands_detector = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.5,
)
face_detector = mp_face.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6,
)


# ──────────────────────────────────────────────
# Helper: Deteksi "menutup mulut"
#   → telapak tangan berada dekat area mulut/wajah
# ──────────────────────────────────────────────
def is_near_face(hand_landmarks, face_bbox, img_w, img_h):
    """
    Cek apakah titik tengah telapak tangan berada di dalam
    bounding-box wajah yang sedikit diperlebar.
    """
    if face_bbox is None:
        return False

    fx, fy, fw, fh = face_bbox
    # Perlebar bbox wajah 30%
    pad_x = fw * 0.3
    pad_y = fh * 0.3
    x1, y1 = fx - pad_x, fy - pad_y
    x2, y2 = fx + fw + pad_x, fy + fh + pad_y

    # Gunakan landmark 9 (tengah telapak) sebagai referensi
    lm = hand_landmarks.landmark[9]
    hx, hy = lm.x * img_w, lm.y * img_h

    return x1 < hx < x2 and y1 < hy < y2


# ──────────────────────────────────────────────
# Helper: Deteksi "melambaikan tangan"
#   → perubahan posisi pergelangan tangan antar frame
# ──────────────────────────────────────────────
WAVE_THRESHOLD = 0.018   # perubahan posisi relatif (0–1) per frame

class WaveDetector:
    def __init__(self):
        self.prev_x = {}   # key = hand_index

    def update(self, hand_index, hand_landmarks):
        """
        Kembalikan True jika tangan bergerak cukup cepat (dianggap melambai).
        """
        wrist_x = hand_landmarks.landmark[0].x
        moving = False
        if hand_index in self.prev_x:
            delta = abs(wrist_x - self.prev_x[hand_index])
            moving = delta > WAVE_THRESHOLD
        self.prev_x[hand_index] = wrist_x
        return moving

    def clear(self, hand_index):
        self.prev_x.pop(hand_index, None)


wave_detector = WaveDetector()


# ──────────────────────────────────────────────
# Inisialisasi Pygame untuk Audio
# ──────────────────────────────────────────────
pygame.mixer.init()
audio_sound = None
cap_cam = cv2.VideoCapture(WEBCAM_INDEX)
if not cap_cam.isOpened():
    sys.exit("[ERROR] Webcam tidak ditemukan. Periksa WEBCAM_INDEX.")

if not os.path.isfile(CAT_VIDEO_PATH):
    sys.exit(f"[ERROR] File video '{CAT_VIDEO_PATH}' tidak ditemukan.\n"
             f"        Letakkan file video kucing di folder yang sama dan\n"
             f"        sesuaikan CAT_VIDEO_PATH di bagian atas script.")

if not os.path.isfile(AUDIO_PATH):
    sys.exit(f"[ERROR] File audio '{AUDIO_PATH}' tidak ditemukan.\n"
             f"        Letakkan file audio di folder yang sama dan\n"
             f"        sesuaikan AUDIO_PATH di bagian atas script.")

# Load audio
try:
    audio_sound = pygame.mixer.Sound(AUDIO_PATH)
    # Deteksi durasi audio otomatis
    audio_duration = audio_sound.get_length()
    KICAU_DURATION = max(audio_duration, 4.0)  # gunakan durasi audio, min 4 detik
    print(f"[INFO] Durasi audio: {audio_duration:.2f} detik")
    print(f"[INFO] Durasi playback: {KICAU_DURATION:.2f} detik")
except Exception as e:
    sys.exit(f"[ERROR] Gagal load audio: {e}")

cap_cat = cv2.VideoCapture(CAT_VIDEO_PATH)
cat_total_frames = int(cap_cat.get(cv2.CAP_PROP_FRAME_COUNT))
cat_fps          = cap_cat.get(cv2.CAP_PROP_FPS) or 30

# Ukuran jendela output
WIN_W, WIN_H = 1280, 580
CAT_W        = WIN_W // 2   # video kucing di sisi kanan


# ──────────────────────────────────────────────
# State mesin
# ──────────────────────────────────────────────
showing_cat   = False
kicau_end_t   = 0.0
cat_frame_pos = 0

print("[INFO] Program berjalan. Tekan Q untuk keluar.")
print("[INFO] Trigger: satu tangan menutup mulut + tangan lain melambaikan.")


# ──────────────────────────────────────────────
# Loop utama
# ──────────────────────────────────────────────
while True:
    ret, frame = cap_cam.read()
    if not ret:
        break

    frame  = cv2.flip(frame, 1)                         # mirror
    img_h, img_w = frame.shape[:2]
    rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ── Deteksi wajah ──────────────────────────
    face_result = face_detector.process(rgb)
    face_bbox   = None
    if face_result.detections:
        det = face_result.detections[0]
        bb  = det.location_data.relative_bounding_box
        face_bbox = (
            int(bb.xmin  * img_w),
            int(bb.ymin  * img_h),
            int(bb.width * img_w),
            int(bb.height* img_h),
        )

    # ── Deteksi tangan ─────────────────────────
    hand_result = hands_detector.process(rgb)

    near_face_detected = False
    moving_detected    = False

    if hand_result.multi_hand_landmarks:
        for idx, hand_lm in enumerate(hand_result.multi_hand_landmarks):

            if SHOW_LANDMARKS:
                mp_drawing.draw_landmarks(
                    frame, hand_lm, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,230,255), thickness=2, circle_radius=3),
                    mp_drawing.DrawingSpec(color=(255,100,0), thickness=2),
                )

            if is_near_face(hand_lm, face_bbox, img_w, img_h):
                near_face_detected = True

            if wave_detector.update(idx, hand_lm):
                moving_detected = True

        # Bersihkan state tangan yang sudah hilang
        active = set(range(len(hand_result.multi_hand_landmarks)))
        for gone in set(wave_detector.prev_x.keys()) - active:
            wave_detector.clear(gone)
    else:
        wave_detector.prev_x.clear()

    # ── Debug info di terminal ──────────────────
    print(f"\r  near_face={near_face_detected}  moving={moving_detected}      ", end="")

    # ── Trigger ────────────────────────────────
    if near_face_detected and not showing_cat:
        showing_cat   = True
        kicau_end_t   = time.time() + KICAU_DURATION
        cap_cat.set(cv2.CAP_PROP_POS_FRAMES, 0)
        cat_frame_pos = 0
        # Putar audio
        if audio_sound:
            audio_sound.play()

    # ── Reset otomatis / Trigger sudah hilang ──────────────────────────────
    if showing_cat and (time.time() > kicau_end_t or not near_face_detected):
        showing_cat = False
        # Stop audio    
        if audio_sound:
            audio_sound.stop()

    # ──────────────────────────────────────────
    # Render frame output
    # ──────────────────────────────────────────
    cam_resized = cv2.resize(frame, (WIN_W // 2, WIN_H))

    if showing_cat:
        ret_c, cat_frame = cap_cat.read()
        if not ret_c:
            # Video sudah selesai, tampilkan frame terakhir atau hitam
            cat_resized = np.zeros((WIN_H, CAT_W, 3), dtype=np.uint8)
        else:
            cat_resized = cv2.resize(cat_frame, (CAT_W, WIN_H))

        # Gabung webcam + kucing
        display = np.hstack([cam_resized, cat_resized])

        # Teks "kicau 🎉 kicau" (OpenCV tidak support emoji, pakai ASCII)
        text       = "kicau   kicau!"
        font       = cv2.FONT_HERSHEY_DUPLEX
        font_scale = 2.0
        thickness  = 4
        (tw, th), _ = cv2.getTextSize(text, font, font_scale, thickness)
        tx = (WIN_W - tw) // 2
        ty = WIN_H - 30
        # Shadow
        cv2.putText(display, text, (tx+3, ty+3), font, font_scale,
                    (0, 0, 0), thickness + 2, cv2.LINE_AA)
        # Teks utama kuning cerah
        cv2.putText(display, text, (tx, ty), font, font_scale,
                    (0, 230, 255), thickness, cv2.LINE_AA)

        # Border animasi di sekitar video kucing
        elapsed = KICAU_DURATION - (kicau_end_t - time.time())
        flash   = int(elapsed * 6) % 2 == 0
        color_b = (0, 255, 100) if flash else (0, 100, 255)
        cv2.rectangle(display,
                      (WIN_W // 2, 0), (WIN_W - 1, WIN_H - 1),
                      color_b, 6)

    else:
        # Hanya webcam
        blank   = np.zeros((WIN_H, CAT_W, 3), dtype=np.uint8)
        # Teks petunjuk
        hint = "!"
        cv2.putText(blank, hint, (20, WIN_H // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (80, 80, 80), 2, cv2.LINE_AA)
        display = np.hstack([cam_resized, blank])

    cv2.imshow("kicau-mania", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:
        break


# ──────────────────────────────────────────────
# Cleanup
# ──────────────────────────────────────────────
cap_cam.release()
cap_cat.release()
cv2.destroyAllWindows()
hands_detector.close()
face_detector.close()
if audio_sound:
    audio_sound.stop()
pygame.mixer.quit()
print("\n[INFO] Program selesai.")