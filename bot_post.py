import praw
import pdb
import re
import os
import requests

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
subreddit = reddit.subreddit('pythonforengineers')
# Check each submission in the subreddit
for submission in subreddit.hot(limit=10):
    # Check each comment for each submission
    for comment in submission.comments:
        # If we haven't replied to this comment before
        if comment.id not in posts_replied_to:

            # Test
            # Do a case insensitive search
            '''
            if re.search("i love python", comment.body, re.IGNORECASE):
                # Reply to the post
                comment.reply("Nigerian scammer bot says: It's all about the Bass (and Python)")
                print("Bot replying to : ", comment.author)

                # Store the current id into our list
                posts_replied_to.append(comment.id)
            '''

            # Print the Bot Summary and Command List
            if re.search("CoverCovid !Help", comment.body, re.IGNORECASE):
                body = '''
                I am a bot for **CoverCovid-19** which tracks Covid-19 cases in the **United States**. I cover cases on both a local (self-reported) and county level (officially reported). I can also provide links to the official CoverCovid-19 Covid-19 map.  
      
                ---
                **CoverCovid !Help** - Prints the bot summary and command list
                **CoverCovid !Total** - Prints the current approximate total of cases in the US.
                **CoverCovid !TopCounties** - Prints the stats of the top 5 counties currently being impacted by Covid-19.
                **CoverCovid !Map** - Provides a link to the CoverCovid-19 Covid Tracker map for viewing or self-reporting.
                **CoverCovid !Map CountyName** - Provides a link to the CoverCovid-19 map centered on the provided county, if it exists. If the county does not exist, then it will provide a link to the map with its default view.
                **CoverCovid !StateMap** - Provides a link to the official CDC map for US state Covid-19 stats.
                '''
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Prints the current approximate total of cases in the US.
            if re.search("CoverCovid !Total", comment.body, re.IGNORECASE):
                resp = requests.get('https://covercovid-19.com/reports/official/total')
                totalCount = resp.text
                body = "The total number of cases in the United States currently is approximately  **{}**. For more detailed information: visit [CoverCovid-19.com](https://covercovid-19.com/).".format(totalCount)
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Prints the stats of the top 5 counties currently being impacted by Covid-19. 
            if re.search("CoverCovid !TopCounties", comment.body, re.IGNORECASE):
                resp = requests.get('https://covercovid-19.com/reports/counties/top')
                comment.reply("")
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Provides a link to the CoverCovid-19 Covid Tracker map for viewing or self-reporting. 
            if re.search("CoverCovid !Map", comment.body, re.IGNORECASE):
                comment.reply("Click [here](https://covercovid-19.com) to view an interactive map of US Covid-19 statistics or to report that you feel unwell and suspect having Covid-19.")
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Provides a link to the CoverCovid-19 map centered on the provided county, if it exists. 
            # If the county does not exist, then it will provide a link to the map with its default view. 
            if re.search("CoverCovid !Map <County>", comment.body, re.IGNORECASE):
                resp = requests.get('https://covercovid-19.com/reports/counties/<County>')
                comment.reply("Click here to find statistics about Covid-19 in <County> or to report that you feel unwell and suspect having Covid-19.")
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Provides a link to the official CDC map for US state Covid-19 stats. 
            if re.search("CoverCovid !StateMap", comment.body, re.IGNORECASE):
                comment.reply("Click [here](https://covercovid-19.com#map-cdc) to view an interactive map of US Covid-19 statistics by state.")
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")