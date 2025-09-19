def count_words_in_file(file_path):
    """
    Reads a text file, counts the number of words, and handles file not found errors.

    Args:
        file_path (str): The path to the text file.

    Returns:
        None: Prints the word count or an error message.
    """
    try:
        # 'with' statement ensures the file is properly closed even if errors occur.
        with open(file_path, 'r') as file:
            content = file.read()  # Read the entire content of the file.
            words = content.split()  # Split the content by whitespace to get a list of words.
            word_count = len(words)  # The length of the list is the word count.
            print(f"✅ Success! The file '{file_path}' contains {word_count} words.")
    except FileNotFoundError:
        # This block runs if the file specified in 'file_path' does not exist.
        print(f"❌ Error: The file '{file_path}' was not found. Please check the file name and path.")
    except Exception as e:
        # A general catch-all for other potential errors (e.g., permission issues).
        print(f"An unexpected error occurred: {e}")

# --- Main part of the script ---
if __name__ == "__main__":
    # Ask the user for the file name.
    filename = input("Enter the name of the text file (e.g., sample.txt): ")
    
    # Call the function with the user-provided filename.
    count_words_in_file(filename)