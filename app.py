import pyautogui
import time
import subprocess
import os
from datetime import datetime
import random

# Caminhos para os navegadores
CAMINHO_BRAVE = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
CAMINHO_CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Função para salvar o log
def salvar_log(mensagem):
    with open("registro_acao.txt", "a") as log_file:
        horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{horario_atual} - {mensagem}\n")

# Função para verificar se o script pode ser executado hoje
def pode_executar_hoje():
    if os.path.exists("registro_acao.txt"):
        with open("registro_acao.txt", "r") as log_file:
            linhas = log_file.readlines()
            if linhas:
                ultima_data_str = linhas[-1].split(" - ")[0]
                ultima_data = datetime.strptime(ultima_data_str, "%Y-%m-%d %H:%M:%S")
                if ultima_data.date() == datetime.now().date():
                    print("O script já foi executado hoje.")
                    return False
    return True

# Função para abrir o navegador (Brave ou Chrome)
def abrir_navegador(caminho_do_navegador):
    try:
        subprocess.Popen([caminho_do_navegador])
        salvar_log(f"Navegador aberto: {caminho_do_navegador}")
    except Exception as e:
        salvar_log(f"Erro ao abrir o navegador: {e}")
        print("Erro ao abrir o navegador!")

# Função para mover o mouse de maneira aleatória e clicar
def clicar_randomico(x1, y1, x2, y2):
    pyautogui.moveTo(random.randint(x1, x2), random.randint(y1, y2), duration=random.uniform(0.5, 1.5))
    pyautogui.click()
    time.sleep(random.uniform(1.5, 3.5))

# Função para garantir que o navegador tenha tempo para abrir
def esperar_navegador_abrir():
    time.sleep(5)  # Aumentei o tempo para garantir que o navegador abra completamente
    salvar_log("Esperando o navegador abrir")

# Função para abrir uma nova guia
def abrir_nova_guia():
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)
    salvar_log("Nova guia aberta")

# Função para clicar no favorito específico
def selecionar_favorito():
    pyautogui.click(50, 50)
    time.sleep(1)
    pyautogui.click(1830, 100)
    time.sleep(1)
    salvar_log("Favorito selecionado e página aberta")

# Função para clicar na Plaza
def clicar_plaza():
    pyautogui.click(1839, 180)
    pyautogui.click(1839, 180)
    time.sleep(1)
    salvar_log("Clicado na Plaza")

# Função para conectar a carteira
def conectar_carteira():
    pyautogui.click(1350, 150)
    pyautogui.click(700, 450)
    pyautogui.write("freitas56")
    pyautogui.click(1800, 430)
    salvar_log("Carteira conectada")

# Função para acessar tokens da Plaza
def plaza_tokens():
    pyautogui.click(550, 850)
    time.sleep(5)
    salvar_log("Tokens da Plaza acessados")

# Função para acessar o portfólio
def acessar_portifolio():
    pyautogui.click(650, 150)
    time.sleep(1)
    salvar_log("Acessado portfólio")

# Função para realizar compra de Bondeth
def comprar_bondeth():
    pyautogui.click(940, 850)
    pyautogui.click(500, 500)
    pyautogui.write("0.5")
    pyautogui.click(650, 900)
    time.sleep(4)
    pyautogui.click(1700, 750)
    pyautogui.click(1700, 750)
    time.sleep(5)
    salvar_log("Bondeth comprado")

# Função para realizar venda de Bondeth
def vender_bondeth():
    pyautogui.click(975, 850)
    pyautogui.click(500, 500)
    pyautogui.write("0.5")
    pyautogui.click(650, 900)
    time.sleep(4)
    pyautogui.click(1700, 750)
    pyautogui.click(1700, 750)
    time.sleep(5)
    salvar_log("Bondeth vendido")

# Função para realizar compra de Leveth
def comprar_leveth():
    pyautogui.click(550, 250)
    pyautogui.scroll(-300)
    pyautogui.click(950, 800)
    pyautogui.click(500, 500)
    pyautogui.write("0.5")
    pyautogui.click(650, 900)
    time.sleep(3.5)
    pyautogui.click(1700, 750)
    pyautogui.click(1700, 750)
    time.sleep(5)
    salvar_log("Leveth comprado")

# Função para realizar venda de Leveth
def vender_leveth():
    pyautogui.click(550, 250)
    pyautogui.scroll(-300)
    pyautogui.click(975, 800)
    pyautogui.click(500, 500)
    pyautogui.write("0.5")
    pyautogui.click(650, 900)
    time.sleep(3.5)
    pyautogui.click(1700, 750)
    pyautogui.click(1700, 750)
    time.sleep(6)
    salvar_log("Leveth vendido")

# Função para realizar Airdrop no Node
def node_airdrop():
    pyautogui.click(600, 70)
    pyautogui.write("https://node.securitylabs.xyz/")
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.click(1600, 710)
    pyautogui.sleep(2)
    pyautogui.click(1600, 710)

# Função para realizar Airdrop no One Futebol
def onefutebol():
    pyautogui.click(600, 70)
    pyautogui.write("https://ofc.onefootball.com/s2/")
    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.click(600, 500)
    pyautogui.scroll(-1200)
    pyautogui.click(1450, 550)
    pyautogui.click(1450, 550)

# Função para realizar Airdrop no Chrome
def node_airdrop_chrome():
    try:
        subprocess.Popen([CAMINHO_CHROME])
        salvar_log("Chrome aberto")
    except Exception as e:
        salvar_log(f"Erro ao abrir o Chrome: {e}")
        print("Erro ao abrir o Chrome!")
    
    pyautogui.sleep(3)
    pyautogui.click(600, 70)
    pyautogui.write("https://node.securitylabs.xyz/")
    pyautogui.press('enter')
    pyautogui.sleep(20)
    pyautogui.click(1600, 710)
    pyautogui.sleep(2)
    pyautogui.click(1600, 710)
    pyautogui.sleep(10)
    pyautogui.hotkey('alt', 'f4')

# Função para fechar a guia atual
def fechar_guia():
    pyautogui.hotkey('ctrl', 'w')
    salvar_log("Guia fechada")

# Automação
if pode_executar_hoje():
    abrir_navegador(CAMINHO_BRAVE)
    esperar_navegador_abrir()
    abrir_nova_guia()
    selecionar_favorito()
    clicar_plaza()
    conectar_carteira()
    plaza_tokens()
    acessar_portifolio()
    comprar_bondeth()
    acessar_portifolio()
    vender_bondeth()
    acessar_portifolio()
    comprar_leveth()
    acessar_portifolio()
    vender_leveth()
    node_airdrop()
    onefutebol()
    fechar_guia()
    node_airdrop_chrome()
else:
    print("O script não será executado hoje. A execução será feita amanhã.")
