import mouseinfo
import pyautogui
import time

# Função para capturar uma screenshot e salvar
def capturar_screenshot(nome_arquivo='captura.png'):
    screenshot = pyautogui.screenshot()
    screenshot.save(nome_arquivo)
    print(f'Screenshot salva como {nome_arquivo}')

# Função para obter e mostrar a posição atual do mouse
def mostrar_posicao_mouse():
    x, y = pyautogui.position()
    print(f'Posição atual do mouse: ({x}, {y})')

# Função para localizar um elemento na tela por imagem
def localizar_elemento(imagem):
    local = pyautogui.locateOnScreen(imagem)
    if local:
        print(f'Elemento encontrado em: {local}')
        return local
    else:
        print('Elemento não encontrado.')
        return None

# Função para rolar a tela
def rolar_mouse(valor):
    pyautogui.scroll(valor)
    print(f'Rolagem do mouse de valor {valor} realizada')

# Seu fluxo original
pyautogui.alert('Vamos começar', title='Início')

pyautogui.moveTo(1300, 1055, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(1821, 152, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(582, 62, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.write("Casa")
pyautogui.press('enter')

pyautogui.moveTo(308, 191, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(554, 416, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.hotkey('ctrl', 'c')    

pyautogui.press('win')

pyautogui.moveTo(730, 1058, duration=2)
pyautogui.click()
time.sleep(1)

pyautogui.write("paint")

pyautogui.press('enter')

pyautogui.scroll(-10)

mostrar_posicao_mouse()

# Capturar screenshot da tela
capturar_screenshot()

# Tente localizar um elemento (exemplo: 'imagem.png' deve existir no seu diretório)
localizar_elemento('imagem.png')

# Rolar o mouse para baixo 10 "ticks"
rolar_mouse(-10)
