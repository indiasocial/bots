import praw

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

target_sub = ""
subreddit = reddit.subreddit(target_sub)
trigger_phrase = "!flair"

for comment in subreddit.stream.comments():
  
    if trigger_phrase in comment.body:
  
        word = comment.body.replace(trigger_phrase, "")
        author = comment.author
        subreddit.flair.set(author, text=word)
