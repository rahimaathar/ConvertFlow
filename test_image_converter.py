from image_converter import convert_image, verify_image_format, get_supported_formats
import os

def test_image_conversion():
    print("=== Testing Image Converter ===\n")
    
    print("Supported formats:", get_supported_formats())
    
    input_file = "uploads/cs-logo.png"
    output_format = "jpg"
    output_file = "uploads/cs-logo_converted.jpg"
    
    if os.path.exists(input_file):
        print(f"\nConverting {input_file} to {output_format.upper()}...")
        
        if convert_image(input_file, output_format, output_file):
            print("\nVerifying converted file:")
            verify_image_format(output_file)
            
            if os.path.exists(output_file):
                print(f"✅ Success! Converted file created: {output_file}")
                print(f"Original size: {os.path.getsize(input_file)} bytes")
                print(f"Converted size: {os.path.getsize(output_file)} bytes")
            else:
                print("❌ Error: Converted file not found")
        else:
            print("❌ Conversion failed!")
    else:
        print(f"❌ Test file not found: {input_file}")
        print("Please upload an image file first through the web interface.")

if __name__ == "__main__":
    test_image_conversion() 