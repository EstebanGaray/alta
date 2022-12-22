import sqlite3
import requests
#create table
con = sqlite3.connect("ufs")
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS uf (valor varchar(10),fecha VARCHAR(10));")

#obhtener dato
api_result = requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=edcc2fc99d53308cdf27920f9c94210dfa1968a7&formato=json')
api_response = api_result.json()
uf=api_response['UFs'][0]["Valor"]
day=api_response['UFs'][0]["Fecha"]

#cargar dato
con = sqlite3.connect("database/ufs")
sql="INSERT INTO uf VALUES('%s','%s');"%(uf,day)
cursor=con.cursor()
cursor.execute(sql)
con.commit()

print('archivo subido con exito')
