import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("Covid")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("id: ", submission.id)
    print("Number of Comments: ", submission.num_comments)
    for comment in submission.comments:
        print(comment.id)
    print("---------------------------------\n")