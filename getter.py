import auth
import tweepy
import urllib.request
import os
import sys

credFile = "creds/key"
photo_dir = "photo"
output_file_prefix = "Yuzu"

def getImageFromTweets(tweets):

	for tweet in tweets:
	    
	    for media in tweet.entities.get("media",[{}]):
	    
	    	if media.get("type", None) == "photo":
	        
	        	file_name = media["media_url"].split("/")[-1]
	        	urllib.request.urlretrieve(media["media_url"], photo_dir + "/" + file_name)

def renameFiles():

	for count, filename in enumerate(os.listdir(photo_dir)):

		os.rename(photo_dir + "/" + filename, photo_dir + "/" + output_file_prefix + "_" + str(count) + "." + filename.split(".")[-1])


def main():
    
	api = auth.getAPIWithLogin(credFile)

	search = tweepy.Cursor(api.search,
	                       q="yuzuru hanyu",
	                       lang="en",                    
	                       result_type="recent").items(100)

	getImageFromTweets(search)

	search = tweepy.Cursor(api.search,
	                       q="羽生結弦",
	                       lang="ja",                    
	                       result_type="recent").items(100)

	getImageFromTweets(search)

	renameFiles()


if __name__ == "__main__":
    main()
