from selenium import webdriver
import os
import sys
import time
from selenium.webdriver.chrome.options import Options
import keyboard
from PyQt5 import uic, QtWidgets
import sqlite3
import threading

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--disable-extensions");
chrome_options.add_argument("test-type");
chrome_options.add_argument("--silent");
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("-headless")

navegador = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))
navegador.maximize_window()

def acao():
    nome_usuario = primeira_tela.lineEdit.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT selecao FROM cadastro WHERE nome ='{}'".format(nome_usuario))
        selecao_bd = cursor.fetchall()
        print(selecao_bd[0][0])
    except:
        print('erro')
        return
    try:
        cursor.execute("SELECT classificação FROM cadastro WHERE nome ='{}'".format(nome_usuario))
        classificação_bd = cursor.fetchall()
        print(classificação_bd[0][0])
    except:
        print('erro')
        return
    while True:
        try:
            if keyboard.is_pressed(selecao_bd[0][0]):
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[5]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[6]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[7]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[8]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[9]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[10]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[11]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[12]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[13]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[14]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[15]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[16]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[17]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[18]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[19]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[20]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
            elif keyboard.is_pressed(classificação_bd[0][0]):
                navegador.find_element_by_xpath('//*[@id="outputPersistent"]/div/div[2]/div/div[2]/div/button/span[1]').click()
                navegador.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div/div[1]/div[1]/select/option[6]').click()
                navegador.find_element_by_xpath('/ html / body / div[3] / div[3] / div / div[3] / div / button[2] / span[1]').click()

        except:
            pass

def tela_cadastro():
    primeira_tela.close()
    segunda_tela.show()

def voltar():
    segunda_tela.close()
    primeira_tela.show()
    segunda_tela.label_7.setText("")

def cadastrar():
    def logar1():
        nome = segunda_tela.lineEdit.text()
        email = segunda_tela.lineEdit_2.text()
        senha = segunda_tela.lineEdit_3.text()
        selecao = segunda_tela.lineEdit_4.text()
        classificacao = segunda_tela.lineEdit_5.text()
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,email text,senha text,selecao text,classificação text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+email+"','"+senha+"','"+selecao+"','"+classificacao+"')")

            banco.commit()
            banco.close()
            segunda_tela.label_7.setText("Salvo com sucesso !")
            time.sleep(4)
            segunda_tela.label_7.setText("")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)

    tarefa = threading.Thread(target=logar1)
    tarefa.daemon = True
    tarefa.start()

def logar():
    def logar1():
        nome_usuario = primeira_tela.lineEdit.text()
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()
        try:
            cursor.execute("SELECT email FROM cadastro WHERE nome ='{}'".format(nome_usuario))
            email_bd = cursor.fetchall()
        except:
            primeira_tela.label_3.setText('   usuário não cadastrado')
            return
        try:
            cursor.execute("SELECT senha FROM cadastro WHERE nome ='{}'".format(nome_usuario))
            senha_bd = cursor.fetchall()
        except:
            primeira_tela.label_3.setText('   usuário não cadastrado')
            return
        try:
            cursor.execute("SELECT selecao FROM cadastro WHERE nome ='{}'".format(nome_usuario))
            selecao_bd = cursor.fetchall()
        except:
            print('erro')
            return
        try:
            cursor.execute("SELECT classificação FROM cadastro WHERE nome ='{}'".format(nome_usuario))
            classificação_bd = cursor.fetchall()
        except:
            print('erro')
            return
        primeira_tela.label_3.setText('entrando na conta, aguarde')
        navegador.get("https://plataforma.offertech.com.br")
        navegador.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/button/span[1]').click()
        time.sleep(5)
        navegador.find_element_by_xpath('//*[@id="1-email"]').send_keys(email_bd[0][0])
        navegador.find_element_by_xpath(
            '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/div/input').send_keys(senha_bd[0][0])
        navegador.find_element_by_xpath(
            '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button/span').click()
        primeira_tela.label_3.setText('         Conectado a conta')
        while True:
            try:
                if keyboard.is_pressed(selecao_bd[0][0]):
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[5]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[6]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[7]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[8]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[9]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[10]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[11]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[12]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[13]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[14]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[15]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[16]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[17]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[18]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[19]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[1]/div[2]/div[2]/div/div[2]/div/div[20]/div/div/div[1]/div[1]/div/div[2]/div[5]/div[1]/span/span[1]/input').click()
                elif keyboard.is_pressed(classificação_bd[0][0]):
                    navegador.find_element_by_xpath(
                        '//*[@id="outputPersistent"]/div/div[2]/div/div[2]/div/button/span[1]').click()
                    navegador.find_element_by_xpath(
                        '/ html / body / div[4] / div[3] / div / div[2] / div / div[1] / div[1] / select').click()
                    navegador.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div/div[2]/div/div[1]/div[1]/select/option[6]').click()
                    navegador.find_element_by_xpath(
                        '/html/body/div[4]/div[3]/div/div[3]/div/button[2]/span[1]').click()

            except:
                pass


    tarefa = threading.Thread(target=logar1)
    tarefa.daemon = True
    tarefa.start()




app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("FILE_1.ui")
segunda_tela = uic.loadUi("FILE_2.ui")
primeira_tela.pushButton_3.clicked.connect(tela_cadastro)
primeira_tela.pushButton.clicked.connect(logar)
segunda_tela.pushButton_4.clicked.connect(voltar)
segunda_tela.pushButton_3.clicked.connect(cadastrar)
primeira_tela.show()
app.exec()