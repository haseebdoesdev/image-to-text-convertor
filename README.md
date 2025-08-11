# Image to Text Converter

A simple yet powerful web application built with Flask that extracts text from images using Optical Character Recognition (OCR) technology. Upload an image and get the extracted text instantly with a clean, user-friendly interface.

## Features

- 🖼️ **Image Upload**: Support for JPG, JPEG, and PNG image formats
- 📝 **Text Extraction**: Advanced OCR using EasyOCR with English language support
- 🎨 **Clean UI**: Modern, responsive web interface with CSS styling
- 📋 **Copy to Clipboard**: Easy text copying functionality
- 🛡️ **File Validation**: File type and size validation (max 10MB)
- ⚡ **Fast Processing**: Efficient text extraction with temporary file handling
- 💬 **User Feedback**: Flash messages for error handling and user guidance

## Technology Stack

- **Backend**: Python Flask
- **OCR Engine**: EasyOCR
- **Frontend**: HTML, CSS, JavaScript
- **File Handling**: Werkzeug utilities
- **Templating**: Jinja2 (Flask's built-in template engine)

## Project Structure

```
image-to-text-convertor/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── index.html        # Upload page with form
│   └── result.html       # Results display page
└── uploads/              # Directory for temporary file storage
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone or download the project:**
   ```powershell
   git clone <repository-url>
   cd image-to-text-convertor
   ```

2. **Create a virtual environment (recommended):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Install required dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```powershell
   python app.py
   ```

5. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. **Upload an Image**: Click "Choose File" and select a JPG, JPEG, or PNG image (max 10MB)
2. **Extract Text**: Click the "Extract Text" button to process the image
3. **View Results**: The extracted text will be displayed on the results page
4. **Copy Text**: Use the "Copy Text" button to copy the extracted text to clipboard
5. **Upload Another**: Click "Upload Another Image" to process more images

## Dependencies

- **Flask (2.3.3)**: Web framework for Python
- **EasyOCR (1.7.0)**: OCR library for text extraction from images
- **Werkzeug (2.3.7)**: WSGI utility library for secure filename handling

## Configuration

### File Upload Settings
- **Maximum file size**: 10MB
- **Supported formats**: PNG, JPG, JPEG
- **Language support**: English (can be extended by modifying the EasyOCR reader)

### Security Notes
- The application uses a secret key for session management
- **Important**: Change the `secret_key` in `app.py` before production deployment
- Files are temporarily stored and automatically cleaned up after processing

## API Endpoints

- **GET `/`**: Main upload page
- **POST `/upload`**: File upload and text extraction endpoint

## Error Handling

The application includes comprehensive error handling for:
- Missing file selection
- Invalid file formats
- File size exceeding limits
- OCR processing errors
- General application errors

## Customization

### Adding More Languages
To support additional languages, modify the EasyOCR reader initialization in `app.py`:
```python
# Example: Add support for Spanish and French
reader = easyocr.Reader(['en', 'es', 'fr'])
```

### Changing File Size Limits
Modify the `MAX_FILE_SIZE` variable in `app.py`:
```python
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB
```

### Adding New File Formats
Update the `ALLOWED_EXTENSIONS` set in `app.py`:
```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
```

## Troubleshooting

### Common Issues

1. **EasyOCR Installation Problems**
   - Ensure you have sufficient disk space (EasyOCR downloads language models)
   - On Windows, you might need Visual C++ Build Tools

2. **Memory Issues**
   - Large images may consume significant memory during processing
   - Consider reducing image size or increasing system memory

3. **Port Already in Use**
   - Change the port in `app.py`: `app.run(debug=True, port=5001)`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source. Please add your preferred license.

## Support

If you encounter any issues or have questions, please create an issue in the repository or contact the maintainer.

---

**Note**: This application is designed for educational and demonstration purposes. For production use, consider additional security measures, error logging, and performance optimizations.