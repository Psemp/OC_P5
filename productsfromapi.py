
import json
import requests

class Product:

    def __init__(self, barcode, name, brand, nutriscore, stores):
        self.barcode = barcode
        self.name = name
        self.brand = brand
        self.nutriscore = nutriscore
        self.stores = stores

class Unsorted:

    def __init__(self, barcode, maincat, secondcat):
        self.barcode = barcode
        self.maincat = maincat
        self.secondcat = secondcat
        del self.secondcat[-1]

class Category:

    def __init__(self, number):
        self.maincat = 'maincat'
        self.identifier = number
        self.secondcat = []
        self.barcode_list = []

category_dict = dict()
alert_dict = dict()
product_list = []
unsorted_list = []
category_list = []

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
            unsorted_list.append(Unsorted(raw_product['_id'],raw_product['categories_hierarchy'][-1],raw_product['categories_hierarchy']))
            category_dict[raw_product['_id']] = raw_product['categories_hierarchy']

            # if 'labels' in raw_product:
            #     alert_dict[raw_product['_id']] = raw_product['labels']

    page_api = page_api + 1

    ##CONTROLS##
    print(page_api)
    print(url)

nbr = 1
identifier = f'id{nbr}'

while nbr <= len(unsorted_list):
    identifier = Category(nbr)
    category_list.append(identifier)
    nbr +=1
    print(identifier, identifier.maincat)

nbr = 1

for unsortedcat in unsorted_list:
    for sortedcat in category_list:
        if unsortedcat.maincat == sortedcat.maincat:
            sortedcat.barcode_list.append(unsortedcat.barcode)
            sortedcat.secondcat.append(unsortedcat.secondcat)
            print('if in loop')
        else:
            sortedcat.maincat = unsortedcat.maincat
            sortedcat.secondcat = unsortedcat.secondcat
            sortedcat.barcode_list.append(unsortedcat.barcode)
            del unsorted_list[unsortedcat]
            print('else in loop')
        nbr += 1


# PRINTS

# for product in product_list:
#     print(product.barcode, product.name, product.nutriscore)

for category in category_list:
    print(category.maincat, category.secondcat)

##CONTROLS##
# print(category_dict)
