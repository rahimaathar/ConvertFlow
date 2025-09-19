#  ConvertFlow

<div align="center">

![ConvertFlow Logo](static/favicon.svg)



*A modern, intuitive web application for converting files between different formats with a professional, enterprise-ready interface.*

</div>


---

##  Features

### **Smart File Detection**
- **Automatic Format Recognition**: Instantly detects file types and categories
- **Intelligent Conversion Options**: Shows only relevant output formats
- **Error Handling**: Graceful handling of unsupported file types

###  **Comprehensive Format Support**
- **Images**: PNG, JPG, GIF, BMP, TIFF, WEBP, HEIF
- **Documents**: DOC, DOCX, PDF, TXT
- **Audio**: MP3, WAV, OGG
- **Video**: MP4, AVI, MOV, MKV
- **Archives**: ZIP, TAR, 7Z

###  **Professional Interface**
- **Modern Design**: Clean, corporate-ready UI
- **Responsive Layout**: Works seamlessly on all devices
- **Real-time Processing**: Instant conversion feedback
- **Download Management**: Secure file downloads



---

##  Technology Stack

### **Backend**
- **Python 3.8+**: Core programming language
- **Flask 3.0+**: Web framework
- **Pillow (PIL)**: Image processing library
- **Werkzeug**: File handling utilities

### **Frontend**
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with custom properties
- **JavaScript**: Interactive functionality
- **Bootstrap 5**: Responsive framework
- **Font Awesome**: Icon library



---

##  Quick Start

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning)

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rahimaathar/ConvertFlow.git
   cd ConvertFlow
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your browser and navigate to: `http://127.0.0.1:5001`

---

## 📁 Project Structure

```
ConvertFlow/
├── 📄 app.py                    # Flask application entry point
├── 📄 file_converter.py         # Core conversion logic
├── 📄 image_converter.py        # Image processing module
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Project documentation
├── 📄 .gitignore               # Git ignore rules
├── 📁 templates/
│   └── 📄 index.html           # Main UI template
├── 📁 static/
│   ├── 📄 favicon.svg          # Application favicon
│   └── 📄 favicon.ico          # Favicon fallback
├── 📁 uploads/                 # File upload directory
└── 📁 venv/                    # Virtual environment (not in repo)
```

---

## 🔧 Supported Conversions

### **🖼️ Image Formats**
| Input Format | Output Formats | Description |
|--------------|----------------|-------------|
| PNG | JPG, GIF, BMP | High-quality raster graphics |
| JPG/JPEG | PNG, GIF, BMP | Compressed image format |
| GIF | PNG, JPG | Animated graphics support |
| BMP | JPG, PNG | Uncompressed bitmap format |
| TIFF/TIF | JPG, PNG | High-resolution imaging |
| HEIF | JPG, PNG, GIF | Modern image format |

### **📄 Document Formats**
| Input Format | Output Formats | Description |
|--------------|----------------|-------------|
| DOC/DOCX | PDF, TXT | Microsoft Word documents |
| PDF | TXT, PNG, JPG | Portable document format |
| TXT | PDF | Plain text documents |

### **🎵 Audio Formats**
| Input Format | Output Formats | Description |
|--------------|----------------|-------------|
| MP3 | WAV, OGG | Compressed audio format |
| WAV | MP3, OGG | Uncompressed audio format |
| OGG | MP3, WAV | Open-source audio format |

### **🎬 Video Formats**
| Input Format | Output Formats | Description |
|--------------|----------------|-------------|
| MP4 | AVI, MOV, MKV | Modern video container |
| AVI | MP4, MOV | Audio Video Interleave |
| MOV | MP4, AVI | Apple QuickTime format |

### **📦 Archive Formats**
| Input Format | Output Formats | Description |
|--------------|----------------|-------------|
| ZIP | TAR, 7Z | Compressed archive format |
| TAR | ZIP, 7Z | Tape archive format |
| 7Z | ZIP, TAR | 7-Zip archive format |

---

## 🎯 Usage Guide

### **Step 1: Upload File**
1. Navigate to the ConvertFlow interface
2. Click the upload area or drag and drop your file
3. The system automatically detects the file type

### **Step 2: Select Output Format**
1. Choose your desired output format from the dropdown
2. Available formats are filtered based on your input file
3. Click "Convert File" to start the process

### **Step 3: Download Result**
1. Wait for the conversion to complete
2. Click the download button to save your converted file
3. The file is automatically saved with the correct extension

### **Best Practices**
- **File Size**: Keep files under 50MB for optimal performance
- **Format Selection**: Choose formats that maintain quality
- **Backup**: Always keep original files as backup
- **Security**: Only upload files from trusted sources



---

## ⚙️ Configuration

### **Environment Variables**
```bash
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Upload Configuration
MAX_CONTENT_LENGTH=52428800  # 50MB limit
UPLOAD_FOLDER=uploads
```

### **Customization Options**
- **Port**: Change default port in `app.py`
- **Upload Limit**: Modify `MAX_CONTENT_LENGTH`
- **Styling**: Customize CSS variables in `templates/index.html`
- **Supported Formats**: Extend conversion maps in `file_converter.py`

---

## 🔒 Security

### **⚠️ IMPORTANT SECURITY WARNING**
**DO NOT UPLOAD CONFIDENTIAL, SENSITIVE, OR PRIVATE FILES**

---




