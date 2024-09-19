def json_encode(data):
    if isinstance(data, str):
        return f'"{data}"'
    elif isinstance(data, bool):
        return "true" if data else "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(item) for item in data) + "]"
    elif isinstance(data, dict):
        items = []
        for key, value in data.items():
            encoded_key = json_encode(key)
            encoded_value = json_encode(value)
            items.append(f"{encoded_key}: {encoded_value}")
        return "{" + ", ".join(items) + "}"
    elif data is None:
        return "null"
    else:
        raise TypeError(f"Type {type(data)} not serializable")

# Example usage:
data = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

encoded_data = json_encode(data)
print(encoded_data)
