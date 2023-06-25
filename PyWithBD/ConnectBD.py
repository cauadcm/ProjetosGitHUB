import mysql.connector

class ConnectBD:

    #FUNÇÃO PARA CONECTAR O BD COM O CÓDIGO
    def conectar(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456789caua',
            port='3306',
            database='pythontest'
        )

    #PEGANDO O CURSOR PARA REFERENCIAR NO CODIGO
    def get_cursor(self):
        return self.mydb.cursor()