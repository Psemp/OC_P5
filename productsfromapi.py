
import json
import requests

class Product:

    def __init__(self, barcode, name, brand, nutriscore, stores):
        self.barcode = barcode
        self.name = name
        self.brand = brand
        self.nutriscore = nutriscore
        self.stores = stores

# class Category:

#     def __init__(self):
#         self.name = str
#         self.translated_name = str

category_dict = dict()
alert_dict = dict()
product_list = []

page_api = 1
sample_size = int

print("sample size ?")
sample_size = int(input())

while len(product_list) < sample_size:

    url = f'https://fr-en.openfoodfacts.org/language/french/{page_api}.json'
    r = requests.get(url)
    productlist_json = r.json()

    for raw_product in productlist_json['products']:

        if len(raw_product['_id']) == 13 and 'product_name' in raw_product and 'categories_hierarchy' in raw_product and 'brands' in raw_product and 'nutriscore_grade' in raw_product and 'stores' in raw_product:
            print(raw_product['_id']) ##CONTROL##

            product_list.append(Product(raw_product['_id'], raw_product['product_name'], raw_product['brands'], raw_product['nutriscore_grade'], raw_product['stores']))

            category_dict[raw_product['_id']] = raw_product['categories_hierarchy']

            # if 'labels' in raw_product:
            #     alert_dict[raw_product['_id']] = raw_product['labels']

    page_api = page_api + 1

    ##CONTROLS##
    print(page_api)
    print(url)

for product in product_list:
    print(product.barcode, product.name, product.nutriscore.upper)

##CONTROLS##
# print(category_dict)
