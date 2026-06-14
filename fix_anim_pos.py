with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove from hero-content
content = content.replace('''    <div class="hero-desktop-anim">
        <img src="assets/images/hero-desktop.jpg" alt="Marketing Strategy" class="hero-floating-img">
    </div>
''', '')

# Add as sibling to container
anim = '''    <div class="hero-desktop-anim">
        <img src="assets/images/hero-desktop.jpg" alt="Marketing Strategy" class="hero-floating-img">
    </div>
'''
if 'hero-desktop-anim' not in content:
    content = content.replace('<div class="container">', anim + '    <div class="container">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
