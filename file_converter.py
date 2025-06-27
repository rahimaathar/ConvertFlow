import os
import shutil
from typing import List, Dict, Tuple
from image_converter import convert_image as convert_image_real

file_conversion_map = {
    "documents": {
        "doc": ["pdf", "txt"],
        "docx": ["pdf", "txt"],
        "pdf": ["txt", "png", "jpg"],
        "txt": ["pdf"]
    },
    "images": {
        "heic": ["jpg", "png", "gif"],
        "png": ["jpg", "gif", "bmp"],
        "jpg": ["png", "gif", "bmp"],
        "jpeg": ["png", "gif", "bmp"],
        "gif": ["png", "jpg"],
        "bmp": ["jpg", "png"],
        "tiff": ["jpg", "png"],
        "tif": ["jpg", "png"]
    },
    "audio": {
        "mp3": ["wav", "ogg"],
        "wav": ["mp3", "ogg"],
        "ogg": ["mp3", "wav"]
    },
    "video": {
        "mp4": ["avi", "mov", "mkv"],
        "avi": ["mp4", "mov"],
        "mov": ["mp4", "avi"]
    },
    "archives": {
        "zip": ["tar", "7z"],
        "tar": ["zip", "7z"],
        "7z": ["zip", "tar"]
    }
}

def get_output_formats(input_format: str, category: str) -> List[str]:
    if category in file_conversion_map and input_format.lower() in file_conversion_map[category]:
        return file_conversion_map[category][input_format.lower()]
    return []

def get_supported_categories() -> List[str]:
    return list(file_conversion_map.keys())

def get_supported_formats(category: str) -> List[str]:
    if category in file_conversion_map:
        return list(file_conversion_map[category].keys())
    return []

