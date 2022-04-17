from dotenv import load_dotenv
import tweepy
import os
import random
from rich.console import Console
from rich.table import Table
from datetime import datetime

load_dotenv()

consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

def clear():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

inputMessage = [
    "What are you gonna tweet today? ",
    "What is on your mind right now? ",
    "Why are you even tweeting? No one is gonna read your tweets anyway. ",
    "What's poppin? ",
    "What is on your mind? ",
    "TELL ME WHAT YOU ARE THINKING RIGHT NOW: "
]

clear()
print("---------------------------------------")
print("1. Tweet with no Media\n2. Reply to a message without media\n3. Exit")
print("---------------------------------------")
choiceInput = input("Choice: ")

if choiceInput == "1":
    clear()

    tweetMsg = input("{0}".format(random.choice(inputMessage)))

    tweepy.Client.create_tweet(client, text = tweetMsg)

    date = datetime.now()

    table = Table(title = "Tweet Information (https://twitter.com/{0})".format(tweepy.Client.get_me(client)[0]))

    table.add_column("Date and Time of Creation")
    table.add_column("Tweet Content")

    table.add_row("{0}".format(date.strftime("%Y-%m-%d %H:%M:%S")), tweetMsg)   

    console = Console()
    print("\n")
    console.print(table)
elif choiceInput == "2":
    clear()

    tweetID = input("Tweet ID: ")
    replyMsg = input("Reply message: ")

    tweepy.Client.create_tweet(client, in_reply_to_tweet_id = tweetID, text = replyMsg)

    date = datetime.now()

    table = Table(title = "Reply Information")

    table.add_column("Date and Time of Reply")
    table.add_column("Reply Content")

    table.add_row("{0}".format(date.strftime("%Y-%m-%d %H:%M:%S")), replyMsg)

    console = Console()
    print("\n")
    console.print(table)
elif choiceInput == "3": {
    quit()
}
else:
    clear()
    print("That's not a valid option. Run this program again.")