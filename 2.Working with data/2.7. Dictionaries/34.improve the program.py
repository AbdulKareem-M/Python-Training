def read_words(filename):
    with open(filename, 'r') as file:
        return file.read().split()


def word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def main(filename):
    frequency = word_frequency(read_words(filename))
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_frequency:
        print(word, count)


if __name__ == "__main__":
    import sys
    filename = input('enter filename')
    main(filename)

