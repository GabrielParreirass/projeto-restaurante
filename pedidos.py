from PyQt5 import QtWidgets, uic
import mysql.connector

app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi('primeira_tela.ui')
pedidos = uic.loadUi('pedidos.ui')



banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="restaurante"
)

cursor = banco.cursor()

comando_SQL = 'INSERT INTO lista (pedido, horario, obs) VALUES (%s, %s, %s)'

comando2_SQL = 'SELECT * FROM lista'

cursor.execute(comando2_SQL)

infos = cursor.fetchall()

info = str(infos)

def verificar():
    try:
        pedido = primeira_tela.linePedido.text()
        hora = primeira_tela.lineHora.text()
        obs = primeira_tela.lineObs.text()
        dados = (pedido, hora, obs)
        cursor.execute(comando_SQL, dados)
        primeira_tela.linePedido.setText('')
        primeira_tela.lineHora.setText('')
        primeira_tela.lineObs.setText('')
        primeira_tela.labelAviso.setText('Pedido enviado com sucesso!')
    except:
        print('erro!')
        primeira_tela.labelAviso.setText('Falha ao enviar o pedido')



pedidos.textBrowser.setText(info)

primeira_tela.pushButton.clicked.connect(verificar)

primeira_tela.show()
pedidos.show()
app.exec()
