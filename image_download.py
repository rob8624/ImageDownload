import os
import requests
from newspaper import Article

#Script to download and save all images from a given URL, useful if the URL is behind
#a paywall and you need to check which images have been used. It uses the 
#Newspaperk3k package to gather images and requests to save them locally.

url = ''

article = Article(url)
article.download()
try:
    article.parse()
except Exception as e:
    print(f'Error {e}, maybe the URL is empty.')

#create a folder on local machine to save images
folder_name = 'image_dl'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


all_images = article.images

for index, image_url in enumerate(all_images):
    try:
        response = requests.get(image_url)
        file_name = os.path.join(folder_name, f'image_{index}.jpg')

        with open(file_name, 'wb') as f:
            f.write(response.content)
            print(f"Image {index} downloaded and saved as {file_name}")
    except Exception as e:
        print(f"Could not get images")
