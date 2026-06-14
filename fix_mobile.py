with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* ===== HERO BTNS FIX ===== */
.hero-btns {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 30px;
}
''')

with open('css/responsive.css', 'r', encoding='utf-8') as f:
    resp = f.read()

# Add to max-width 768px section
mobile_css = '''
  .hero-btns {
    flex-direction: column;
    width: 100%;
  }
  .hero-btns .btn {
    width: 100%;
    text-align: center;
  }
'''

# Find a good place in max-width: 768px
import re
resp = re.sub(r'(@media \(max-width: 768px\) \{)', r'\1' + mobile_css, resp)

with open('css/responsive.css', 'w', encoding='utf-8') as f:
    f.write(resp)

print("CSS updated for hero-btns.")
