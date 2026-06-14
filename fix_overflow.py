import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace html block
css = re.sub(
    r'html \{[^}]+\}',
    'html {\n  scroll-behavior: smooth;\n  scroll-padding-top: var(--navbar-height);\n  -webkit-font-smoothing: antialiased;\n  -moz-osx-font-smoothing: grayscale;\n  overflow-x: hidden;\n  width: 100%;\n}',
    css
)

# Replace body block
css = re.sub(
    r'body \{[^}]+\}',
    'body {\n  font-family: var(--font-body);\n  font-size: 16px;\n  line-height: 1.7;\n  color: var(--text-primary);\n  background-color: var(--dark-bg);\n  overflow-x: hidden;\n  width: 100%;\n  position: relative;\n}',
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied strict overflow-x: hidden to html and body.")
