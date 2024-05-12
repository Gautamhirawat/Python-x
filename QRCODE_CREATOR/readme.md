
```markdown
# QR Code Generator

## Text-Based QR Code Generator

The `TEXT_BASED.py` script generates a QR code from user input (a text or URL) and saves it as an image file. Below is an overview of the script:

```python
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
url = input("Enter any text or URL to convert it into QR code: ")
file_path = input("Enter the file path and name to save the QR code (e.g., qr.png): ")
save_qr_code(url, file_path)
print("QR code saved successfully!")
```

### Functionality:
- The script prompts the user to input a text or URL and the file path where they want to save the QR code image.
- It uses the `qrcode` library to create a QR code with the specified parameters:
  - Version: 1
  - Error correction level: High
  - Box size: 10
  - Border size: 2
- The URL is added to the QR code, and then the code is generated and saved as an image using PIL (`PIL.Image`).
- The default fill color is black, and the background color is white.

---

## UI-Based QR Code Generator

The `UI_BASED.py` script generates QR codes with a graphical user interface (GUI) using Tkinter. Here's an overview of the script:

```python
import qrcode
from PIL import Image
import tkinter as tk


def save_qr_code(url, file_path, fill_color, back_color, border_color):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Convert RGB color to hex format for PIL
    border_color_hex = "#{:02x}{:02x}{:02x}".format(*border_color)
    img = img.convert("RGB")
    img_with_border = Image.new("RGB", (img.width + 2 * qr.border, img.height + 2 * qr.border), border_color_hex)
    img_with_border.paste(img, (qr.border, qr.border))

    img_with_border.save(file_path)

# UI creation using Tkinter is here...
root = tk.Tk()
root.title("QR Code Generator")

url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

file_label = tk.Label(root, text="File path:")
file_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=1, column=1, padx=5, pady=5)
file_button = tk.Button(root, text="Choose File", command=choose_file)
file_button.grid(row=1, column=2, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=2, column=0, columnspan=3, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()

    
     
```

### Functionality:
- The script generates QR codes with a graphical user interface using Tkinter.
- It allows users to enter a URL and select the file path where they want to save the QR code image.
- Users can also choose the fill color, background color, and border color for the QR code using a color picker.
- Upon clicking the "Generate QR Code" button, the QR code is generated with the specified parameters and saved as an image file.
- The script provides a more user-friendly and interactive way to generate QR codes compared to the text-based approach.

---

These scripts provide different methods for generating QR codes: one through simple text-based input and the other via a graphical user interface. Users can choose the method that best suits their needs and preferences.
```
