def main():
    # Prompt user for filename
    filename = input("Enter the filename: ")

    try:
        # Read all lines into a list
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Main loop
        while True:
            print(f"\nThe file has {len(lines)} lines.")
            line_number = int(input("Enter a line number (0 to quit): "))

            if line_number == 0:
                print("Exiting program.")
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print("Invalid line number. Please try again.")

    except FileNotFoundError:
        print("File not found. Please make sure the filename is correct.")

if __name__ == "__main__":
    main()
