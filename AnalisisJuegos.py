import tweepy 
import pandas as pd
import numpy as np

apiKey = "AmhDV5Rt39NnuMv8s849UDZU7"
apiSecretKey = "xcAne0MF7gn8DGON8zQQnkQdfLra54MjBGocLbbTinioEAd7zt" 

accessToken = "966168183794225152-THwvZuOKY86etOONbvvnbboZETvyE2E"
secretAccessToken = "HLD68hrW7pOcmmsCWd9EUr36lJwZmqXRhR08H5HPuhMdn"

autenticacion = tweepy.OAuthHandler( apiKey , apiSecretKey )
autenticacion.set_access_token( accessToken , secretAccessToken )


def post_a_DataFrame(tweets):
    
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=["Tweets"])
    
    df['id'] = np.array([tweet.id for tweet in tweets]) 
    df['date'] = np.array([tweet.created_at for tweet in tweets])
    df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
    df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
    
    return df
    
    

api = tweepy.API(autenticacion, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

starWars = post_a_DataFrame(api.user_timeline(screen_name = "EAStarWars", count=100))

starWarsFiltrado = starWars.loc[(starWars.Tweets.str[0] != '@') & (starWars['likes']>0)]

nfs = post_a_DataFrame(api.user_timeline(screen_name = "NeedforSpeed", count=100))

nfsFiltrado = nfs.loc[(nfs.Tweets.str[0] != '@') & (nfs['likes']>0)]

fifa = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSFIFA", count=100))

fifaFiltrado = fifa.loc[(fifa.Tweets.str[0] != '@') & (fifa['likes']>0)]

maden = post_a_DataFrame(api.user_timeline(screen_name = "EAMaddenNFL", count=100))

madenFiltrado = maden.loc[(maden.Tweets.str[0] != '@') & (maden['likes']>0)]

apex = post_a_DataFrame(api.user_timeline(screen_name = "PlayApex", count=100))

apexFiltrado = apex.loc[(apex.Tweets.str[0] != '@') & (apex['likes']>0)]

battle = post_a_DataFrame(api.user_timeline(screen_name = "Battlefield", count=100))

battleFiltrado = battle.loc[(battle.Tweets.str[0] != '@') & (battle['likes']>0)]

sims = post_a_DataFrame(api.user_timeline(screen_name = "TheSims", count=100))

simsFiltrado = sims.loc[(sims.Tweets.str[0] != '@') & (sims['likes']>0)]

nba = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSNBA", count=100))

nbaFiltrado = nba.loc[(nba.Tweets.str[0] != '@') & (nba['likes']>0)]











