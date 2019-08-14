from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL0 = "https://anchor.fm/s/a935558/podcast/rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://d3t3ozftmdmh3i.cloudfront.net/production/podcast_uploaded/1674278/1674278-1564177705682-bea0801e2e24b.jpg"},
   {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('latest_episodes'),
            'thumbnail': "https://d3t3ozftmdmh3i.cloudfront.net/production/podcast_uploaded/1674278/1674278-1564177705682-bea0801e2e24b.jpg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL0)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_episodes/')
def latest_episodes():
    soup = mainaddon.get_soup(URL0)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
