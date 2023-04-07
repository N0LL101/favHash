import mmh3
import requests
import codecs

url_ico = input("enter the url : ")


responce = requests.get(url_ico)

favicon=codecs.encode(responce.content,"base64")

hash = mmh3.hash(favicon)

print(hash)
