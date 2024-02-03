#!/usr/bin/env python3
# This Python3 script will read raw.txt -> sort and format -> write to prod_blocklist

def main():
    try:
        # Open raw.txt for reading
        with open("raw.txt", "r") as raw_list:
            # Read lines, remove leading/trailing whitespace, and store in a list
            lines = [line.strip() for line in raw_list]

        # Sort the lines in the list
        sorted_lines = sorted(lines)

        # Open prod_blocklist for writing
        with open("prod_blocklist.txt", "w") as prod_list:
            # Write sorted lines to prod_blocklist
            for line in sorted_lines:
                prod_list.write("0.0.0.0 " + line + '\n')

        print("Sorting and formatting completed. Results written to prod_blocklist.txt")

    except FileNotFoundError:
        print("Error: The input file 'raw.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
