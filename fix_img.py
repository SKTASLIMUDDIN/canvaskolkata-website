import urllib.request
import os

url = 'https://images.unsplash.com/photo-1542435503-956c28f11550?auto=format&fit=crop&w=600&q=80'
path = os.path.join('assets', 'images', 'blog-ind-politics.jpg')

req = urllib.request.build_opener()
req.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(req)

try:
    urllib.request.urlretrieve(url, path)
    print("Downloaded replacement image")
except Exception as e:
    print("Failed", e)
