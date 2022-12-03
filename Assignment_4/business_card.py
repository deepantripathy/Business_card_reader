import cv2
import pytesseract
import webbrowser
 
# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\deepa\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"

image = cv2.imread("business_card.png")
 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
 
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
 
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
 
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)
 
image2 = image.copy()
 
file = open("information.txt", "w+")
file.write("")
file.close()

#write text 
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    rect = cv2.rectangle(image2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cropped = image2[y:y + h, x:x + w]

    file = open("information.txt", "a")

    text = pytesseract.image_to_string(cropped)

    file.write(text)
    file.close

#qr code
detect = cv2.QRCodeDetector()
url_data, bbox, straight_qrcode = detect.detectAndDecode(image)
if url_data:
    webbrowser.open(url_data)