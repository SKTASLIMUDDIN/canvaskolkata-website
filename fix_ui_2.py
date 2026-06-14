import re
import os
import urllib.request

images_to_download = {
    'hero-desktop.jpg': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80',
    'service-campaign.jpg': 'https://images.unsplash.com/photo-1541802052445-56d11a687fc4?auto=format&fit=crop&w=800&q=80',
    'service-print.jpg': 'https://images.unsplash.com/photo-1562504208-03d85ce8faa0?auto=format&fit=crop&w=800&q=80',
    'service-brand.jpg': 'https://images.unsplash.com/photo-1542435503-956c28f11550?auto=format&fit=crop&w=800&q=80',
    'portfolio-2.jpg': 'https://images.unsplash.com/photo-1475721025505-11756b17c762?auto=format&fit=crop&w=600&q=80',
}

req = urllib.request.build_opener()
req.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(req)

for name, url in images_to_download.items():
    path = os.path.join('assets', 'images', name)
    if not os.path.exists(path):
        try:
            urllib.request.urlretrieve(url, path)
            print(f"Downloaded {name}")
        except:
            # Fallback
            urllib.request.urlretrieve('https://picsum.photos/600/400', path)

# 1. Update Services HTML
with open('services.html', 'r', encoding='utf-8') as f:
    services_html = f.read()

services = [
    'service-social.jpg', 'service-digital.jpg', 'service-campaign.jpg',
    'service-ads.jpg', 'service-print.jpg', 'service-brand.jpg'
]

# We need to replace the symbolic icons in services.html. 
# Some were replaced in previous tasks but left the <i> tags.
# Let's clean up all .service-detail-visual
for i, img in enumerate(services):
    # Regex to match the whole visual div and replace it
    # We'll just find all service-detail-visual and replace them in order
    pass

# A simpler way to replace all service-detail-visuals in order:
parts = re.split(r'(<div class="service-detail-visual"[^>]*>.*?</div>)', services_html, flags=re.DOTALL)
new_parts = []
img_index = 0
for part in parts:
    if part.startswith('<div class="service-detail-visual"'):
        if img_index < len(services):
            new_part = f'<div class="service-detail-visual" style="background: url(\'assets/images/{services[img_index]}\') center/cover;"><div style="position:absolute;inset:0;background:rgba(18,18,42,0.4);"></div></div>'
            new_parts.append(new_part)
            img_index += 1
        else:
            new_parts.append(part)
    else:
        new_parts.append(part)

services_html = "".join(new_parts)
with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services_html)

# 2. Update Portfolio HTML
with open('portfolio.html', 'r', encoding='utf-8') as f:
    portfolio_html = f.read()

port_parts = re.split(r'(<div class="portfolio-card-bg"[^>]*>.*?</div>)', portfolio_html, flags=re.DOTALL)
new_port_parts = []
p_img_idx = 1
for part in port_parts:
    if part.startswith('<div class="portfolio-card-bg"'):
        if p_img_idx <= 8:
            new_part = f'<div class="portfolio-card-bg" style="background: url(\'assets/images/portfolio-{p_img_idx}.jpg\') center/cover;"></div>'
            new_port_parts.append(new_part)
            p_img_idx += 1
        else:
            new_port_parts.append(part)
    else:
        new_port_parts.append(part)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write("".join(new_port_parts))

# 3. Update Index HTML Hero and Services grid
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Add desktop animation to hero
hero_anim = '''
    <div class="hero-desktop-anim">
        <img src="assets/images/hero-desktop.jpg" alt="Marketing Strategy" class="hero-floating-img">
    </div>
'''
if 'hero-desktop-anim' not in index_html:
    index_html = index_html.replace('<div class="hero-content">', hero_anim + '<div class="hero-content">')

# Add CSS for desktop anim to style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

anim_css = '''
/* Hero Desktop Animation */
.hero-desktop-anim {
    position: absolute;
    right: 5%;
    top: 25%;
    width: 400px;
    height: 300px;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    border: 2px solid rgba(255,255,255,0.1);
    animation: float 6s ease-in-out infinite;
    z-index: 2;
    display: none;
}
.hero-floating-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
@media (min-width: 1024px) {
    .hero-desktop-anim {
        display: block;
    }
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
}
'''
if 'hero-desktop-anim' not in style_css:
    style_css += anim_css
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(style_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updates completed successfully.")
