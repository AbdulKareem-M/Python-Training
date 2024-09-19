import string

def mutate(word):
    mutations = []
    letters = string.ascii_lowercase

    # Insert a character
    for i in range(len(word) + 1):
        for char in letters:
            mutations.append(word[:i] + char + word[i:])

    # Delete a character
    for i in range(len(word)):
        mutations.append(word[:i] + word[i+1:])

    # Replace a character
    for i in range(len(word)):
        for char in letters:
            if char != word[i]:
                mutations.append(word[:i] + char + word[i+1:])

    # Swap two consecutive characters
    for i in range(len(word) - 1):
        mutations.append(word[:i] + word[i+1] + word[i] + word[i+2:])

    return mutations


# Example usage:
word = "cat"
mutations = mutate(word)
for mutation in mutations:
    print(mutation)
