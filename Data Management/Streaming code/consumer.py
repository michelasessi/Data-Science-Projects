from kafka import KafkaConsumer
from pymongo import MongoClient
import time
import json


consumer = KafkaConsumer(bootstrap_servers='sandbox.hortonworks.com:6667',
								auto_offset_reset='earliest',					#togliere auto_offset_reset='earliest' se non si vogliono memorizzare dall'inizio tutti i dati in un topic
								consumer_timeout_ms=1000)
								
consumer.subscribe('<nome_topic>')


client = MongoClient()
db = client.<nome_DB>


while(True):
	for msgJ in consumer:
		tweet = json.loads(msgJ.value)
		row = { "Screen_name" : tweet[0] , 
                	"Nome" : tweet[1] , 
                        "Testo" : tweet[2] , 
                            "Followers" : tweet[3] ,
                                "Numero Retweet" : tweet[4] ,
                                    "Posizione" : tweet[5],
                                    	"Data" : tweet[6] }
		print (row)
		result = db.<nome_collection>.insert_one(row)
	time.sleep(5)

	