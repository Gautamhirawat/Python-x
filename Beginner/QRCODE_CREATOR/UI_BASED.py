import qrcode
from PIL import Image
import tkinter as tk
import subprocess

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

    img.save(file_path)  
    
    
def get_color(color_label):
    # Here you can use any color picker you prefer or integrate with a color picker library
    # This is just an example using a simple color picker
    color = subprocess.run(['zenity', '--color-selection', '--title', f'Choose {color_label} color'], capture_output=True, text=True).stdout.strip()
    return color

def choose_file():
    file_path = subprocess.run(['zenity', '--file-selection', '--save', '--confirm-overwrite'], capture_output=True, text=True).stdout.strip()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def generate_qr():
    url = url_entry.get()
    file_path = file_entry.get()
    fill_color = get_color("fill")
    back_color = get_color("background")
    border_color = get_color("border")
    save_qr_code(url, file_path, fill_color, back_color, border_color)
    status_label.config(text="QR code saved successfully!")

# Create UI
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
