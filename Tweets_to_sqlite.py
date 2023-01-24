import tweepy as tw
import sqlite3


#Developer platform twiiter: https://developer.twitter.com/
consumer_key = ""
consumer_secret  = ""
bearer_token = ""
access_token = ""
access_token_secret = ""


#conexão com  banco de dados
bd = sqlite3.connect('BD_python.db')
cursor = bd.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS tweets (texto TEXT, rt TEXT)')

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


for i in dados:
    texto = i.text
    #verifica se é um tweet ou um rtweet
    if (texto[:2] == "RT"):
        rt = "SIM" 
    else:
        rt = "NÂO"
    #insere os valores no banco de dados
    cursor.execute( "INSERT INTO tweets(texto, rt) VALUES (?, ?)", (texto,rt))
    

bd.commit()
bd.close()