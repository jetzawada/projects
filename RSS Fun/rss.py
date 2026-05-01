import feedparser
import pandas as pd

def scrape_rss(url):
    feed = feedparser.parse(url)
    print(feed.feed)

    return feed.entries

def filter_and_save(df, save_to):
    df_filtered = df[['title', 'summary']]

    print("Filtered content")
    print(df_filtered)

    df_filtered.to_csv('news.csv', index=False)
    print("Saved filtered content to " + save_to)


urlNz = "https://www.rnz.co.nz/rss/national.xml"
saveTo = "news.csv"

entries = scrape_rss(urlNz)

unfiltered_df = pd.DataFrame(entries)

filter_and_save(unfiltered_df, saveTo)





