import praw
import pdb
import re
import os
import requests

reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('Coronavirus')
# Check each submission in the subreddit
for submission in subreddit.hot(limit=10):
    # Check each comment for each submission
    for comment in submission.comments:
        # If we haven't replied to this comment before
        if comment.id not in posts_replied_to:

            # Print the Bot Summary and Command List
            if re.search("CoverCovid !Help", comment.body, re.IGNORECASE):
                body = """
I am a bot for **CoverCovid-19** which tracks Covid-19 cases in the **United States**. I cover cases on both a local (self-reported) and county level (officially reported by the NYT). I can also provide links to the official [CoverCovid-19](https://covercovid-19.com) Covid-19 map.

---

**CoverCovid !Help** \- Prints the bot summary and command list

**CoverCovid !Total** \- Prints the current approximate total of cases in the US.

**CoverCovid !TopCounties** \- Prints the stats of the top 5 counties currently being impacted by Covid-19.  

**CoverCovid !Map** \- Provides a link to the CoverCovid-19 Covid Tracker map for viewing or self-reporting.  

**CoverCovid !County <County Name>, <State Name>** \- Provides a link to the CoverCovid-19 map centered on the provided county, if it exists. If the county does not exist, then it will provide a link to the map with its default view.  

**CoverCovid !StateMap** \- Provides a link to the official CDC map for US state Covid-19 stats.

---
Beep Boop, I am a Bot. 
Comment CoverCovid! Help for a list of my commands!
[Click here to send me feedback!](https://www.reddit.com/message/compose/?to=CoverCovid19)
                """
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Prints the current approximate total of cases in the US.
            if re.search("CoverCovid !Total", comment.body, re.IGNORECASE):
                resp = requests.get('https://covercovid-19.com/reports/official/total')
                totalCount = resp.text
                body = """The total number of cases in the United States currently is approximately  **> 6300000**. For more detailed information: visit [CoverCovid-19.com](https://covercovid-19.com/).
 
---
Beep Boop, I am a Bot. 
Comment CoverCovid! Help for a list of my commands!
[Click here to send me feedback!](https://www.reddit.com/message/compose/?to=CoverCovid19)
                """.format(totalCount)
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Prints the stats of the top 5 counties currently being impacted by Covid-19. 
            if re.search("CoverCovid !TopCounties", comment.body, re.IGNORECASE):
                resp = requests.get('https://covercovid-19.com/reports/counties/top')
                counties = resp.json()
                body = ""
                for i, county in enumerate(counties, start =1):
                    body +=  "\n" + str(i) + ". " + (county['name'] + ", " + county['state'] + ": **" + str(county['2wd']) + "**")
                body += """

---
Beep Boop, I am a Bot. 
Comment CoverCovid! Help for a list of my commands!
[Click here to send me feedback!](https://www.reddit.com/message/compose/?to=CoverCovid19)
                """
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Provides a link to the CoverCovid-19 Covid Tracker map for viewing or self-reporting. 
            if re.search("CoverCovid !Map", comment.body, re.IGNORECASE):
                body = "Click [here](https://covercovid-19.com/#map-anchor) to view an interactive map of US Covid-19 statistics or to report that you feel unwell and suspect having Covid-19."
                body += """

---
Beep Boop, I am a Bot. 
Comment CoverCovid! Help for a list of my commands!
[Click here to send me feedback!](https://www.reddit.com/message/compose/?to=CoverCovid19)
                """
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Provides a link to the CoverCovid-19 map centered on the provided county, if it exists. 
            # If the county does not exist, then it will provide a link to the map with its default view. 
            if re.search("CoverCovid !County [a-zA-Z]+, [a-zA-Z]+", comment.body, re.IGNORECASE):
                responseArr = comment.body.split("CoverCovid !County ")[1]
                data = responseArr.split(",")
                county = data[0]
                state = data[1].strip(" ")
                resp = requests.get('https://covercovid-19.com/reports/counties/{}/{}'.format(county, state))
                body = ""
                if resp is None:
                    body = "Uh-Oh, it looks like you might have mistyped the county name. Click [here](https://covercovid-19.com/#map-anchor) to view the whole interactive map of US Covid-19 statistics."
                else:
                    body = "Click [here](https://covercovid-19.com/?lat={}&lon={}) to find statistics about Covid-19 in {}, {} or to report that you feel unwell and suspect having Covid-19.".format(county, state, county, state)
                body += """

---
Beep Boop, I am a Bot. 
Comment CoverCovid! Help for a list of my commands!
[Click here to send me feedback!](https://www.reddit.com/message/compose/?to=CoverCovid19)
                """
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

            # Provides a link to the official CDC map for US state Covid-19 stats. 
            if re.search("CoverCovid !StateMap", comment.body, re.IGNORECASE):
                body = "Click [here](https://covercovid-19.com#map-cdc) to view an interactive map of US Covid-19 statistics by state."
                body += """

---
Beep Boop, I am a Bot. 
Comment CoverCovid! Help for a list of my commands!
[Click here to send me feedback!](https://www.reddit.com/message/compose/?to=CoverCovid19)
                """
                comment.reply(body)
                print("Bot replying to : ", comment.author)
                posts_replied_to.append(comment.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")