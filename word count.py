Python 3.12.2 (v3.12.2:6abddd9f6a, Feb  6 2024, 17:02:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Sentence = sentence.split()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Sentence = sentence.split()
NameError: name 'sentence' is not defined
>>> hello
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    hello
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> # Define a function to list all files and folders in the current directory
... def list_files_in_directory():
...     # Print the current directory
...     print("Current directory:", os.getcwd())
...     # List all files and folders in the current directory
...     print("Files and folders in the current directory:")
...     for item in os.listdir():
...         print(item)
... 
... # Define a function to search for a word in a given file
... def search_word_in_file(file_path, word):
...     # Initialize a counter for the word occurrences
...     word_count = 0
...     # Open the file in read mode
...     with open(file_path, 'r') as file:
...         # Read each line in the file
...         for line in file:
...             # Count the occurrences of the word in the line (case insensitive)
...             word_count += line.lower().count(word.lower())
...     # Return the total count of word occurrences
...     return word_count
... 
... # Define the main function
... def main():
...     # List files and folders in the current directory
...     list_files_in_directory()
...     # Ask the user to enter the file name to search in
    file_name = input("Enter the name of the file to search in: ")
    # Check if the file exists
    if os.path.exists(file_name):
        # Ask the user to enter the word to search for
        word = input("Enter the word to search for: ")
        # Count the occurrences of the word in the file
        word_count = search_word_in_file(file_name, word)
        # Print the result
        print(f"The word '{word}' was found {word_count} times in the file: {file_name}")
    else:
        print("File not found.")

# Call the main function
if __name__ == "__main__":
