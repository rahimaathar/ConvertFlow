from PIL import Image
import os
import imghdr
from typing import Dict, Optional

format_mapping = {
    "jpg": "JPEG",
    "jpeg": "JPEG", 
    "png": "PNG",
    "gif": "GIF",
    "bmp": "BMP",
    "tiff": "TIFF",
    "tif": "TIFF",
    "webp": "WEBP",
    "ico": "ICO"
}

def convert_image(input_path: str, output_format: str, output_path: str) -> bool:
    try:
        if not os.path.exists(input_path):
            print(f"Error: Input file '{input_path}' not found")
            return False
        
        if output_format.lower() not in format_mapping:
            print(f"Error: Unsupported output format '{output_format}'")
            return False
        
        pillow_format = format_mapping[output_format.lower()]
        
        with Image.open(input_path) as img:
            if pillow_format == "JPEG" and img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            elif pillow_format == "JPEG" and img.mode == 'P':
                img = img.convert('RGB')
            
            img.save(output_path, format=pillow_format, optimize=True)
            
        print(f"Successfully converted '{input_path}' to '{output_path}' ({pillow_format})")
        return True
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False

def verify_image_format(file_path: str) -> Optional[str]:
    try:
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found")
            return None
        
        detected_format = imghdr.what(file_path)
        if detected_format:
            print(f"Verified: '{file_path}' is a valid {detected_format.upper()} image")
            return detected_format
        else:
            print(f"Warning: Could not detect format for '{file_path}'")
            return None
            
    except Exception as e:
        print(f"Error verifying image format: {e}")
        return None

def get_supported_formats() -> list:
    return list(format_mapping.keys())

def main():
    print("=== Image Format Converter ===\n")
    
    print("Supported formats:")
    for ext, pillow_format in format_mapping.items():
        print(f"  {ext.upper()} → {pillow_format}")
    
    print("\nExample conversion:")
    
    input_file = "sample.png"
    output_format = "jpeg"
    output_file = "sample_converted.jpeg"
    
    print(f"Converting '{input_file}' to {output_format.upper()}...")
    
    if convert_image(input_file, output_format, output_file):
        print("\nVerifying converted file:")
        verify_image_format(output_file)
    else:
        print("Conversion failed!")

if __name__ == "__main__":
    main() 