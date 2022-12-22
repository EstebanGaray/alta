from flask import Flask,jsonify
app = Flask(__name__)
import requests
import random
#import sqlite3
import datetime
import pytz
import pgdb
# coding: utf-8
db_host = "postgres-service.default.svc.cluster.local"
db_name='postgresdb'
db_user='postgres'
db_password='postgres'




@app.route('/')
def hello_world():
   return "Hello, World!"

@app.route('/temp')
def temp():
   params={
      'access_key': "996be65dbbfdaa87d732990d2d1b15f0",
      'query': 'Santiago Chile'
   }
   api_result = requests.get('http://api.weatherstack.com/current', params)
   api_response = api_result.json()
   #print(api_response["current"]["temperature"])
   return jsonify(temperatura=api_response["current"]["temperature"])

@app.route('/uf')
def uf():
   x = datetime.datetime.now(pytz.timezone('America/Santiago'))
   hoy=str(x.year)+'-'+str(x.month)+'-'+str(x.day)
   con = pgdb.connect(host=db_host,database=db_name,user=db_user,password=db_password)
   cursor=con.cursor()
   #sql="SELECT * FROM uf WHERE fecha='%s';"%hoy
   sql='SELECT * from uf'
   res = cursor.execute(sql)
   ret=res.fetchone()
   print(ret)
   return jsonify(valor=ret[1],fecha=ret[2])
   
   


   '''api_result = requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=edcc2fc99d53308cdf27920f9c94210dfa1968a7&formato=json')
   api_response = api_result.json()
   return jsonify(api_response['UFs'])'''

@app.route('/dolares')
def dolar():
   api_result = requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar?apikey=edcc2fc99d53308cdf27920f9c94210dfa1968a7&formato=json')
   api_response = api_result.json()
   return jsonify(api_response['Dolares'][0])


@app.route('/cru')
def crucigrama():
   comienza = random.randint(0, 2231)
   return jsonify(url="https://www.epasatiempos.es/crucigramas.php?cg=%s"%comienza)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)







   