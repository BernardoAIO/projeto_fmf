import json

def find_duplicates(products):
    seen_links = set()
    seen_models = set()
    duplicates = []

    for product in products:
        if (product['link'] in seen_links) or (product['modelo'] in seen_models):
            duplicates.append(product)
        else:
            seen_links.add(product['link'])
            seen_models.add(product['modelo'])

    return duplicates

# Carregar os links dos produtos do arquivo JSON
with open('links_filtrados.json', 'r') as json_file:
    products = json.load(json_file)

total_products = len(products)
print(f"Total de produtos no JSON: {total_products}")

duplicate_products = find_duplicates(products)

if len(duplicate_products) > 0:
    print("Produtos com links ou modelos duplicados:")
    for product in duplicate_products:
        print(f"Link: {product['link']}, Modelo: {product['modelo']}")
else:
    print("Nenhum produto com links ou modelos duplicados encontrado.")
