import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Revert Navbar Logo
    content = re.sub(
        r'<img src="assets/images/logo.png" alt="Canvas Kolkata Logo" class="brand-logo">',
        '<span class="logo-text">Canvas<span class="logo-accent">Kolkata</span></span>',
        content
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Reverted logo image to text logo in all HTML files.")
