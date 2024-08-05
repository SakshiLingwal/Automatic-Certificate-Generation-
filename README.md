# Automatic Certificate Generation 

This project allows you to generate certificates automatically using a certificate template and Python code. It also includes QR code generation for added functionality.

## Files Included

### 1. **Certificate Template**
   - You can install this template from Google or any other source of your choice. 
   - It serves as the base design for your certificates.

### 2. **main.py**
   - This Python script contains all the code necessary for certificate generation and QR code embedding.
   - Make sure to customize it according to your specific requirements (e.g., input data, formatting, and template merging).

### 3. **Generated Certificates Folder**
   - After executing `main.py`, this folder will be created automatically.
   - It contains all the certificates that were generated based on your template and input data.

## Usage

1. **Install the certificate template**:
   - Download or create your desired certificate template and place it in the project directory.

2. **Customize `main.py`**:
   - Edit `main.py` with your data and formatting preferences to suit your specific needs.

3. **Run `main.py`**:
   - Execute the script by running `python main.py` in your terminal or command prompt.

4. **Check the `generated_certificates` folder**:
   - Upon successful execution, your freshly generated certificates will be available in the `generated_certificates` folder.

## Example

To run the script, use the following command:

```bash
pip install -r requirements.txt
python main.py


### Tips:

- Replace `"python main.py"` with `"python3 main.py"` if you're using Python 3 and it isn't the default.
- The `requirements.txt` file should list all necessary Python packages, such as `Pillow` and `qrcode`.

This README provides a clear, structured guide for users to set up and run your project.

