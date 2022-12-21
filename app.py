from flask import Flask,jsonify
app = Flask(__name__)
import requests
import random
import sqlite3
import datetime

# coding: utf-8




@app.route('/')
def hello_world():
   return "Hello, World!"

@app.route('/temp')
def temp():
   
   api_result = requests.get('http://api.weatherunlocked.com/api/current/-33.456,-70.648?app_id=210dc524&app_key=a1277856144d5af27e35db0afb5744e5')
   api_response = api_result.json()
   return jsonify(api_response['temp_c'])

@app.route('/uf')
def uf():
   x = datetime.datetime.now()
   hoy=str(x.year)+'-'+str(x.month)+'-'+str(x.day)
   con = sqlite3.connect("database/ufs")
   cursor=con.cursor()
   sql="SELECT * FROM uf WHERE fecha='%s';"%hoy
   res = cursor.execute(sql)
   ret=res.fetchone()
   
   return jsonify(ret)


   '''api_result = requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=edcc2fc99d53308cdf27920f9c94210dfa1968a7&formato=json')
   api_response = api_result.json()
   return jsonify(api_response['UFs'])'''

@app.route('/dolares')
def dolar():
   api_result = requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar?apikey=edcc2fc99d53308cdf27920f9c94210dfa1968a7&formato=json')
   api_response = api_result.json()
   return jsonify(api_response['Dolares'])


@app.route('/cru')
def crucigrama():
   comienza = random.randint(0, 2231)
   return jsonify("https://www.epasatiempos.es/crucigramas.php?cg=%s"%comienza)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)







   