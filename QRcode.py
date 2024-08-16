import pyqrcode
import png
from pyqrcode import QRCode


def generate_qr_code():
    print("Welcome to the QR Code Generator!")


    s = input("Please enter the URL or text to generate the QR code: ").strip()

    # Ensure the user enters a non-empty input
    if not s:
        print("Error: No input provided. Please enter a valid URL or text.")
        return

    # Prompt user to enter the file names for saving
    svg_filename = input("Enter the name for the SVG file (without extension, e.g., 'myqr'): ").strip()
    png_filename = input("Enter the name for the PNG file (without extension, e.g., 'myqr'): ").strip()

    if not svg_filename:
        svg_filename = "qr_code"
    if not png_filename:
        png_filename = "qr_code"

    # Generate QR code
    url = pyqrcode.create(s)

    # Save the SVG file
    svg_file_path = f"{svg_filename}.svg"
    url.svg(svg_file_path, scale=8)
    print(f"SVG file saved as {svg_file_path}")

    # Save the PNG file
    png_file_path = f"{png_filename}.png"
    url.png(png_file_path, scale=6)
    print(f"PNG file saved as {png_file_path}")

    print("QR Code generated successfully!")


if __name__ == "__main__":
    generate_qr_code()
