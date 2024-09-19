def nearly_equal(a, b):
    # If the length difference is more than 1, they can't be nearly equal
    if abs(len(a) - len(b)) > 1:
        return False

    # If the strings are of the same length, check for a single substitution
    if len(a) == len(b):
        count_diff = sum(1 for x, y in zip(a, b) if x != y)
        return count_diff == 1

    # If the strings are of different lengths, check for a single insertion/deletion
    if len(a) > len(b):
        a, b = b, a  # Ensure a is the shorter string

    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] != b[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1

    return True


# Example usage
print(nearly_equal("abc", "ab"))  # True (deletion)
print(nearly_equal("abc", "abcd"))  # True (insertion)
print(nearly_equal("abc", "adc"))  # True (substitution)
print(nearly_equal("abc", "abx"))  # False (more than one mutation)
