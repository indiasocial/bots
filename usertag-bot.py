#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import praw
import re
import praw
from psaw import PushshiftAPI


# In[ ]:


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)

target_sub = "IndiaSocial"
subreddit = reddit.subreddit(target_sub)
trigger_phrase = "u/"
usernameRegex = re.compile("/u/[A-Za-z0-9_-]+")
MIN_COMMENTS = 20


# In[ ]:


for comment in subreddit.stream.comments(skip_existing=True):
    if trigger_phrase in comment.body:
        result = usernameRegex.search(comment.body)
        print(result)


# In[ ]:


api = PushshiftAPI(reddit)

comments_generator = api.search_comments(after='7D', subreddit='indiasocial', limit=10) # Returns a generator object
comment_list = list(comments_generator)


# In[ ]:


c = 0
for commentID in comment_list:
    ID = str(commentID)
    commentID = reddit.comment(ID)
    author = commentID.author
    if str(author) == result:
        c = c + 1


# In[ ]:


print(c)


# In[ ]:




