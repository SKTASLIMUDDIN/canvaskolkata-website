import os
import re

blog_posts = [
    {
        "id": "political-campaigns",
        "filename": "blog-political-campaigns.html",
        "title": "5 Social Media Strategies for Political Campaigns in 2026",
        "content": """
            <h2>1. Authentic Video Content</h2>
            <p>In 2026, voters crave authenticity. Polished ads are taking a backseat to raw, behind-the-scenes video content that shows the human side of a candidate. Short-form videos on Instagram Reels and YouTube Shorts are critical for reaching younger demographics.</p>
            
            <h2>2. Micro-Targeting with Data</h2>
            <p>General messages are less effective. Utilizing data analytics to understand hyper-local issues allows campaigns to tailor their messaging to specific neighborhoods, ensuring that the concerns of the community are directly addressed.</p>
            
            <h2>3. Community Management and Engagement</h2>
            <p>Social media is a two-way street. It's not enough to just broadcast; campaigns must actively engage. Responding to comments, hosting live Q&A sessions, and fostering community discussions build trust and loyalty.</p>
            
            <h2>4. Leveraging Influencer Partnerships</h2>
            <p>Partnering with local micro-influencers who share the campaign's values can significantly amplify reach. These influencers already have the trust of their audience, making their endorsement highly valuable.</p>
            
            <h2>5. Combating Misinformation Proactively</h2>
            <p>With the rise of deepfakes and rapid misinformation, campaigns must have a rapid-response team ready to debunk false claims with clear, fact-based content across all platforms.</p>
        """
    },
    {
        "id": "digital-marketing",
        "filename": "blog-digital-marketing.html",
        "title": "Why Your Business Needs Digital Marketing in Kolkata",
        "content": """
            <p>Kolkata is rapidly evolving into a digital hub. As consumer behavior shifts towards online research and purchasing, local businesses must adapt or risk being left behind. Here's why digital marketing is no longer optional in Kolkata.</p>
            <h2>Visibility in a Crowded Market</h2>
            <p>With thousands of businesses vying for attention, relying solely on foot traffic and word-of-mouth is insufficient. Local SEO ensures your business appears when potential customers search for your services.</p>
            <h2>Cost-Effective Advertising</h2>
            <p>Compared to traditional print or billboard advertising, digital marketing—specifically targeted social media and search ads—offers a much higher return on investment (ROI) by reaching the exact demographic most likely to convert.</p>
            <h2>Building Brand Trust</h2>
            <p>A strong online presence, characterized by a professional website, active social media, and positive reviews, establishes credibility and trust with potential customers before they even contact you.</p>
        """
    },
    {
        "id": "branded-merchandise",
        "filename": "blog-branded-merchandise.html",
        "title": "The Power of Branded Merchandise for Your Campaign",
        "content": """
            <p>In an increasingly digital world, tangible items hold unique power. Branded merchandise—like t-shirts, caps, and badges—serves as a physical touchpoint that extends the lifespan of your campaign far beyond a single event.</p>
            <h2>Creating Walking Billboards</h2>
            <p>When supporters wear your merchandise, they become mobile advertisements, organically spreading your message and logo throughout their daily lives.</p>
            <h2>Fostering a Sense of Belonging</h2>
            <p>Merchandise creates a unifying identity among your supporters or team members. It fosters a sense of community and shared purpose, which is especially vital for political campaigns and NGOs.</p>
            <h2>High Recall Value</h2>
            <p>People tend to keep useful items. A well-designed cap or a high-quality t-shirt will be used repeatedly, ensuring your brand stays top-of-mind long after the initial interaction.</p>
        """
    },
    {
        "id": "google-vs-meta-ads",
        "filename": "blog-google-vs-meta-ads.html",
        "title": "Google Ads vs META Ads: Which is Right?",
        "content": """
            <p>Choosing between Google Ads and META (Facebook/Instagram) Ads is a common dilemma. Both are powerful, but they serve fundamentally different purposes in the customer journey.</p>
            <h2>Google Ads: Capturing Intent</h2>
            <p>Google Ads excel when users are actively searching for a specific product or service. They have high "intent." If someone searches for "best marketing agency in Kolkata," they are likely ready to hire one. Google Ads capture this bottom-of-the-funnel traffic.</p>
            <h2>META Ads: Generating Awareness</h2>
            <p>META Ads are unparalleled for building brand awareness and generating interest. You are interrupting a user's feed with compelling visuals. It's ideal for products or services people might not know they need yet, or for building a strong visual brand identity.</p>
            <h2>The Verdict</h2>
            <p>For most comprehensive strategies, a combination is best. Use META Ads to build awareness and generate demand, and use Google Ads to capture that demand when users start searching.</p>
        """
    },
    {
        "id": "ngo-social-media",
        "filename": "blog-ngo-social-media.html",
        "title": "How NGOs Can Leverage Social Media",
        "content": """
            <p>For Non-Governmental Organizations (NGOs), social media is a critical tool for advocacy, fundraising, and volunteer recruitment. It allows NGOs to bypass traditional media gatekeepers and speak directly to the public.</p>
            <h2>Storytelling is Key</h2>
            <p>The most successful NGO campaigns rely on emotional storytelling. Share the real stories of the people or communities you are helping. High-quality visuals and videos are essential here.</p>
            <h2>Transparent Impact Reporting</h2>
            <p>Donors want to know where their money is going. Use social media to provide regular, transparent updates on the impact of their contributions. Showing tangible results builds long-term trust.</p>
            <h2>Mobilizing Action</h2>
            <p>Social media is perfect for quick mobilization. Whether it's signing a petition, attending a rally, or raising emergency funds, clear calls-to-action on platforms like Twitter and Facebook can drive immediate results.</p>
        """
    },
    {
        "id": "print-marketing",
        "filename": "blog-print-marketing.html",
        "title": "Print Marketing is Not Dead",
        "content": """
            <p>Despite the digital revolution, print marketing remains a highly effective, and sometimes necessary, component of a complete marketing strategy. It offers a tactile experience that digital simply cannot replicate.</p>
            <h2>Standing Out in the Physical World</h2>
            <p>While digital inboxes are overflowing, physical mailboxes are less crowded. A well-designed, high-quality brochure or direct mail piece can capture attention in a way an email often fails to do.</p>
            <h2>Credibility and Permanence</h2>
            <p>Print materials carry an inherent weight and credibility. A premium business card or a glossy catalog signals professionalism and stability. Furthermore, print materials linger on desks and coffee tables, providing repeated exposure.</p>
            <h2>Integration with Digital</h2>
            <p>The best campaigns integrate both. Using QR codes on print materials seamlessly bridges the gap, driving offline engagement to online action.</p>
        """
    },
    {
        "id": "brand-identity",
        "filename": "blog-brand-identity.html",
        "title": "Building a Brand Identity on a Budget",
        "content": """
            <p>You don't need a massive budget to build a strong, memorable brand identity. Consistency and clarity are far more important than expensive design work.</p>
            <h2>Define Your Core Message</h2>
            <p>Before designing anything, you must know what your brand stands for. What is your mission? Who is your target audience? What is your unique value proposition? Clarifying these points forms the foundation of your identity.</p>
            <h2>Consistent Visual Language</h2>
            <p>Choose a simple color palette (2-3 colors) and a maximum of two fonts. Stick to them religiously across all platforms—from your website to your social media graphics to your business cards. Consistency breeds recognition.</p>
            <h2>Leverage Free and Low-Cost Tools</h2>
            <p>Tools like Canva offer professional-grade templates for social media and marketing materials. While a custom logo is ideal, a clean, typography-based logo can look incredibly premium and costs nothing to create.</p>
        """
    }
]

