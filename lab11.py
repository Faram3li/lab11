import csv

def read_csv(file_path):
    products = {}
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            product, price = row
            products[product] = float(price)
    return products

def write_csv(file_path, data):
    with open(file_path, mode='w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for product, price in data.items():
            writer.writerow([product, price])

input_file = 'input.csv'
products = read_csv(input_file)

output_file = 'output.csv'
write_csv(output_file, products)


