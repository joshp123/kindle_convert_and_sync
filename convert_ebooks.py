# For guessing MIME type based on file name extension
import os
import subprocess


def main():
    all_files = os.listdir()
    os.makedirs('converted', exist_ok=True)
    converted_files = os.listdir('converted')
    epubs = {f for f in all_files if os.path.splitext(f)[-1] == '.epub'}
    azw3s = {f for f in converted_files if os.path.splitext(f)[-1] == '.azw3'}
    for epub in epubs:
        if (target_filename := epub.replace('epub', 'azw3')) in azw3s:
            print(f"Already converted {epub} - skipping")
        else:
            print(f"Converting {epub} to azw3")
            target_file_path = os.path.join('converted', target_filename)
            subprocess.run(["ebook-convert", epub, target_file_path], capture_output=True)
            print(f"Converted {epub} to azw3")
            print(f"Copying {target_filename} to Kindle")
            copy_args = ['ebook-device', 'cp', target_file_path, os.path.join('dev:/documents', target_filename)]
            subprocess.run(copy_args)

    subprocess.run(["ebook-device", "eject"])


if __name__ == "__main__":
    main()
