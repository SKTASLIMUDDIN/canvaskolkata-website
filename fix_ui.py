import urllib.request
import os
import re

images = {
    'blog-ind-politics.jpg': 'https://images.unsplash.com/photo-1532375810709-75b1d8d15229?auto=format&fit=crop&w=600&q=80',
    'blog-ind-digital.jpg': 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=600&q=80',
    'blog-ind-merch.jpg': 'https://images.unsplash.com/photo-1529369623266-f5264b696110?auto=format&fit=crop&w=600&q=80',
    'service-ind-social.jpg': 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=600&q=80',
    'service-ind-ads.jpg': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80'
}

req = urllib.request.build_opener()
req.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(req)

for name, url in images.items():
    path = os.path.join('assets', 'images', name)
    try:
        urllib.request.urlretrieve(url, path)
        print(f'Downloaded {name}')
    except Exception as e:
        print(f'Failed to download {name}: {e}')

# Fix index.html classes and gradients
with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Replace classes
content = content.replace('class="blog-title"', 'class="blog-card-title"')
content = content.replace('class="blog-excerpt"', 'class="blog-card-excerpt"')
content = content.replace('class="blog-image"', 'class="blog-card-image"')
content = content.replace('class="blog-meta"', 'class="blog-card-meta"')
content = content.replace('class="blog-read-more"', 'class="blog-card-link"')

# Replace gradients with images in index.html blog cards
content = re.sub(
    r'<div class="blog-card-image" style="background: linear-gradient[^"]+;">',
    r'<div class="blog-card-image" style="background: url(\'assets/images/blog-ind-politics.jpg\') center/cover;">\n            <div style="position:absolute;inset:0;background:rgba(18,18,42,0.5);"></div>',
    content, count=1
)
content = re.sub(
    r'<div class="blog-card-image" style="background: linear-gradient[^"]+;">',
    r'<div class="blog-card-image" style="background: url(\'assets/images/blog-ind-digital.jpg\') center/cover;">\n            <div style="position:absolute;inset:0;background:rgba(18,18,42,0.5);"></div>',
    content, count=1
)
content = re.sub(
    r'<div class="blog-card-image" style="background: linear-gradient[^"]+;">',
    r'<div class="blog-card-image" style="background: url(\'assets/images/blog-ind-merch.jpg\') center/cover;">\n            <div style="position:absolute;inset:0;background:rgba(18,18,42,0.5);"></div>',
    content, count=1
)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(content)

# Fix services.html gradients
with open('services.html', 'r', encoding='utf-8') as file:
    s_content = file.read()

s_content = re.sub(
    r'<div class="service-detail-visual" style="background: linear-gradient[^"]+;">',
    r'<div class="service-detail-visual" style="background: url(\'assets/images/service-ind-social.jpg\') center/cover;">\n          <div style="position:absolute;inset:0;background:rgba(108,60,225,0.6);"></div>',
    s_content, count=1
)
s_content = re.sub(
    r'<div class="service-detail-visual" style="background: linear-gradient[^"]+;">',
    r'<div class="service-detail-visual" style="background: url(\'assets/images/service-ind-ads.jpg\') center/cover;">\n          <div style="position:absolute;inset:0;background:rgba(255,107,53,0.6);"></div>',
    s_content, count=1
)

with open('services.html', 'w', encoding='utf-8') as file:
    file.write(s_content)

print("HTML classes fixed and images applied.")
