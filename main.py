import os
import shutil
import argparse

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            extension = filename.split('.')[-1].lower()
            target_folder = os.path.join(folder_path, extension)

            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fayllarni avtomatik tartiblovchi CLI dastur")
    parser.add_argument("--path", required=True, help="Fayllar joylashgan papka yo‘li")

    args = parser.parse_args()
    organize_files(args.path)
    print("✅ Fayllar muvaffaqiyatli tartiblandi!")

