import requests
import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

params = parse.urlencode({
  "q": "AdrianoRibeiro",  "api_key":"VYWxJYA6f6mWYy7bst57AKe4YhtqaH67",
  "limit": "5"
})

with request.urlopen("".join((url, "?", params))) as response:
  data = json.loads(response.read())

print(json.dumps(data, sort_keys=True, indent=4))

requisicao = requests.get ("https://api.giphy.com/v1/gifs/search?api_key=VYWxJYA6f6mWYy7bst57AKe4YhtqaH67&q=feliz&limit=1&offset=0&rating=g&lang=en")
print (requisicao)
print (requisicao.json())

