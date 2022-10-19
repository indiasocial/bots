{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27fd69ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "import praw\n",
    "import re\n",
    "import praw\n",
    "from psaw import PushshiftAPI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79c565d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "reddit = praw.Reddit(\n",
    "    client_id=\"\",\n",
    "    client_secret=\"\",\n",
    "    password=\"\",\n",
    "    user_agent=\"\",\n",
    "    username=\"\",\n",
    ")\n",
    "\n",
    "target_sub = \"IndiaSocial\"\n",
    "subreddit = reddit.subreddit(target_sub)\n",
    "trigger_phrase = \"u/\"\n",
    "usernameRegex = re.compile(\"/u/[A-Za-z0-9_-]+\")\n",
    "MIN_COMMENTS = 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1de3d611",
   "metadata": {},
   "outputs": [],
   "source": [
    "for comment in subreddit.stream.comments(skip_existing=True):\n",
    "    if trigger_phrase in comment.body:\n",
    "        result = usernameRegex.search(comment.body)\n",
    "        print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f50015d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "api = PushshiftAPI(reddit)\n",
    "\n",
    "comments_generator = api.search_comments(after='7D', subreddit='indiasocial', limit=10) # Returns a generator object\n",
    "comment_list = list(comments_generator)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74b8a96c",
   "metadata": {},
   "outputs": [],
   "source": [
    "c = 0\n",
    "for commentID in comment_list:\n",
    "    ID = str(commentID)\n",
    "    commentID = reddit.comment(ID)\n",
    "    author = commentID.author\n",
    "    if str(author) == result:\n",
    "        c = c + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4f05aff",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73b612b0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
