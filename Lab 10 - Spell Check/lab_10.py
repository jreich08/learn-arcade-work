import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def read_in_file(file_name):
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open(file_name)

    # Create an empty list to store our text lines
    line_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        line_list.append(line)

    my_file.close()

    return line_list

def linear_search(word, dictionary):
    # --- Linear search


    # Start at the beginning of the list
    current_position_in_dictionary = 0

    # Loop until you reach the end of the dictionary, or the value at the
    # current position is equal to the word

    while current_position_in_dictionary < len(dictionary) and dictionary[current_position_in_dictionary] != word:
        # Advance to the next word in the list
        current_position_in_dictionary += 1

    if current_position_in_dictionary < len(dictionary):
        return True
    else:
        return False

def main():
    dictionary_words = read_in_file("dictionary.txt")
   # print(f"There are {len(dictionary_words)} words in the dictionary.")
   #for word in dictionary_words:
    #    print(word)

    chapter_lines = read_in_file("AliceInWonderLand200.txt")
    #chapter_words = []
    #for line in chapter_lines:
    for i in range(len(chapter_lines)):
        words = split_line(chapter_lines[i])
        for word in words:
             if not linear_search(word.upper(), dictionary_words):
                 print(f'The word \'{word}\' is not in the dictionary.')
                 print(f'Discrepancy found on line {i+1}. ')




main()