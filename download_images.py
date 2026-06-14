import urllib.request
import os

images = {
    'hero.jpg': 'https://images.unsplash.com/photo-1557838923-2985c318be48?auto=format&fit=crop&w=1200&q=80',
    'about.jpg': 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=800&q=80',
    'service-social.jpg': 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=800&q=80',
    'service-digital.jpg': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80',
    'service-campaign.jpg': 'https://images.unsplash.com/photo-1541802052445-56d11a687fc4?auto=format&fit=crop&w=800&q=80',
    'service-ads.jpg': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80',
    'service-print.jpg': 'https://images.unsplash.com/photo-1562504208-03d85ce8faa0?auto=format&fit=crop&w=800&q=80',
    'service-brand.jpg': 'https://images.unsplash.com/photo-1542435503-956c28f11550?auto=format&fit=crop&w=800&q=80',
    'portfolio-1.jpg': 'https://images.unsplash.com/photo-1555421689-d68471e189f2?auto=format&fit=crop&w=600&q=80',
    'portfolio-2.jpg': 'https://images.unsplash.com/photo-1475721025505-11756b17c762?auto=format&fit=crop&w=600&q=80',
    'portfolio-3.jpg': 'https://images.unsplash.com/photo-1533750516457-a7f992034fec?auto=format&fit=crop&w=600&q=80',
    'portfolio-4.jpg': 'https://images.unsplash.com/photo-1529369623266-f5264b696110?auto=format&fit=crop&w=600&q=80',
    'portfolio-5.jpg': 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=600&q=80',
    'portfolio-6.jpg': 'https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=600&q=80',
    'portfolio-7.jpg': 'https://images.unsplash.com/photo-1523381210434-271e8be1f52b?auto=format&fit=crop&w=600&q=80',
    'portfolio-8.jpg': 'https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&w=600&q=80',
    'blog-1.jpg': 'https://images.unsplash.com/photo-1432828689048-b042b4ee689b?auto=format&fit=crop&w=600&q=80',
    'blog-2.jpg': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=600&q=80',
    'blog-3.jpg': 'https://images.unsplash.com/photo-1512486130939-2c4f79935e4f?auto=format&fit=crop&w=600&q=80',
    'blog-4.jpg': 'https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?auto=format&fit=crop&w=600&q=80',
    'blog-5.jpg': 'https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&w=600&q=80',
    'blog-6.jpg': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=600&q=80',
    'team-1.jpg': 'https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=300&q=80',
    'team-2.jpg': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=300&q=80',
    'team-3.jpg': 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=300&q=80',
    'team-4.jpg': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=300&q=80'
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
