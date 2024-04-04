import re

def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): a string containing one or more words.

    Returns:
        list of str: a list of words from s converted to lower-case.
    """
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words

class UniqueWords:
    """A class for identifying and managing unique words in text files."""

    def __init__(self):
        """Initialize the UniqueWords instance."""
        self.all_words = set()
        self.unique_words = set()
        self.words_by_file = {}

    def add_file(self, filename, key):
        """Add a file's words to the UniqueWords instance.

        Args:
            filename (str): The path to the file to be read.
            key (str): A nickname for the file.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            words = set(get_words(file_contents))
            self.words_by_file[key] = words

            # Update unique_words and all_words
            new_words = words - self.all_words
            self.unique_words.update(new_words)
            self.all_words.update(new_words)

    def unique(self, key):
        """Get the set of words unique to a specified file.

        Args:
            key (str): A nickname for the file.

        Returns:
            set: The set of words unique to the specified file.
        """
        return self.words_by_file[key] - (self.all_words - self.words_by_file[key])




# Example usage
if __name__ == "__main__":
    # Create an instance of UniqueWords
    unique_word_counter = UniqueWords()

    # Add files and specify their keys
    unique_word_counter.add_file("federalist_01.txt", "File 1")
    unique_word_counter.add_file("federalist_02.txt", "File 2")

    # Get and print unique words for a specific file
    unique_words_file1 = unique_word_counter.unique("File 1")
    unique_words_file2 = unique_word_counter.unique("File 2")

    print("Unique words in File 1:", unique_words_file1)
    print("Unique words in File 2:", unique_words_file2)
