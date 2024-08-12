import cv2

# Mengakses kamera (0 adalah default untuk kamera utama)
cap = cv2.VideoCapture(0)

# Periksa apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Error: Tidak bisa mengakses kamera.")
    exit()

# Loop untuk membaca frame dari kamera
while True:
    # Baca frame dari kamera
    ret, frame = cap.read()
    
    # Jika frame berhasil dibaca
    if ret:
        # Tampilkan frame
        cv2.imshow('Kamera', frame)
        
        # Tunggu 1ms, tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Tidak bisa membaca frame.")
        break

# Lepaskan kamera dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()