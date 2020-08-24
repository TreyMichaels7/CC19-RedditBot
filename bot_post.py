import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

## reddit.login("CoverCovid", "Tyxc0614")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('Coronavirus')
for submission in subreddit.hot(limit=10):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Test
        # Do a case insensitive search
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

        # Print the Bot Summary and Command List
        if re.search("CoverCovid !Help", submission.title, re.IGNORECASE):
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

        # Prints the current approximate total of cases in the US.
        if re.search("CoverCovid !Total", submission.title, re.IGNORECASE):
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

        # Prints the stats of the top 5 counties currently being impacted by Covid-19. 
        if re.search("CoverCovid !TopCounties", submission.title, re.IGNORECASE):
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

        # Provides a link to the CoverCovid-19 Covid Tracker map for viewing or self-reporting. 
        if re.search("CoverCovid !Map", submission.title, re.IGNORECASE):
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

        # Provides a link to the CoverCovid-19 map centered on the provided county, if it exists. 
        # If the county does not exist, then it will provide a link to the map with its default view. 
        if re.search("CoverCovid !Map <County>", submission.title, re.IGNORECASE):
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

        # Provides a link to the official CDC map for US state Covid-19 stats. 
        if re.search("CoverCovid !StateMap", submission.title, re.IGNORECASE):
            submission.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

        

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")