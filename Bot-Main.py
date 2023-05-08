import praw
import random
import time

# read in quotes from file
file1 = open("FarnQuotes.txt", "r")
farnsworth_quotes = file1.readlines()


def main():

    # read credentials from file
    file = open("Bot")
    pw = file.readline().strip('\n')
    secret = file.readline()

    # instantiate reddit
    reddit = praw.Reddit(
        client_id="UiQWFajVtcRFM_4VxsSKoA",
        client_secret=secret,
        user_agent="<console:Farnsworth:1.0>",
        username="Prof-Farnsworth-bot",
        password=pw
    )

    # loop through submissions and parse
    subreddit = reddit.subreddit("futurama")
    for submission in subreddit.hot(limit=50):
        parse_submission(submission)


def parse_submission(submission):
    """Parses a submission in r/futurama and replies to any that contains professor
    or farnsworth with a random quote."""

    # loop through comments and check if comments contain professor
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if "farnsworth" in comment_lower or "professor" in comment_lower:

                # choose random quote and print replied to/reply
                print("---------")
                print("Replied to: ", comment.body)
                random_index = random.randint(0, len(farnsworth_quotes) - 1)
                print("Reply: ", farnsworth_quotes[random_index])
                comment.reply(farnsworth_quotes[random_index])
                time.sleep(2)


if __name__ == "__main__":
    main()
