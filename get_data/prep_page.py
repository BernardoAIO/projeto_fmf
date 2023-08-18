import pyautogui
import time
from bs4 import BeautifulSoup
import requests
import pyautogui
import time
import clipboard
import json
from pywinauto import Desktop, Application


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}


def rolar_comments():
    # Move the mouse to the left side of the screen
    screen_height = pyautogui.size().height
    screen_width = pyautogui.size().width
    middle_screen_x = screen_width // 2
    middle_screen_y = screen_height // 2

    pyautogui.moveTo(middle_screen_x, middle_screen_y)

    left_edge_x = 780

    pyautogui.moveTo(left_edge_x, middle_screen_y)
    time.sleep(1)

    # Scroll down
    scroll_amount = 6460  # Adjust this value as needed
    pyautogui.scroll(-scroll_amount)
    #
    # Wait for a moment to allow content to load
    time.sleep(2)  # Adjust the delay as needed




    # Find and click the button using image recognition
    button_image_path = 'img.png'  # Replace with the actual path
    time.sleep(1)
    button_location = pyautogui.locateCenterOnScreen(button_image_path)
    time.sleep(2)


    cont = 0


    if button_location:
        pyautogui.click(button_location)
    else:
        pyautogui.scroll(-10000)
        button_location = pyautogui.locateCenterOnScreen(button_image_path)
        if button_location:
            pyautogui.click(button_location)
        else:
            print("Button not found on the screen.")
            return False

    for i in range(0, 100):
        pyautogui.scroll(-10000)
        time.sleep(0.5)



def middle_screen(x=0,y=0):
    screen_height = pyautogui.size().height
    screen_width = pyautogui.size().width
    middle_screen_x = screen_width // 2
    middle_screen_y = screen_height // 2
    pyautogui.moveTo(middle_screen_x-x, middle_screen_y-y)
    return middle_screen_x, middle_screen_y



def get_html():
    middle_screen(100)

    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('f12')
    time.sleep(1)
    pyautogui.moveTo(1200, 500)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')  # Use hotkey() to simulate pressing multiple keys
    pyautogui.write('infinite-scroll-component')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.moveTo(1166, 772)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    html = clipboard.paste()  # Use clipboard.paste() to get content from clipboard
    return html


def write_html(html, location='page.html'):

    with open(location, 'w', encoding='utf-8') as f:
        f.write(html)


def read_links_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            products = json.load(file)
            links = [product['link'] for product in products]
            return links
    except FileNotFoundError:
        print(f"O arquivo '{file_path}' não foi encontrado.")
        return []


def remove_duplicate_links(links):
    unique_links = list(set(links))
    return unique_links


def get_url():
    pyautogui.moveTo(780, 50)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    url = clipboard.paste()  # Use clipboard.paste() to get content from clipboard
    return url


def extract_product_name_from_url(page_url):
    start_index = page_url.find('com.br/') + len('com.br/')
    end_index = page_url.find('/p/')

    if start_index != -1 and end_index != -1:
        name = page_url[start_index:end_index]
        return name
    else:
        return None


def open_new_tab(link='https://www.google.com/'):
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.write(link)
    time.sleep(1)
    pyautogui.press('enter')


if __name__ == '__main__':

    Application().start(r"C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 ")

    #Maximize
    time.sleep(1)
    # pyautogui.hotkey('win', 'up')
    # time.sleep(1)

    filepath = '../links_extras.json' \
               ''

    links = read_links_from_json(filepath)
    links = remove_duplicate_links(links)
    print('Foram achados x links únicos:', len(links))
    #
    links_adicionados = []

    links_defeituosos = []

    for link in links:
        print("Abrindo link:", link)
        open_new_tab(link)
        time.sleep(2)

        middle_screen()

        confere = rolar_comments()

        if confere == False:
            print("&"*50)
            print("Não foi possível encontrar o botão de carregar mais comentários.")
            print("Adicionando link à lista de links defeituosos.")
            links_defeituosos.append(link)
            print("Links defeituosos:", links_defeituosos)
            #Pular para o próximo link
            print("Aguardando 2 segundos para o próximo link...")
            print("&"*50)
            time.sleep(2)
            continue

        html = get_html()

        url = get_url()

        nome = extract_product_name_from_url(link)

        write_html(html, f'pages/{nome}.html')



        links_adicionados.append(link)

        print("-"*100)
        print("links adicionados:", links_adicionados)
        print("\n")
        print("links defeituosos:", links_defeituosos)
        #Análise de quantos links foram adicionados
        print(f"Links adicionados: {len(links_adicionados)} de {len(links)}")
        #Porcentagem do processo realizado
        print(f"Porcentagem: {round(len(links_adicionados)/len(links)*100, 2)}%")
        #Tempo estimado para finalizar o processo
        print(f"Tempo estimado: {round((len(links)-len(links_adicionados))*2/60, 2)} minutos")
        print("Aguardando 2 segundos para o próximo link...")
        print("-" * 100)
        time.sleep(2)
