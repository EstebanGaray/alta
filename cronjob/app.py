import pg
import requests
db_host = 'postgres-service.default.svc.cluster.local'
db_name='postgresdb'
db_user='postgres'
db_password='postgres'
api_result = requests.get('https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=edcc2fc99d53308cdf27920f9c94210dfa1968a7&formato=json')
api_response = api_result.json()
uf=api_response['UFs'][0]["Valor"]
day=api_response['UFs'][0]["Fecha"]
con = pg.connect(host=db_host,dbname=db_name,user=db_user,passwd=db_password)
sql="CREATE TABLE IF NOT EXISTS uf(id serial primary key, valor varchar(10),fecha varchar(10));"
print('table create')
con.query(sql)
sql="INSERT INTO uf(valor,fecha) VALUES('%s','%s');"%(uf,day)
print('valor agregado')
con.query(sql)
print(uf,day)