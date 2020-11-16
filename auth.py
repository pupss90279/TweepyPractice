import tweepy

# fetch API key and secret from credFileName
# file in format:
# API key:###
# API secret key:###
def getAPIKeyAndSecretFromFile(credFileName):
	
	with open(credFileName, "r") as creds:

		APIKey = creds.readline().split(":")[1].strip()
		APISecret = creds.readline().split(":")[1].strip()
		accessToken = creds.readline().split(":")[1].strip()
		accessTokenSecret = creds.readline().split(":")[1].strip()

	return APIKey, APISecret, accessToken, accessTokenSecret


def getAPI(credFileName):
	
	APIKey, APISecret, _ = getAPIKeyAndSecretFromFile(credFileName)
	auth = tweepy.AppAuthHandler(APIKey, APISecret)
	return tweepy.API(auth)

def getAPIWithLogin(credFileName):

	APIKey, APISecret, accessToken, accessTokenSecret = getAPIKeyAndSecretFromFile(credFileName)

	auth = tweepy.OAuthHandler(APIKey, APISecret)
	auth.set_access_token(accessToken, accessTokenSecret)
	return tweepy.API(auth)