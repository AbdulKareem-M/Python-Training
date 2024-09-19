import os
import sys
# import requests


def download_file(url):
    # Determine the filename
    if url.endswith('/'):
        filename = 'index.html'
    else:
        filename = os.path.basename(url)

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Write the content to a file
        with open(filename, 'wb') as file:
            file.write(response.content)

        print(f"Downloaded '{url}' and saved as '{filename}'")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download '{url}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wget.py <URL>")
    else:
        url = sys.argv[1]
        download_file(url)
