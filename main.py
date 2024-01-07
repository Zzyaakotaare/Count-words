file_path = input("Enter the file path: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print(f"Number of words in file: {word_count}")
except FileNotFoundError:
    print("File not found.")
