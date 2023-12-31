# import module
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}


# user define function
# Scrape the data
def getdata(location):
    # pass the location
    # into requests.get() function
    # ler o texto do arquivo html
    with open(location, 'r', encoding='utf-8') as f:
        page = f.read()

    return page


def html_code(page_url):
    # pass the url
    # into getdata function
    # clicar em butao

    htmldata = getdata(page_url)
    s = BeautifulSoup(htmldata, 'html.parser')
    return s


def cus_data(s):
    # find the Html tag
    # with find()
    # and convert into string

    cus_list = [item.get_text() for item in s.find_all("span", class_="a-profile-name")]
    return cus_list


def cus_rev(s, name, page, brand, model):
    # find the Html tag
    # with find()
    # and convert into string
    # print(inf_scroll.prettify())
    review_items = s.find_all("article", class_="ui-review-capability-comments__comment")
    # print(review_items)
    rev_result = []

    for item in review_items:
        data = item.find("span", class_="ui-review-capability-comments__comment__date").get_text()
        data = format_date(data)
        review = item.find("p", class_="ui-review-capability-comments__comment__content").get_text()
        stars = item.find("p", class_="andes-visually-hidden").get_text()
        stars = stars[10]
        rev_result.append({'review': review, 'date': data, 'product': name, 'url': page, 'stars': stars, 'brand': brand,
                           'model': model})

    return rev_result


def convert_month_abbr(input_month):
    month_mapping = {
        'jan.': 'Jan.',
        'fev.': 'Feb.',
        'mar.': 'Mar.',
        'abr.': 'Apr.',
        'mai.': 'May',
        'jun.': 'Jun.',
        'jul.': 'Jul.',
        'ago.': 'Aug.',
        'set.': 'Sep.',
        'out.': 'Oct.',
        'nov.': 'Nov.',
        'dez.': 'Dec.'
    }

    return month_mapping.get(input_month.lower(), input_month)


def format_date(input_date):
    day, month, year = input_date.split()
    formatted_month = convert_month_abbr(month)
    formatted_date = f'{day} {formatted_month} {year}'

    return formatted_date


def extract_product_name_from_url(page_url):
    start_index = page_url.find('com.br/') + len('com.br/')
    end_index = page_url.find('/p/')

    if start_index != -1 and end_index != -1:
        name = page_url[start_index:end_index]
        return name
    else:
        return None



def read_products_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            products = json.load(file)
            return products
    except FileNotFoundError:
        print(f"O arquivo '{file_path}' não foi encontrado.")
        return []

def remove_duplicate_products(products):
    unique_products = []
    seen_products = set()
    for product in products:
        product_tuple = (product['link'], product['modelo'], product['marca'])
        if product_tuple not in seen_products:
            seen_products.add(product_tuple)
            unique_products.append(product)
    return unique_products


if __name__ == '__main__':

    file_path = 'links_seguranca.json'  # Substitua pelo caminho do seu arquivo JSON

    products = read_products_from_json(file_path)
    unique_products = remove_duplicate_products(products)

    for product in unique_products:

        url = product['link']

        marca = product['marca']

        modelo = product['modelo']

        product_name = extract_product_name_from_url(url)

        page_loc = f'pages/{product_name}.html'

        marca = marca.lower()

        modelo = modelo.lower()
        try:
            soup = html_code(page_loc)
        except:
            print(f"Não foi possível ler o arquivo '{page_loc}'")
            continue

        # cus_res = cus_data(soup)
        rev_data = cus_rev(soup, product_name, url, marca, modelo)
        # print(rev_data)

        # print(cus_res)
        # print(rev_data)

        # Create a DataFrame from a list of dictionaries
        df = pd.DataFrame(rev_data)

        # Mostras a descrição do DataFrame
        # print('DataFrame description:')
        # print(df.describe())

        # Save the DataFrame to a CSV file on "output_tables_test" folder
        df.to_csv(f'output_tables/{product_name}.csv', index=False, encoding='utf-8-sig')

        print('CSV file saved successfully!')
