from __future__ import unicode_literals

import subprocess, os
import youtube_dl


if __name__ == '__main__':
    live_link = input('Youtube live Link\n: ')
    yt = youtube_dl.YoutubeDL({'quiet': True})
    stream_info = yt.extract_info(live_link, download=False)
    print(f"{len(stream_info['formats'])} stream quality found.")
    stream_links = []

    for i, stream in enumerate(stream_info['formats'], 1):
        stream_links.append((stream['format'], stream['url']))
        print(f"{i}. Quality: {stream['format']}")
    sel = input('Select Resolution to stream\n: ')
    if int(sel) > len(stream_links):
        print('Please Enter number from above list.')
    else:
        q, link_selected = stream_links[int(sel)-1]
        try:
            print('Starting the stream...(press CTRL+C to close)')
            # os.system(f'ffmpeg -re -i {link_selected} -c copy -f flv rtmp://127.0.0.1:1935/live/yt')
            subprocess.run(['ffmpeg', '-re', '-i', link_selected, '-c', 'copy', '-f', 'flv', 'rtmp://127.0.0.1:1935/live/yt'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, check=True)
        except KeyboardInterrupt:
            exit()

# don't close cmd window
input('\nPress Any key to exit.')