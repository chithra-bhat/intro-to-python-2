import string
rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def bleeper(word):
    # Write code to replace rude words with asterisks
    no_punct_word = word.strip(string.punctuation)
    n = len(no_punct_word)
    replacement_word = '*' * n
    pos = word.find(no_punct_word)
    word = word.replace(word[pos:pos + n], replacement_word)
    return word


def check_line(line):
    new_list = []
    rude_count = 0
    words = line.split(" ")
    for index, word in enumerate(words):
        word_processed = word.strip(string.punctuation).lower()
        if word_processed in rude_words:
            rude_count += 1
            new_word = bleeper(word)
            new_list.append(new_word)
        else:
            new_list.append(word)

    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")

    else:
        print("There is/are {} rude word(s) in the file.".format(rude_count))
    return new_list


def check_file(filename):
    new_line = " "
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            new_line = " ".join(check_line(line))
    with open("output.txt", 'w') as of:
        of.write(new_line)


if __name__ == '__main__':
    check_file("my_other_story.txt")
