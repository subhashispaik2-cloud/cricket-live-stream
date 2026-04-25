import requests

# ফ্রি সোর্স থেকে লিঙ্ক খোঁজার চেষ্টা
SOURCE_URL = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/in.m3u"

def get_link():
    try:
        r = requests.get(SOURCE_URL)
        lines = r.text.split('\n')
        for i, line in enumerate(lines):
            if "Star Sports" in line or "Cricket" in line:
                return lines[i+1].strip()
    except: pass
    return "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"

link = get_link()

html = f"""
<html>
<head>
    <title>Live Cricket</title>
    <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />
    <style>body{{background:#000; color:#fff; text-align:center; padding-top:50px;}}</style>
</head>
<body>
    <h1>Cricket Live Stream</h1>
    <video id="player" class="video-js vjs-default-skin vjs-big-play-centered" controls width="800" height="450">
        <source src="{link}" type="application/x-mpegURL">
    </video>
    <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
</body>
</html>
"""
with open("index.html", "w") as f:
    f.write(html)
