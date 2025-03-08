import sys
from stats import char_frequency, sort_char_frequency

def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Get book path from CLI argument

    try:
        with open(book_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

    freq_dict = char_frequency(content)  # Generate character frequency dictionary
    sorted_report = sort_char_frequency(freq_dict)  # Sort it

    print("--------- Character Count -------")
    for item in sorted_report:
        print(f"{item['char']}: {item['count']}")  # Matches expected format
    print("============= END ===============")

if __name__ == "__main__":
    main()