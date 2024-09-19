def unflatten_dict(d, sep='.'):
    result_dict = {}
    for key, value in d.items():
        parts = key.split(sep)
        d = result_dict
        for part in parts[:-1]:
            if part not in d:
                d[part] = {}
            d = d[part]
        d[parts[-1]] = value
    return result_dict


# Example usage:
flattened_dict = {
    'a.b': 1,
    'a.c.d': 2,
    'a.c.e': 3,
    'f': 4
}

nested = unflatten_dict(flattened_dict)
print(nested)
