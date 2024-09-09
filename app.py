import pyautogui
from time import sleep
from mouseinfo import mouseInfo


# mouseInfo()

# Cadastrar Usuario


# - clicar e inserir o usuario
pyautogui.click(997,537, duration=2)
pyautogui.write('Daniel')
# - clicar e digitar senha
pyautogui.click(996,567, duration=2)
pyautogui.write('dandan123')

# - clicar em entrar
pyautogui.click(869,600, duration=2)

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