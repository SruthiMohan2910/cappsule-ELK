from elasticsearch import Elasticsearch
import csv

# Replace 'localhost' with your Elasticsearch server address
es = Elasticsearch(['http://localhost:9200/'])

with open('/Users/sruthimohan/Desktop/cappsule-elk/medicines_01.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # extract values from row
        product_name = row['name']
        description = row['description']
        sideEffects = row['sideEffects']
        prescription = row['prescription']
        composition = row['composition']
        manufacturer = row['manufacturer']
        units = row['units']
        expiry_date = row['LastUpdated']
        price = row['bestPrice1mg']

        # create document
        doc = {
            'product_name': product_name,
            'description': description,
            'sideEffects': sideEffects,
            'prescription': prescription,
            'composition': composition,
            'manufacturer': manufacturer,
            'units': units,
            'expiry_date': expiry_date,
            'price': price
        }

        # index document in Elasticsearch
        res = es.index(index='pharmacy_inventory', body=doc)
        print(res)
