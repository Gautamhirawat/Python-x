import qrcode
from PIL import Image


def save_qr_code(url, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)


# Example usage:
url = input("Enter any text or url to convert it into QRcode. ")
file_path = input("Enter the file path and name to save the QR code (e.g., qr.png): ")
save_qr_code(url, file_path)
print("QR code saved successfully!")