with open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

head_end = blog_content.find('</nav>') + 6
footer_start = blog_content.find('<section class="cta-banner">')
if footer_start == -1:
    footer_start = blog_content.find('<footer')

header = blog_content[:head_end]
footer = blog_content[footer_start:]

post_css = """
<style>
.blog-post-header {
    padding: 150px 0 50px;
    background: var(--darker-bg);
    text-align: center;
}
.blog-post-title {
    font-size: 3rem;
    margin-bottom: 20px;
}
.blog-post-content {
    padding: 50px 0 100px;
    max-width: 800px;
    margin: 0 auto;
}
.blog-post-content h2 {
    margin-top: 40px;
    margin-bottom: 20px;
    color: var(--text-primary);
}
.blog-post-content p {
    margin-bottom: 20px;
    line-height: 1.8;
    color: var(--text-secondary);
    font-size: 1.1rem;
}
</style>
"""
header = header.replace('</head>', post_css + '</head>')

for post in blog_posts:
    post_html = header + f'''
    <section class="blog-post-header">
        <div class="container">
            <h1 class="blog-post-title gradient-text">{post['title']}</h1>
            <p class="text-muted">By Canvas Kolkata Expert Team</p>
        </div>
    </section>
    <section class="blog-post-content container">
        {post['content']}
        <div style="margin-top: 50px; text-align: center;">
            <a href="blog.html" class="btn btn-outline">← Back to Blog</a>
        </div>
    </section>
    ''' + footer
    
    with open(post['filename'], 'w', encoding='utf-8') as f:
        f.write(post_html)

for post in blog_posts:
    title_anchor = f'<a href="#">{post["title"]}</a>'
    new_title_anchor = f'<a href="{post["filename"]}">{post["title"]}</a>'
    blog_content = blog_content.replace(title_anchor, new_title_anchor)
    pattern = r'(' + re.escape(post["title"]) + r'.*?<a href=")#[^"]*(" class="blog-read-more")'
    blog_content = re.sub(pattern, r'\1' + post["filename"] + r'\2', blog_content, flags=re.DOTALL)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_content)

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

for post in blog_posts:
    title_anchor = f'<a href="#">{post["title"]}</a>'
    new_title_anchor = f'<a href="{post["filename"]}">{post["title"]}</a>'
    index_content = index_content.replace(title_anchor, new_title_anchor)
    pattern = r'(' + re.escape(post["title"]) + r'.*?<a href=")blog\.html(" class="blog-read-more")'
    index_content = re.sub(pattern, r'\1' + post["filename"] + r'\2', index_content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Blog posts created and links updated successfully.")
