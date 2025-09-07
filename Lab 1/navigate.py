# Program: Line Navigator
# Allows the user to navigate through lines of a text file.

def main():
    # Prompt the user for a filename
    filename = input("Enter the filename: ")

    try:
        # Read lines into a list
        with open(filename, "r") as file:
            lines = file.readlines()

        total_lines = len(lines)
        if total_lines == 0:
            print("The file is empty.")
            return

        while True:
            print(f"\nThe file has {total_lines} lines.")
            # Prompt for line number
            user_input = input(f"Enter a line number (1-{total_lines}) or 0 to quit: ")

            # Validate input
            if not user_input.isdigit():
                print("Please enter a valid number.")
                continue

            line_number = int(user_input)

            if line_number == 0:
                print("Exiting program.")
                break
            elif 1 <= line_number <= total_lines:
                # Print the requested line (remove newline at the end)
                print(f"Line {line_number}: {lines[line_number - 1].rstrip()}")
            else:
                print(f"Please enter a number between 0 and {total_lines}.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
