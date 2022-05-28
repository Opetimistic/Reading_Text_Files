# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    read_file = ""
    with open(filename, 'r') as open_file:
        read_file = open_file.read()
    # return "Hello World"
    return read_file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = {}
    for word in text.split(" "):
        word = word.strip()
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace("?", "")
        count[word] = count.get(word, 0) + 1
    # return {"as": 10, "would": 20}
    return count


print(count_words())
