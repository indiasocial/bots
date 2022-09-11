import urllib.request
import re
import praw
import json
import urllib

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

target_sub = ""
subreddit = reddit.subreddit(target_sub)
trigger_phrase = "!alexa"

for comment in subreddit.stream.comments():
  
    if trigger_phrase in comment.body:
  
        search_word = comment.body.replace(trigger_phrase, "")
        search_string = search_word.replace(" ","+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_string)
        video_ids = ""
        data = ""
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_ids[0]}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            #print(data['title'])
            comment.reply("https://www.youtube.com/watch?v=" + video_ids[0]+'\n'+data['title'])
