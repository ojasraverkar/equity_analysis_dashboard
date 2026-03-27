import feedparser
import zoneinfo
from datetime import datetime, timezone
import time

def convert_to_ist(dt_utc):
    ist = zoneinfo.ZoneInfo("Asia/Kolkata")
    return dt_utc.astimezone(ist).strftime("%a, %d %b %Y %H:%M:%S IST")

def parse_news_time(entry):
    if hasattr(entry, 'published_parsed') and entry.published_parsed:
        try:
            dt_utc = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            return convert_to_ist(dt_utc)
        except:
            pass

    pub_str = entry.get('published', '')
    if pub_str:
        for fmt in ["%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"]:
            try:
                dt_utc = datetime.strptime(pub_str, fmt).replace(tzinfo=timezone.utc)
                return convert_to_ist(dt_utc)
            except:
                continue
        return pub_str
    return ""

def get_news(symbol):
    query = symbol.replace('.NS', '')
    rss_url = f"https://news.google.com/rss/search?q={query}+stock&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:10]:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': parse_news_time(entry)
        })
    return articles