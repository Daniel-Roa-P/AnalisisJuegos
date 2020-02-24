import tweepy 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statistics as st

apiKey = "AmhDV5Rt39NnuMv8s849UDZU7"
apiSecretKey = "xcAne0MF7gn8DGON8zQQnkQdfLra54MjBGocLbbTinioEAd7zt" 

accessToken = "966168183794225152-THwvZuOKY86etOONbvvnbboZETvyE2E"
secretAccessToken = "HLD68hrW7pOcmmsCWd9EUr36lJwZmqXRhR08H5HPuhMdn"

autenticacion = tweepy.OAuthHandler( apiKey , apiSecretKey )
autenticacion.set_access_token( accessToken , secretAccessToken )


def post_a_DataFrame(tweets):
    
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=["Tweets"])
    
    df['id'] = np.array([tweet.id for tweet in tweets]) 
    df['fecha'] = np.array([tweet.created_at for tweet in tweets])
    df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
    df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
    
    return df
    
    

api = tweepy.API(autenticacion, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

starWars = post_a_DataFrame(api.user_timeline(screen_name = "EAStarWars", count=150))
starWarsFiltrado = starWars.loc[(starWars.Tweets.str[0] != '@') & (starWars['likes']>0)]

likesStars = pd.Series(data=starWarsFiltrado['likes'].values, index=starWarsFiltrado['fecha'])
likesStars.plot(figsize=(10, 4), color = 'b' )
plt.title("Likes vs Fecha (Juegos de Star Wars)")
plt.show()

print('El promedio likes de los juegos de starwars: ' + str(st.mean(starWarsFiltrado['likes'])))


nfs = post_a_DataFrame(api.user_timeline(screen_name = "NeedforSpeed", count=150))
nfsFiltrado = nfs.loc[(nfs.Tweets.str[0] != '@') & (nfs['likes']>0)]

likesNfs = pd.Series(data=nfsFiltrado['likes'].values, index=nfsFiltrado['fecha'])
likesNfs.plot(figsize=(10, 4), color = 'g' )
plt.title("Likes vs Fecha (Juegos de Need for speed)")
plt.show()

print('El promedio likes de los juegos de need for speed: ' + str(st.mean(nfsFiltrado['likes'])))


fifa = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSFIFA", count=150))
fifaFiltrado = fifa.loc[(fifa.Tweets.str[0] != '@') & (fifa['likes']>0)]

likesFifa = pd.Series(data=fifaFiltrado['likes'].values, index=fifaFiltrado['fecha'])
likesFifa.plot(figsize=(10, 4), color = 'r' )
plt.title("Likes vs Fecha (Juegos de Fifa)")
plt.show()

print('El promedio likes de los juegos de fifa: ' + str(st.mean(fifaFiltrado['likes'])))


maden = post_a_DataFrame(api.user_timeline(screen_name = "EAMaddenNFL", count=150))
madenFiltrado = maden.loc[(maden.Tweets.str[0] != '@') & (maden['likes']>0)]

likesMaden = pd.Series(data=madenFiltrado['likes'].values, index=madenFiltrado['fecha'])
likesMaden.plot(figsize=(10, 4), color = 'c' )
plt.title("Likes vs Fecha (Juegos de Madden NFL)")
plt.show()

print('El promedio likes de los juegos de madden: ' + str(st.mean(madenFiltrado['likes'])))


apex = post_a_DataFrame(api.user_timeline(screen_name = "PlayApex", count=150))
apexFiltrado = apex.loc[(apex.Tweets.str[0] != '@') & (apex['likes']>0)]

likesApex = pd.Series(data=apexFiltrado['likes'].values, index=apexFiltrado['fecha'])
likesApex.plot(figsize=(10, 4), color = 'm' )
plt.title("Likes vs Fecha (Apex Legends)")
plt.show()

print('El promedio likes de apex ' + str(st.mean(apexFiltrado['likes'])))


battle = post_a_DataFrame(api.user_timeline(screen_name = "Battlefield", count=150))
battleFiltrado = battle.loc[(battle.Tweets.str[0] != '@') & (battle['likes']>0)]

likesBattle = pd.Series(data=battleFiltrado['likes'].values, index=battleFiltrado['fecha'])
likesBattle.plot(figsize=(10, 4), color = 'y' )
plt.title("Likes vs Fecha (Juegos de Battlefield)")
plt.show()

print('El promedio likes de los juegos de Battlefield ' + str(st.mean(battleFiltrado['likes'])))


sims = post_a_DataFrame(api.user_timeline(screen_name = "TheSims", count=150))
simsFiltrado = sims.loc[(sims.Tweets.str[0] != '@') & (sims['likes']>0)]

likesSims = pd.Series(data=simsFiltrado['likes'].values, index=simsFiltrado['fecha'])
likesSims.plot(figsize=(10, 4), color = 'k' )
plt.title("Likes vs Fecha (Juegos los Sims)")
plt.show()

print('El promedio likes de los juegos de The sims ' + str(st.mean(simsFiltrado['likes'])))


nba = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSNBA", count=150))
nbaFiltrado = nba.loc[(nba.Tweets.str[0] != '@') & (nba['likes']>0)]

likesNba = pd.Series(data=nbaFiltrado['likes'].values, index=nbaFiltrado['fecha'])
likesNba.plot(figsize=(10, 4), color = 'r' )
plt.title("Likes vs Fecha (Juegos de Nba)")
plt.show()

print('El promedio likes de los juegos Nba ' + str(st.mean(nbaFiltrado['likes'])))


