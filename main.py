import sys
import xbmcgui
import xbmcplugin
import urllib

__url__ = sys.argv[0]
__handle__ = int(sys.argv[1])

with urllib.request.urlopen('https://filmy.ml/app/channels.js') as f:
    with f.decode('utf-8') as a
        with a.split("var ")[1] as r
            eval(r.split(";")[0])

def list_videos():
    listing = []
    for video in channels:
        list_item = xbmcgui.ListItem(label=video['name'], thumbnailImage=video['thumb'])
        list_item.setProperty('fanart_image', video['thumb'])
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        list_item.setProperty('IsPlayable', 'true')
        url = '{0}?action=play&video={1}'.format(__url__, video['video'])
        is_folder = False
        listing.append((url, list_item, is_folder))
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(__handle__)

def play_video(path):
    play_item = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(__handle__, True, listitem=play_item)

def router(paramstring):
    params = dict(parse_qsl(paramstring[1:]))
    if params:
        if params['action'] == 'play':
            play_video(params['video'])
    else:
        list_videos()

if __name__ == '__main__':
    router(sys.argv[2])