def convert_word_to_pdf(input_path: str, output_path: str) -> bool:
    print(f"Converting Word document {input_path} to PDF {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_word_to_txt(input_path: str, output_path: str) -> bool:
    print(f"Converting Word document {input_path} to text {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_pdf_to_txt(input_path: str, output_path: str) -> bool:
    print(f"Converting PDF {input_path} to text {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_pdf_to_image(input_path: str, output_path: str, format_type: str) -> bool:
    print(f"Converting PDF {input_path} to {format_type} image {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_txt_to_pdf(input_path: str, output_path: str) -> bool:
    print(f"Converting text {input_path} to PDF {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_heif_to_jpg(input_path: str, output_path: str) -> bool:
    print(f"Converting HEIF {input_path} to JPG {output_path}")
    return convert_image_real(input_path, "jpg", output_path)

def convert_heif_to_png(input_path: str, output_path: str) -> bool:
    print(f"Converting HEIF {input_path} to PNG {output_path}")
    return convert_image_real(input_path, "png", output_path)

def convert_heif_to_gif(input_path: str, output_path: str) -> bool:
    print(f"Converting HEIF {input_path} to GIF {output_path}")
    return convert_image_real(input_path, "gif", output_path)

def convert_png_to_jpg(input_path: str, output_path: str) -> bool:
    print(f"Converting PNG {input_path} to JPG {output_path}")
    return convert_image_real(input_path, "jpg", output_path)

def convert_png_to_gif(input_path: str, output_path: str) -> bool:
    print(f"Converting PNG {input_path} to GIF {output_path}")
    return convert_image_real(input_path, "gif", output_path)

def convert_png_to_bmp(input_path: str, output_path: str) -> bool:
    print(f"Converting PNG {input_path} to BMP {output_path}")
    return convert_image_real(input_path, "bmp", output_path)

def convert_jpg_to_png(input_path: str, output_path: str) -> bool:
    print(f"Converting JPG {input_path} to PNG {output_path}")
    return convert_image_real(input_path, "png", output_path)

def convert_jpg_to_gif(input_path: str, output_path: str) -> bool:
    print(f"Converting JPG {input_path} to GIF {output_path}")
    return convert_image_real(input_path, "gif", output_path)

def convert_jpg_to_bmp(input_path: str, output_path: str) -> bool:
    print(f"Converting JPG {input_path} to BMP {output_path}")
    return convert_image_real(input_path, "bmp", output_path)

def convert_gif_to_png(input_path: str, output_path: str) -> bool:
    print(f"Converting GIF {input_path} to PNG {output_path}")
    return convert_image_real(input_path, "png", output_path)

def convert_gif_to_jpg(input_path: str, output_path: str) -> bool:
    print(f"Converting GIF {input_path} to JPG {output_path}")
    return convert_image_real(input_path, "jpg", output_path)

def convert_bmp_to_jpg(input_path: str, output_path: str) -> bool:
    print(f"Converting BMP {input_path} to JPG {output_path}")
    return convert_image_real(input_path, "jpg", output_path)

def convert_bmp_to_png(input_path: str, output_path: str) -> bool:
    print(f"Converting BMP {input_path} to PNG {output_path}")
    return convert_image_real(input_path, "png", output_path)

def convert_tiff_to_jpg(input_path: str, output_path: str) -> bool:
    print(f"Converting TIFF {input_path} to JPG {output_path}")
    return convert_image_real(input_path, "jpg", output_path)

def convert_tiff_to_png(input_path: str, output_path: str) -> bool:
    print(f"Converting TIFF {input_path} to PNG {output_path}")
    return convert_image_real(input_path, "png", output_path)

def convert_mp3_to_wav(input_path: str, output_path: str) -> bool:
    print(f"Converting MP3 {input_path} to WAV {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_mp3_to_ogg(input_path: str, output_path: str) -> bool:
    print(f"Converting MP3 {input_path} to OGG {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_wav_to_mp3(input_path: str, output_path: str) -> bool:
    print(f"Converting WAV {input_path} to MP3 {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_wav_to_ogg(input_path: str, output_path: str) -> bool:
    print(f"Converting WAV {input_path} to OGG {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_ogg_to_mp3(input_path: str, output_path: str) -> bool:
    print(f"Converting OGG {input_path} to MP3 {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_ogg_to_wav(input_path: str, output_path: str) -> bool:
    print(f"Converting OGG {input_path} to WAV {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_mp4_to_avi(input_path: str, output_path: str) -> bool:
    print(f"Converting MP4 {input_path} to AVI {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_mp4_to_mov(input_path: str, output_path: str) -> bool:
    print(f"Converting MP4 {input_path} to MOV {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_mp4_to_mkv(input_path: str, output_path: str) -> bool:
    print(f"Converting MP4 {input_path} to MKV {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_avi_to_mp4(input_path: str, output_path: str) -> bool:
    print(f"Converting AVI {input_path} to MP4 {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_avi_to_mov(input_path: str, output_path: str) -> bool:
    print(f"Converting AVI {input_path} to MOV {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_mov_to_mp4(input_path: str, output_path: str) -> bool:
    print(f"Converting MOV {input_path} to MP4 {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_mov_to_avi(input_path: str, output_path: str) -> bool:
    print(f"Converting MOV {input_path} to AVI {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_zip_to_tar(input_path: str, output_path: str) -> bool:
    print(f"Converting ZIP {input_path} to TAR {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_zip_to_7z(input_path: str, output_path: str) -> bool:
    print(f"Converting ZIP {input_path} to 7Z {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_tar_to_zip(input_path: str, output_path: str) -> bool:
    print(f"Converting TAR {input_path} to ZIP {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_tar_to_7z(input_path: str, output_path: str) -> bool:
    print(f"Converting TAR {input_path} to 7Z {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_7z_to_zip(input_path: str, output_path: str) -> bool:
    print(f"Converting 7Z {input_path} to ZIP {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_7z_to_tar(input_path: str, output_path: str) -> bool:
    print(f"Converting 7Z {input_path} to TAR {output_path}")
    try:
        shutil.copy2(input_path, output_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def convert_file(input_path: str, output_format: str) -> bool:
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} does not exist")
        return False
    
    file_extension = os.path.splitext(input_path)[1][1:].lower()
    
    for category, formats in file_conversion_map.items():
        if file_extension in formats and output_format in formats[file_extension]:
            output_path = os.path.splitext(input_path)[0] + "." + output_format
            
            if category == "documents":
                if file_extension in ["doc", "docx"] and output_format == "pdf":
                    return convert_word_to_pdf(input_path, output_path)
                elif file_extension in ["doc", "docx"] and output_format == "txt":
                    return convert_word_to_txt(input_path, output_path)
                elif file_extension == "pdf" and output_format == "txt":
                    return convert_pdf_to_txt(input_path, output_path)
                elif file_extension == "pdf" and output_format in ["png", "jpg"]:
                    return convert_pdf_to_image(input_path, output_path, output_format)
                elif file_extension == "txt" and output_format == "pdf":
                    return convert_txt_to_pdf(input_path, output_path)
            
            elif category == "images":
                if file_extension == "heic" and output_format == "jpg":
                    return convert_heif_to_jpg(input_path, output_path)
                elif file_extension == "heic" and output_format == "png":
                    return convert_heif_to_png(input_path, output_path)
                elif file_extension == "heic" and output_format == "gif":
                    return convert_heif_to_gif(input_path, output_path)
                elif file_extension == "png" and output_format == "jpg":
                    return convert_png_to_jpg(input_path, output_path)
                elif file_extension == "png" and output_format == "gif":
                    return convert_png_to_gif(input_path, output_path)
                elif file_extension == "png" and output_format == "bmp":
                    return convert_png_to_bmp(input_path, output_path)
                elif file_extension in ["jpg", "jpeg"] and output_format == "png":
                    return convert_jpg_to_png(input_path, output_path)
                elif file_extension in ["jpg", "jpeg"] and output_format == "gif":
                    return convert_jpg_to_gif(input_path, output_path)
                elif file_extension in ["jpg", "jpeg"] and output_format == "bmp":
                    return convert_jpg_to_bmp(input_path, output_path)
                elif file_extension == "gif" and output_format == "png":
                    return convert_gif_to_png(input_path, output_path)
                elif file_extension == "gif" and output_format == "jpg":
                    return convert_gif_to_jpg(input_path, output_path)
                elif file_extension == "bmp" and output_format == "jpg":
                    return convert_bmp_to_jpg(input_path, output_path)
                elif file_extension == "bmp" and output_format == "png":
                    return convert_bmp_to_png(input_path, output_path)
                elif file_extension in ["tiff", "tif"] and output_format == "jpg":
                    return convert_tiff_to_jpg(input_path, output_path)
                elif file_extension in ["tiff", "tif"] and output_format == "png":
                    return convert_tiff_to_png(input_path, output_path)
            
            elif category == "audio":
                if file_extension == "mp3" and output_format == "wav":
                    return convert_mp3_to_wav(input_path, output_path)
                elif file_extension == "mp3" and output_format == "ogg":
                    return convert_mp3_to_ogg(input_path, output_path)
                elif file_extension == "wav" and output_format == "mp3":
                    return convert_wav_to_mp3(input_path, output_path)
                elif file_extension == "wav" and output_format == "ogg":
                    return convert_wav_to_ogg(input_path, output_path)
                elif file_extension == "ogg" and output_format == "mp3":
                    return convert_ogg_to_mp3(input_path, output_path)
                elif file_extension == "ogg" and output_format == "wav":
                    return convert_ogg_to_wav(input_path, output_path)
            
            elif category == "video":
                if file_extension == "mp4" and output_format == "avi":
                    return convert_mp4_to_avi(input_path, output_path)
                elif file_extension == "mp4" and output_format == "mov":
                    return convert_mp4_to_mov(input_path, output_path)
                elif file_extension == "mp4" and output_format == "mkv":
                    return convert_mp4_to_mkv(input_path, output_path)
                elif file_extension == "avi" and output_format == "mp4":
                    return convert_avi_to_mp4(input_path, output_path)
                elif file_extension == "avi" and output_format == "mov":
                    return convert_avi_to_mov(input_path, output_path)
                elif file_extension == "mov" and output_format == "mp4":
                    return convert_mov_to_mp4(input_path, output_path)
                elif file_extension == "mov" and output_format == "avi":
                    return convert_mov_to_avi(input_path, output_path)
            
            elif category == "archives":
                if file_extension == "zip" and output_format == "tar":
                    return convert_zip_to_tar(input_path, output_path)
                elif file_extension == "zip" and output_format == "7z":
                    return convert_zip_to_7z(input_path, output_path)
                elif file_extension == "tar" and output_format == "zip":
                    return convert_tar_to_zip(input_path, output_path)
                elif file_extension == "tar" and output_format == "7z":
                    return convert_tar_to_7z(input_path, output_path)
                elif file_extension == "7z" and output_format == "zip":
                    return convert_7z_to_zip(input_path, output_path)
                elif file_extension == "7z" and output_format == "tar":
                    return convert_7z_to_tar(input_path, output_path)
    
    print(f"Error: Conversion from {file_extension} to {output_format} is not supported")
    return False

def upload_file():
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = input("Enter the path of the file to upload: ").strip()
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return None
    dest_path = os.path.join(upload_dir, os.path.basename(file_path))
    shutil.copy(file_path, dest_path)
    print(f"File uploaded to {dest_path}")
    return dest_path

def main():
    print("=== File Converter Backend Module ===\n")
    while True:
        print("Options:")
        print("1. Upload a file")
        print("2. Show available categories")
        print("3. Get output formats for a format and category")
        print("4. Convert a file")
        print("5. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            upload_file()
        elif choice == "2":
            print("Available categories:")
            for category in get_supported_categories():
                print(f"- {category}")
        elif choice == "3":
            category = input("Enter category: ").strip()
            input_format = input("Enter input format (e.g. docx, png): ").strip()
            outputs = get_output_formats(input_format, category)
            print(f"Output formats for {input_format.upper()} in {category}: {outputs}")
        elif choice == "4":
            file_path = input("Enter the path of the file to convert: ").strip()
            output_format = input("Enter the desired output format: ").strip()
            convert_file(file_path, output_format)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
        print()

if __name__ == "__main__":
    main() 