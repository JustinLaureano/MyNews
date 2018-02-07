import json
import praw
from pprint import pprint

reddit = praw.Reddit(client_id='WA6xYdJsSDwLLw',
                     client_secret='u6PQcqlR7YgBEQpnU4LwlZykL-U',
                     username='gravatron',
                     password='Steelers87',
                     user_agent='mynews')


news_list = []
unique_id = 1

for submission in reddit.subreddit('all').hot(limit=5):
    post_dict = {"model": "mynewsfeed.RedditPost", "pk": unique_id, "fields":
        {"title": submission.title, "url": submission.url, "comments":
            submission.shortlink, "subreddit": submission.subreddit.display_name}}

    unique_id += 1
    news_list.append(post_dict)

pprint(news_list)
with open('../../fixtures/reddit_all.json', 'w') as file:
    file.write(json.dumps(news_list))
