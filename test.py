import tweepy
import mysql.connector
consumer_key = 'Yu6yUQXoYdHND2tFs4zjyPiR7'
consumer_secret = 'cFKf6UaPNoPFNvJPoJjJhUHE629uPqJfzXJ6lycotjTBsQI0s3'
access_token = '373411090-xNmx3gEK3MLM9cminHnqDk1j6pCh1j8Rki5Gsfdw'
access_token_secret = 'BNtrExisb5PGXdeA6drLfHjS79OQg4IHidVcogTOQHbxU'
try:
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
except tweepy.TweepError:
	print ('Error! Failed to get request token.') 
cnx = mysql.connector.connect(user='root', password='rushal1', database='traffic')
cursor = cnx.cursor()
query = ("SELECT * FROM temp")
cursor.execute(query)
for (a, b) in cursor:
	api.update_status('@DelhiTrafficPol'+' #'+a+' '+b)
cursor.close()
cnx.close()
