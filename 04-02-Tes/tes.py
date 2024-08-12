import cv2

# Baca gambar
gambar = cv2.imread('teks.jpg')

# Konversi gambar ke grayscale
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# Aplikasikan thresholding
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Temukan kontur
kontur, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Hitung jumlah objek
jumlah_objek = len(kontur)
jumlah_kata = len(kontur)

print(f"Jumlah objek yang terdeteksi: {jumlah_objek}")
print(f"Jumlah kata:{jumlah_kata}")

# Menampilkan gambar dengan kontur yang terdeteksi
for cnt in kontur:
    cv2.drawContours(gambar, [cnt], 0, (0, 255, 0), 3)

cv2.imshow('Gambar dengan kontur', gambar)
cv2.waitKey(0)
cv2.destroyAllWindows()