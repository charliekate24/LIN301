import urllib.request

url = "https://www.gutenberg.org/files/141/141-0.txt"  # Mansfield Park
filename = "../../data/gutenberg/mansfield_park.txt"

try:
    urllib.request.urlretrieve(url, filename)
    print("Downloaded:", filename)
except FileNotFoundError:
    print("Couldn't save the file — does the ../../data/gutenberg/ folder exist?")