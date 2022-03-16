pip install qrcode
import qrcode
img = qrcode.make("https://www.youtube.com/")
img.save("youtubeQR.jpg")