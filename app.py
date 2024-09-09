import pyautogui
from time import sleep
from mouseinfo import mouseInfo


# mouseInfo()

#abrir app a partir da barra de tarefas
position_app = pyautogui.locateOnScreen('imageApp.png')
pyautogui.click(position_app)

# Cadastrar Usuario
pyautogui.click(974,595, duration=2)
pyautogui.click(997,537, duration=2)
pyautogui.write('Daniel')
pyautogui.click(996,567, duration=2)
pyautogui.write('dandan123')

#clicar em registrar
pyautogui.click(909,598, duration=1)

# - clicar e inserir o usuario
pyautogui.click(997,537, duration=2)
pyautogui.write('Daniel')
# - clicar e digitar senha
pyautogui.click(996,567, duration=2)
pyautogui.write('dandan123')

# - clicar em entrar
pyautogui.click(868,595, duration=2)

# - extrair cada produto
with open('produtos.txt', "r") as file:
    for line in file:
        product = line.split(",")[0]
        quantity = line.split(",")[1]
        price = line.split(",")[2]
    # 	1- clicar e digitar produto
        pyautogui.click(696,530, duration=2)
        pyautogui.write(product)
    # 	2- clicar e digitar quantidade
        pyautogui.click(707,549, duration=2)
        pyautogui.write(quantity)
    # 	3- clicar e digitar preço
        pyautogui.click(712,578, duration=2)
        pyautogui.write(price)
    # 	4- 2- clicar em registrar
        pyautogui.click(597,732, duration=2)
        sleep(1)