import requests

# Define the API endpoint and parameters
endpoint = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "titles": "food",
    "prop": "extracts|pageimages",
    "exintro": 1,
    "explaintext": 1,
    "pithumbsize": 500,
    "utf8": 1,
}

# Send a GET request to the API endpoint
response = requests.get(endpoint, params=params)

# Parse the response JSON and extract the article text and image
data = response.json()
page_id = next(iter(data["query"]["pages"]))
article = data["query"]["pages"][page_id]
#print(article)
# Print the article title, text, and image URL
print("Title: ", article["title"])
print("Text: ", article["extract"])
try:
    print("Image URL: ", article['thumbnail']["source"])
except:
    print('no image')

