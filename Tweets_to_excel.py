import tweepy as tw
import pandas as pd


#Developer platform twiiter: https://developer.twitter.com/
consumer_key = ""
consumer_secret  = ""
bearer_token = ""
access_token = ""
access_token_secret = ""

#criando cliente
client = tw.Client(bearer_token,consumer_key,consumer_secret,access_token,access_token_secret)

#inicio e fim das pesquisas, data e horário
start =""
end = ""
#palavra que vai ser pesquisada
keyword = ""

#pesquisa  os 100 tweets recentes com o assunto da query
searchs = client.search_recent_tweets(query=keyword,max_results=100,start_time=start,end_time=end)
dados = searchs.data

#cria um dataframe vazio
df = pd.DataFrame(columns = ['Texto_twitter','RT'])

for i in dados:
    texto = i.text
    #verifica se é um tweet ou um rtweet
    if (texto[:2] == "RT"):
        rt = "SIM" 
    else:
        rt = "NÂO"
    
    df.loc[(len(df))] = texto,rt


df.to_excel("resultados.xlsx")