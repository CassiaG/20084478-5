from PyQt5 import uic, QtWidgets
import sqlite3
import pyautogui
import time


def dicas():
    livro.show()

def limpar_dados():
    banco = sqlite3.connect('banco_cadastroGanhos.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastroGanhos")
    dados_lidos = cursor.fetchall()
    tela_listar.tableWidget.setRowCount(len(dados_lidos))
    tela_listar.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_listar.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def limpar_dados2():
    banco2 = sqlite3.connect('banco_cadastroGastos.db')
    cursor2 = banco2.cursor()
    cursor2.execute("SELECT * FROM cadastroGastos")
    dados_lidos2 = cursor2.fetchall()
    tela_listar.tableWidget_2.setRowCount(len(dados_lidos2))
    tela_listar.tableWidget_2.setColumnCount(5)

    for i in range(0, len(dados_lidos2)):
        for j in range(0, 5):
            tela_listar.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos2[i][j])))

        banco2.close()


def gastos():
    nome = tela_cadastro_GG.lineEdit_5.text()
    valor = tela_cadastro_GG.lineEdit_7.text()
    prazo = tela_cadastro_GG.lineEdit_8.text()

    cod = tela_cadastro_GG.lineEdit_6.text()
    categoria = tela_cadastro_GG.lineEdit_11.text()

    if (nome != ""):
        try:
            banco = sqlite3.connect('banco_cadastroGastos.db')
            cursor = banco.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS cadastroGastos ( cod text, nome text,prazo text,valor text,  categoria text)")
            cursor.execute(
                "INSERT INTO cadastroGastos VALUES ('" + cod + "','" + nome + "','" + valor + "','" + prazo + "','" + categoria + "')")

            banco.commit()
            banco.close()

            tela_cadastro_GG.label_3.setText("Gasto cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
def chama_segunda_tela():
    primeira_tela.label_5.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == "adm" and senha == "1234":
        primeira_tela.close()
        segunda_tela.show()

    else:
        primeira_tela.label_5.setText("Login ou senha inválido!")


def logout():
    segunda_tela.close()


def menu_():
    tela_listar.close()
    tela_cadastro_GG.close()
    livro.close()
    segunda_tela.show()




def abre_tela_cadastro():
    tela_cadastro.show()


def abre_tela_cadastroGG():
    tela_cadastro_GG.show()


def listar_dados():
    tela_listar.show()
    banco = sqlite3.connect('banco_cadastroGanhos.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastroGanhos")
    dados_lidos = cursor.fetchall()
    tela_listar.tableWidget.setRowCount(len(dados_lidos))
    tela_listar.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_listar.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    banco.close()

    banco2 = sqlite3.connect('banco_cadastroGastos.db')
    cursor2 = banco2.cursor()
    cursor2.execute("SELECT * FROM cadastroGastos")
    dados_lidos2 = cursor2.fetchall()
    tela_listar.tableWidget_2.setRowCount(len(dados_lidos2))
    tela_listar.tableWidget_2.setColumnCount(5)

    for i in range(0, len(dados_lidos2)):
        for j in range(0, 5):
            tela_listar.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos2[i][j])))


        banco2.close()


def buscar_dados():
    nome = tela_listar.lineEdit.text()
    banco = sqlite3.connect('banco_cadastroGanhos.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastroGanhos WHERE nome = ?", (nome,))
    dados_lidos = cursor.fetchall()
    tela_listar.tableWidget.setRowCount(len(dados_lidos))
    tela_listar.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela_listar.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    banco.close()



def buscar_dados2():
    nome2 = tela_listar.lineEdit_2.text()
    banco2 = sqlite3.connect('banco_cadastroGastos.db')
    cursor2 = banco2.cursor()
    cursor2.execute("SELECT * FROM cadastroGastos WHERE categoria = ?", (nome2,))
    dados_lidos2 = cursor2.fetchall()
    tela_listar.tableWidget_2.setRowCount(len(dados_lidos2))
    tela_listar.tableWidget_2.setColumnCount(5)

    for i in range(0, len(dados_lidos2)):
        for j in range(0, 5):
            tela_listar.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos2[i][j])))

    banco2.close()



def Ganhos():
    cod = tela_cadastro_GG.lineEdit_9.text()
    nome = tela_cadastro_GG.lineEdit.text()
    valor = tela_cadastro_GG.lineEdit_2.text()
    prazo = tela_cadastro_GG.lineEdit_3.text()
    dia = tela_cadastro_GG.lineEdit_4.text()
    categoria = tela_cadastro_GG.lineEdit_10.text()

    if (nome != ""):
        try:
            banco = sqlite3.connect('banco_cadastroGanhos.db')
            cursor = banco.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS cadastroGanhos ( cod text, nome text,prazo text,valor text, dia text, categoria text)")
            cursor.execute(
                "INSERT INTO cadastroGanhos VALUES ('" + cod + "','" + nome + "','" + prazo + "','" + valor + "','" + dia + "','" + categoria + "')")

            banco.commit()
            banco.close()

            tela_cadastro_GG.label_2.setText("Ganho cadastrado com sucesso")



        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)





def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()



    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "')")

            banco.commit()
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")





app = QtWidgets.QApplication([])

primeira_tela = uic.loadUi("Tela Login.ui")
segunda_tela = uic.loadUi("Tela Sucesso.ui")
tela_cadastro = uic.loadUi("Cadastro.ui")
tela_cadastro_GG = uic.loadUi("Cadastrar GG.ui")
tela_listar = uic.loadUi("Listar GG.ui")
livro = uic.loadUi("Livros.ui")

tela_listar.pushButton.clicked.connect(menu_)
tela_cadastro_GG.pushButton_2.clicked.connect(menu_)
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(logout)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
segunda_tela.pushButton_2.clicked.connect(abre_tela_cadastroGG)
segunda_tela.pushButton_3.clicked.connect(listar_dados)
tela_cadastro_GG.pushButton_4.clicked.connect(Ganhos)
tela_listar.pushButton_8.clicked.connect(buscar_dados)
tela_listar.pushButton_9.clicked.connect(buscar_dados2)
tela_cadastro_GG.pushButton_5.clicked.connect(gastos)
tela_listar.pushButton_4.clicked.connect(limpar_dados)
tela_listar.pushButton_7.clicked.connect(limpar_dados2)
tela_cadastro_GG.pushButton.clicked.connect(listar_dados)
segunda_tela.pushButton_4.clicked.connect(dicas)
livro.pushButton_4.clicked.connect(menu_)



primeira_tela.show()
app.exec()