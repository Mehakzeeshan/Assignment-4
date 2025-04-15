import cv2

# DECODING QR CODE

# Load the image
img = cv2.imread('C:/Users/i Tech Computers/Pictures/Camera Roll/myqrcode.png')

# Initialize the QRCode detector
detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, bbox, _ = detector.detectAndDecode(img)

if data:
    print("Decoded QR Code data:", data)
else:
    print("No QR Code found.")
