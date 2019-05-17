import postgresql as psql
from Connection import *

con = Connection('pq://ocatolicobot:Voljin!555@127.0.0.1/ocatolicobot')
cpf = '01211973360'
rs = con.consult("select nome from pessoa where cpf = '{0}'".format(cpf))
for linha in rs:
    print(linha[0])

con.closeConnection()