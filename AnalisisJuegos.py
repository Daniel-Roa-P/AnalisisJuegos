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

promedios=[]
labels = 'Stars Wars','Need for speed','Fifa','Madden','ApeX legends','Battlefield','The Sims','NBA' 

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

promedios.append(int(st.mean(starWarsFiltrado['likes'])))
print('El promedio likes de los juegos de starwars es: ' + str(promedios[0]) + ' likes')


nfs = post_a_DataFrame(api.user_timeline(screen_name = "NeedforSpeed", count=150))
nfsFiltrado = nfs.loc[(nfs.Tweets.str[0] != '@') & (nfs['likes']>0)]

likesNfs = pd.Series(data=nfsFiltrado['likes'].values, index=nfsFiltrado['fecha'])
likesNfs.plot(figsize=(10, 4), color = 'g' )
plt.title("Likes vs Fecha (Juegos de Need for speed)")
plt.show()

promedios.append(int(st.mean(nfsFiltrado['likes'])))
print('El promedio likes de los juegos de need for speed es: ' + str(promedios[1])+ ' likes')


fifa = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSFIFA", count=150))
fifaFiltrado = fifa.loc[(fifa.Tweets.str[0] != '@') & (fifa['likes']>0)]

likesFifa = pd.Series(data=fifaFiltrado['likes'].values, index=fifaFiltrado['fecha'])
likesFifa.plot(figsize=(10, 4), color = 'r' )
plt.title("Likes vs Fecha (Juegos de Fifa)")
plt.show()

promedios.append(int(st.mean(fifaFiltrado['likes'])))
print('El promedio likes de los juegos de fifa es: ' + str(promedios[2])+ ' likes')


maden = post_a_DataFrame(api.user_timeline(screen_name = "EAMaddenNFL", count=150))
madenFiltrado = maden.loc[(maden.Tweets.str[0] != '@') & (maden['likes']>0)]

likesMaden = pd.Series(data=madenFiltrado['likes'].values, index=madenFiltrado['fecha'])
likesMaden.plot(figsize=(10, 4), color = 'c' )
plt.title("Likes vs Fecha (Juegos de Madden NFL)")
plt.show()

promedios.append(int(st.mean(madenFiltrado['likes'])))
print('El promedio likes de los juegos de madden es: ' + str(promedios[3])+ ' likes')


apex = post_a_DataFrame(api.user_timeline(screen_name = "PlayApex", count=150))
apexFiltrado = apex.loc[(apex.Tweets.str[0] != '@') & (apex['likes']>0)]

likesApex = pd.Series(data=apexFiltrado['likes'].values, index=apexFiltrado['fecha'])
likesApex.plot(figsize=(10, 4), color = 'm' )
plt.title("Likes vs Fecha (Apex Legends)")
plt.show()

promedios.append(int(st.mean(apexFiltrado['likes'])))
print('El promedio likes de apex es:' + str(promedios[4])+ ' likes')


battle = post_a_DataFrame(api.user_timeline(screen_name = "Battlefield", count=150))
battleFiltrado = battle.loc[(battle.Tweets.str[0] != '@') & (battle['likes']>0)]

likesBattle = pd.Series(data=battleFiltrado['likes'].values, index=battleFiltrado['fecha'])
likesBattle.plot(figsize=(10, 4), color = 'y' )
plt.title("Likes vs Fecha (Juegos de Battlefield)")
plt.show()

promedios.append(int(st.mean(battleFiltrado['likes'])))
print('El promedio likes de los juegos de Battlefield es:' + str(promedios[5])+ ' likes')


sims = post_a_DataFrame(api.user_timeline(screen_name = "TheSims", count=150))
simsFiltrado = sims.loc[(sims.Tweets.str[0] != '@') & (sims['likes']>0)]

likesSims = pd.Series(data=simsFiltrado['likes'].values, index=simsFiltrado['fecha'])
likesSims.plot(figsize=(10, 4), color = 'k' )
plt.title("Likes vs Fecha (Juegos los Sims)")
plt.show()

promedios.append(int(st.mean(simsFiltrado['likes'])))
print('El promedio likes de los juegos de The sims es: ' + str(promedios[6])+ ' likes')


nba = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSNBA", count=150))
nbaFiltrado = nba.loc[(nba.Tweets.str[0] != '@') & (nba['likes']>0)]

likesNba = pd.Series(data=nbaFiltrado['likes'].values, index=nbaFiltrado['fecha'])
likesNba.plot(figsize=(10, 4), color = 'r' )
plt.title("Likes vs Fecha (Juegos de Nba)")
plt.show()

promedios.append(int(st.mean(nbaFiltrado['likes'])))
print('El promedio likes de los juegos Nba es: ' + str(promedios[7])+ ' likes')

print('Grafica de pastel con los promedios de likes de cada juego es:')

fig1, ax1 = plt.subplots()
ax1.pie(promedios, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()