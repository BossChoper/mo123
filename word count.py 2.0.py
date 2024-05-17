


 display_current_directory():
    print("Current working directory:",
    print("Files and folders in the current directory:")
    for item in os.listdir():
        print(item)

 get_target_file():
    while True:
        file_path = input("Enter the path of the file to search: ")
        if os.path.exists(file_path):
            return file_path
        else:
            print("Error: The specified file does not exist. Please try again.")

 get_search_word():
    while True:
        s
           search_word     = input("Enter the word to search for (single word only): ")
        if len(search_word.split()) == 1:
            return search_word
        else:
            print("Error: Only single words are allowed. Please try again.")

 count_word_occurrences(file_path, search_word, case_sensitive=True):
    with open(file_path, 'r') as file:
        text = file.read()
        if not case_sensitive:
            text = text.lower()
            search_word = search_word.lower()
        occurrences = text.count(search_word)
    return occurrences

 main():
    display_current_directory()
    target_file = get_target_file()
    search_word = get_search_word()
    case_sensitive_input = input("Do you want the search to be case sensitive? (yes/no): ").lower()
    case_sensitive = case_sensitive_input == "yes"

    try:
        word_count = count_word_occurrences(target_file, search_word, case_sensitive)
        print(f"The word '{search_word}' was found {word_count} times in the file: {target_file}")
    except Exception as e:
        print("An error occurred:", e)

 __momin__ == "__main__":
    main()
