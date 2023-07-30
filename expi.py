import os

def process_directory(path, output_file):
    for root, _, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "rb") as file:  # Open the file in binary mode
                try:
                    content = file.read().decode("utf-8")  # Manually decode the content
                except UnicodeDecodeError:
                    print(f"Error decoding file: {file_path}")
                    continue  # Skip the file if decoding fails

                output_file.write(f"<file name: {file_path}>\n<content>\n")
                output_file.write(content)
                output_file.write("\n<content/>\n<file/>\n")

if __name__ == "__main__":
    input_folder = "."

    with open("output.txt", "w", encoding="utf-8") as output_file:
        process_directory(input_folder, output_file)

    print("Process completed. Data has been written to 'output.txt' file.")
