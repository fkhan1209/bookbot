def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        #return (file_contents)
        file_words = word_count(file_contents)
        char_dict = char_count(file_words)
        sorted_char_dict = dict(sorted(char_dict.items(), key=lambda x:x[1], reverse=True))
        for key,value in sorted_char_dict.items():
            print (f"The {key} character was found {value} times.")

def word_count(file_contents):
    file_words = file_contents.split()
    print(len(file_words))
    return(file_words)

char_dict = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0,
    ":":0,
    "/":0,
    ",":0,
    ".":0,
    "-":0,
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "'":0
}

def char_count(file_words):
    for word in file_words:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
    return(char_dict)
    
main()
#file_words = word_count()
#char_dict = char_count(file_words)


