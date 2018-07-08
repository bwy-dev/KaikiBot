import praw
from cryptography.fernet import Fernet
from key_pathing import MasterKey as mk

key_init = mk.initializeMaster()

client_id_key = 'gAAAAABbQPVNnHVXERESzTJbP3JWWlpn-nDmV1-6nU8_VxpcPnZMG9BZgk8wewSB0oChULv3GqePOS3HUYLDimZOkBf_U3GKNA=='.encode()
client_secret_key = 'gAAAAABbQPVN57Bx3ZnwFrSZfbBdYv27cBw5aNvnYu8K0FgFrkX0LKYMomQE9lx1_-BTrFTtOpqZ1w050g4aYUCt70gWnr4sbCYxx4_55y0G0-bFvCQK00U='.encode()
username_key = 'gAAAAABbQhzAloDoCN5F4hfj72pxoyAYh3b3JB9W076Z2G4_iSAz3FhNYW3Eo5r9gu0dvboxQlGBgXEiID6KMaCXlUv-FSZ_VA=='.encode()
password_key = 'gAAAAABbQPVNRi88iJoa7GOk9Q7fV_NltZVxxks9Qp0uEimRJ8jFAOGYokIehwDmE_e6EY_yuNvhoBLDuVWVKXdaryXSB7g1Tw=='.encode()

decrypt_key = [client_id_key, client_secret_key, username_key, password_key]
decrypts = [''] *4 
lens = [0] *4
ends = [0] *4
for i in range(3):
	decrypts[i] = str(key_init.decrypt(decrypt_key[i]))
	lens[i] = len(decrypts[i])
	ends[i] = lens[i] - 1

r = praw.Reddit(client_id= decrypts[0][2:ends[0]],
				client_secret= decrypts[1][2:ends[1]],
				user_agent='KaikiBot',
				username= decrypts[2][2:ends[2]],
				password= decrypts[3][2:ends[3]])

user = r.redditor('KaikiBot')

print(user.comments.new())