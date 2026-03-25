import feedparser

def get_news(symbol):
    query = symbol.replace('.NS', '')
    rss_url = f"https://news.google.com/rss/search?q={query}+stock&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:10]:
        articles.append({
            'title' : entry.title,
            'link' : entry.link,
            'published' : entry.published
        })
    return articles