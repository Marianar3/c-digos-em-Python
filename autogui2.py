import pyautogui
import time
print("Bem Vindo!")
programa=(input("Qual programa você deseja abrir?"))
time.sleep(1)
pyautogui.press("win")
pyautogui.write(programa)
pyautogui.press("enter")