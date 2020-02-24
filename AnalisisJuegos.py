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

promediosLikes=[]
promediosRet=[]
labels = 'Stars Wars','Need for speed','Fifa','Madden','Apex legends','Battlefield','The Sims','NBA' 

def post_a_DataFrame(tweets):
    
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=["Tweets"])
    
    df['fecha'] = np.array([tweet.created_at for tweet in tweets])
    df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
    df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
    
    return df
    
api = tweepy.API(autenticacion, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

starWars = post_a_DataFrame(api.user_timeline(screen_name = "EAStarWars", count=150))
starWarsFiltrado = starWars.loc[(starWars.Tweets.str[0] != '@') & (starWars['likes']>0)]

likesStars = pd.Series(data=starWarsFiltrado['likes'].values, index=starWarsFiltrado['fecha'])
likesStars.plot(figsize=(10, 4), color = 'b', legend = True, label='likes' )
starsRet = pd.Series(data=starWarsFiltrado['retweets'].values, index=starWarsFiltrado['fecha'])
starsRet.plot(figsize=(10, 4), color = 'r', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Juegos de Star Wars)")
plt.show()

promediosLikes.append(int(st.mean(starWarsFiltrado['likes'])))
print('El promedio likes de los juegos de starwars es: ' + str(promediosLikes[0]) + ' likes')
promediosRet.append(int(st.mean(starWarsFiltrado['retweets'])))
print('El promedio retweets de los juegos de starwars es: ' + str(promediosRet[0]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(starWarsFiltrado['likes'],starWarsFiltrado['retweets'])[0][1]))

plt.plot(starWarsFiltrado['likes'],starWarsFiltrado['retweets'], 'bo')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



nfs = post_a_DataFrame(api.user_timeline(screen_name = "NeedforSpeed", count=150))
nfsFiltrado = nfs.loc[(nfs.Tweets.str[0] != '@') & (nfs['likes']>0)]

likesNfs = pd.Series(data=nfsFiltrado['likes'].values, index=nfsFiltrado['fecha'])
likesNfs.plot(figsize=(10, 4), color = 'g',legend = True, label='likes' )
nfsRet = pd.Series(data=nfsFiltrado['retweets'].values, index=nfsFiltrado['fecha'])
nfsRet.plot(figsize=(10, 4), color = 'b', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Juegos de Need for speed)")
plt.show()

promediosLikes.append(int(st.mean(nfsFiltrado['likes'])))
print('El promedio likes de los juegos de need for speed es: ' + str(promediosLikes[1])+ ' likes')
promediosRet.append(int(st.mean(nfsFiltrado['retweets'])))
print('El promedio retweets de los juegos de Need for speed es: ' + str(promediosRet[1]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(nfsFiltrado['likes'],nfsFiltrado['retweets'])[0][1]))

plt.plot(nfsFiltrado['likes'],nfsFiltrado['retweets'], 'go')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



fifa = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSFIFA", count=150))
fifaFiltrado = fifa.loc[(fifa.Tweets.str[0] != '@') & (fifa['likes']>0)]

likesFifa = pd.Series(data=fifaFiltrado['likes'].values, index=fifaFiltrado['fecha'])
likesFifa.plot(figsize=(10, 4), color = 'r', legend = True, label='likes' )
fifRet = pd.Series(data=fifaFiltrado['retweets'].values, index=fifaFiltrado['fecha'])
fifRet.plot(figsize=(10, 4), color = 'c', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Juegos de Fifa)")
plt.show()

promediosLikes.append(int(st.mean(fifaFiltrado['likes'])))
print('El promedio likes de los juegos de fifa es: ' + str(promediosLikes[2])+ ' likes')
promediosRet.append(int(st.mean(fifaFiltrado['retweets'])))
print('El promedio retweets de los juegos de Fifa es: ' + str(promediosRet[2]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(fifaFiltrado['likes'],fifaFiltrado['retweets'])[0][1]))

plt.plot(fifaFiltrado['likes'],fifaFiltrado['retweets'], 'ro')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



maden = post_a_DataFrame(api.user_timeline(screen_name = "EAMaddenNFL", count=150))
madenFiltrado = maden.loc[(maden.Tweets.str[0] != '@') & (maden['likes']>0)]

likesMaden = pd.Series(data=madenFiltrado['likes'].values, index=madenFiltrado['fecha'])
likesMaden.plot(figsize=(10, 4), color = 'c', legend = True, label='likes' )
madRet = pd.Series(data=madenFiltrado['retweets'].values, index=madenFiltrado['fecha'])
madRet.plot(figsize=(10, 4), color = 'g', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Juegos de Madden NFL)")
plt.show()

promediosLikes.append(int(st.mean(madenFiltrado['likes'])))
print('El promedio likes de los juegos de madden es: ' + str(promediosLikes[3])+ ' likes')
promediosRet.append(int(st.mean(madenFiltrado['retweets'])))
print('El promedio retweets de los juegos de Madden es: ' + str(promediosRet[3]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(madenFiltrado['likes'],madenFiltrado['retweets'])[0][1]))

plt.plot(madenFiltrado['likes'],madenFiltrado['retweets'], 'co')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



apex = post_a_DataFrame(api.user_timeline(screen_name = "PlayApex", count=150))
apexFiltrado = apex.loc[(apex.Tweets.str[0] != '@') & (apex['likes']>0)]

likesApex = pd.Series(data=apexFiltrado['likes'].values, index=apexFiltrado['fecha'])
likesApex.plot(figsize=(10, 4), color = 'm', legend = True, label='likes' )
apRet = pd.Series(data=apexFiltrado['retweets'].values, index=apexFiltrado['fecha'])
apRet.plot(figsize=(10, 4), color = 'y', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Apex Legends)")
plt.show()

promediosLikes.append(int(st.mean(apexFiltrado['likes'])))
print('El promedio likes de apex es: ' + str(promediosLikes[4])+ ' likes')
promediosRet.append(int(st.mean(apexFiltrado['retweets'])))
print('El promedio retweets de apex: ' + str(promediosRet[4]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(apexFiltrado['likes'],apexFiltrado['retweets'])[0][1]))

plt.plot(apexFiltrado['likes'],apexFiltrado['retweets'], 'mo')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



battle = post_a_DataFrame(api.user_timeline(screen_name = "Battlefield", count=150))
battleFiltrado = battle.loc[(battle.Tweets.str[0] != '@') & (battle['likes']>0)]

likesBattle = pd.Series(data=battleFiltrado['likes'].values, index=battleFiltrado['fecha'])
likesBattle.plot(figsize=(10, 4), color = 'y', legend = True, label='likes' )
batRet = pd.Series(data=battleFiltrado['retweets'].values, index=battleFiltrado['fecha'])
batRet.plot(figsize=(10, 4), color = 'g', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Juegos de Battlefield)")
plt.show()

promediosLikes.append(int(st.mean(battleFiltrado['likes'])))
print('El promedio likes de los juegos de Battlefield es: ' + str(promediosLikes[5])+ ' likes')
promediosRet.append(int(st.mean(battleFiltrado['retweets'])))
print('El promedio retweets de los juegos de Battlefield: ' + str(promediosRet[5]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(battleFiltrado['likes'],battleFiltrado['retweets'])[0][1]))

plt.plot(battleFiltrado['likes'],battleFiltrado['retweets'], 'yo')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



sims = post_a_DataFrame(api.user_timeline(screen_name = "TheSims", count=150))
simsFiltrado = sims.loc[(sims.Tweets.str[0] != '@') & (sims['likes']>0)]

likesSims = pd.Series(data=simsFiltrado['likes'].values, index=simsFiltrado['fecha'])
likesSims.plot(figsize=(10, 4), color = 'k', legend = True, label='likes' )
simRet = pd.Series(data=simsFiltrado['retweets'].values, index=simsFiltrado['fecha'])
simRet.plot(figsize=(10, 4), color = 'b', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Juegos los Sims)")
plt.show()

promediosLikes.append(int(st.mean(simsFiltrado['likes'])))
print('El promedio likes de los juegos de The sims es: ' + str(promediosLikes[6])+ ' likes')
promediosRet.append(int(st.mean(simsFiltrado['retweets'])))
print('El promedio retweets de los juegos de The sims: ' + str(promediosRet[6]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(simsFiltrado['likes'],simsFiltrado['retweets'])[0][1]))

plt.plot(simsFiltrado['likes'],simsFiltrado['retweets'], 'ko')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



nba = post_a_DataFrame(api.user_timeline(screen_name = "EASPORTSNBA", count=150))
nbaFiltrado = nba.loc[(nba.Tweets.str[0] != '@') & (nba['likes']>0)]

likesNba = pd.Series(data=nbaFiltrado['likes'].values, index=nbaFiltrado['fecha'])
likesNba.plot(figsize=(10, 4), color = 'r', legend = True, label='likes' )
nbaRet = pd.Series(data=nbaFiltrado['retweets'].values, index=nbaFiltrado['fecha'])
nbaRet.plot(figsize=(10, 4), color = 'g', legend = True, label='retweets' )
plt.title("(Likes, Retweets) vs Fecha (Juegos de Nba)")
plt.show()

promediosLikes.append(int(st.mean(nbaFiltrado['likes'])))
print('El promedio likes de los juegos Nba es: ' + str(promediosLikes[7])+ ' likes')
promediosRet.append(int(st.mean(nbaFiltrado['retweets'])))
print('El promedio retweets de los juegos de Nba: ' + str(promediosRet[7]) + ' retweets')
print('La correlacion entre sus retweets y likes es: ' + str(np.corrcoef(nbaFiltrado['likes'],nbaFiltrado['retweets'])[0][1]))

plt.plot(nbaFiltrado['likes'],nbaFiltrado['retweets'], 'ro')
plt.title('correlacion entre sus retweets y likes')
plt.xlabel('Likes')
plt.ylabel('Retweets')
plt.show()



print()

print('Grafica de pastel con los promedios de likes de cada juego es:')

fig1, ax1 = plt.subplots()
ax1.pie(promediosLikes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()

print()

print('Grafica de pastel con los promedios de retweets de cada juego es:')

fig2, ax2 = plt.subplots()
ax2.pie(promediosRet, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax2.axis('equal') 
plt.show()