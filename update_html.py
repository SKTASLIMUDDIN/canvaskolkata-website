import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace Navbar Logo
    content = re.sub(
        r'<a href="index\.html" class="nav-logo">\s*<span class="logo-text">Canvas<span class="logo-accent">Kolkata</span></span>\s*</a>',
        '<a href="index.html" class="nav-logo">\n      <img src="assets/images/logo.png" alt="Canvas Kolkata Logo" class="brand-logo">\n    </a>',
        content
    )
    
    # Replace Footer Logo
    content = re.sub(
        r'<a href="index\.html" class="footer-logo">\s*<span class="logo-text">Canvas<span class="logo-accent">Kolkata</span></span>\s*</a>',
        '<a href="index.html" class="footer-logo">\n            <img src="assets/images/logo.png" alt="Canvas Kolkata Logo" class="brand-logo">\n          </a>',
        content
    )
    
    # Add authentic background image to hero
    if f == 'index.html':
        content = content.replace(
            '<section class="hero" id="home">',
            '<section class="hero" id="home" style="background: url(\'assets/images/hero.jpg\') no-repeat center center/cover; position: relative;">\n    <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: rgba(10,10,26,0.85); z-index: 1;"></div>'
        )
        # Ensure hero-content stays above the new background overlay
        content = content.replace('<div class="container hero-content">', '<div class="container hero-content" style="z-index: 2;">')
        
        # Replace About preview image
        content = content.replace(
            '<div class="about-preview-image-inner">',
            '<div class="about-preview-image-inner" style="background: url(\'assets/images/about.jpg\') center/cover;">\n            <div style="position:absolute;inset:0;background:rgba(108,60,225,0.4);"></div>'
        )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated HTML files with logos and hero/about images.")
