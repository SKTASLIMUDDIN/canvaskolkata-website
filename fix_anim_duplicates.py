import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all instances of the animation div
# We will match from <div class="hero-desktop-anim" to the closing </div>
# Since the div contains an img, we can just match it non-greedily
pattern = r'\s*<div class="hero-desktop-anim">.*?</div>\n'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# Also match if there's any weird spacing
pattern2 = r'<div class="hero-desktop-anim">.*?</div>'
content = re.sub(pattern2, '', content, flags=re.DOTALL)

# Clean up any leftover empty lines that might have been caused
content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

# Now, strictly insert it ONLY in the hero section
hero_pattern = r'(<section class="hero" id="hero">\s*<canvas class="hero-canvas" id="hero-canvas"></canvas>\s*)(<div class="container">)'

anim_html = '''
    <div class="hero-desktop-anim">
        <img src="assets/images/hero-desktop.jpg" alt="Marketing Strategy" class="hero-floating-img">
    </div>
    '''

content = re.sub(hero_pattern, r'\1' + anim_html + r'\2', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned up duplicated animations and inserted one precisely in hero section.")
