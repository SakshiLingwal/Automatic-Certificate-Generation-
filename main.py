import pandas as pd
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Read recipient data from CSV file
data = pd.read_csv('recipients.csv')

# Load the certificate template
template = Image.open('certificate_template.png')

# Load a font
font = ImageFont.truetype('arial.ttf', 40)

# Function to generate a certificate
def generate_certificate(name):
    certificate = template.copy()
    draw = ImageDraw.Draw(certificate)
    
    # Get text bounding box for centering
    name_bbox = draw.textbbox((0, 0), name, font=font)
    
    # Calculate width and height
    name_width = name_bbox[2] - name_bbox[0]
    name_height = name_bbox[3] - name_bbox[1]
    
    # Calculate positions to center the text
    name_x = (certificate.width - name_width) / 2
    name_y = (certificate.height / 2) - 100  # Adjust the Y-coordinate as needed
    
    # Draw text on the certificate
    draw.text((name_x, name_y), name, font=font, fill='black')
    
    return certificate

# Function to generate QR code
def generate_qr_code(file_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(file_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# Function to embed QR code in the certificate
def embed_qr_code(certificate, qr_code):
    qr_code = qr_code.resize((150, 150))  # Resize QR code as needed
    certificate.paste(qr_code, (certificate.width - 200, certificate.height - 200))
    return certificate

# Directory to save certificates
output_dir = 'generated_certificate'
os.makedirs(output_dir, exist_ok=True)

# Generate and save certificates
for index, row in data.iterrows():
    name = row['Name']
    
    # Generate certificate
    certificate = generate_certificate(name)
    
    # Save the certificate to a file
    certificate_file_path = os.path.join(output_dir, f'{name}.png')
    certificate.save(certificate_file_path)
    
    # Create a URL that points to the certificate file
    file_url = f'https://example.com/{name}.png'  # Replace with your server URL
    
    # Generate QR code with the file URL
    qr_code = generate_qr_code(file_url)
    
    # Embed the QR code in the certificate
    certificate = embed_qr_code(certificate, qr_code)
    
    # Save the certificate with QR code
    certificate.save(os.path.join(output_dir, f'{name}_with_qr.png'))