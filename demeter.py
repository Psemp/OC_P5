import requests


class Product:

    def __init__(self, barcode, name, brand, nutriscore, stores):
        self.barcode = barcode
        self.name = name
        self.brand = brand
        self.nutriscore = nutriscore
        self.stores = stores
        self.category_id = []


class Category:

    def __init__(self, web_id, name, link, amount):
        self.web_id = web_id
        self.display_name = name
        self.link = link
        self.amount = amount
        self.id = 0


product_list = []
category_list = []

page_api = 1

category_url = 'https://fr-fr.openfoodfacts.org/categories.json'
r = requests.get(category_url)
category_page = r.json()


def FiltersOnId(catid):
    if '-and-' in catid:
        return True
    else:
        return False


def FiltersOnProductCnt(number):
    if number > 200 and number < 5000:
        return True
    else:
        return False


def BarcodeTest(barcode):
    if len(barcode) == 13:
        return True
    else:
        return False


def SectionsInProduct(prod):
    if 'product_name' in prod and 'categories_hierarchy' in prod and 'brands' in prod and 'nutriscore_grade' in prod and 'stores' in prod:
        return True
    else:
        return False


for web_category in category_page['tags']:

    if FiltersOnProductCnt(web_category['products']) and FiltersOnId(web_category['id']):
        category_list.append(Category(web_category['id'], web_category['name'], web_category['url'], web_category['products']))

print('checkpoint1')
idgen = 1

for category in category_list:
    category.id = idgen
    idgen += 1

product_place_in_list = 0
barcode_dict = {}  # {barcode, product_place_in_list}

for category in reversed(category_list):

    page_api = 1
    products_analyzed = 0
    user_defined_limit = 100

    while page_api < 2:  # (category.amount/20):
        formatted_url = category.link + f'/{page_api}.json'
        r = requests.get(formatted_url)
        productlist_page = r.json()
        # print('checkpoint2')
        print(formatted_url)

        for web_product in productlist_page['products']:
            print('checkpoint3')

            if SectionsInProduct(web_product) and BarcodeTest:

                if web_product['_id'] not in barcode_dict:

                    barcode_dict[web_product['_id']] = product_place_in_list
                    product_list.append(Product(web_product['_id'], web_product['product_name'], web_product['brands'], web_product['nutriscore_grade'], web_product['stores']))
                    product_list[product_place_in_list].category_id.append(category.id)
                    product_place_in_list += 1

                else:
                    # product_list[product_place_in_list].category_id.append(category.id)
                    pass
                products_analyzed += 1

            print('checkpoint4')
        page_api += 1

        print('checkpoint5')

for product in product_list:
    print(product.name)

print(len(category_list))

for category in category_list:
    print(category.web_id, category.link, category.id)
