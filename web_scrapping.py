import requests
from bs4 import BeautifulSoup
import csv
import time

def get_product_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    max_retries = 5
    retries = 0
    
    while retries < max_retries:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            products = []

            # Extract product information
            for product in soup.find_all('div', class_='s-item'):
                name = product.find('h2', class_='s-title-instructions').text.strip()
                price = product.find('span', class_='a-offscreen').text.strip()
                rating = product.find('span', class_='a-icon-alt')

                if rating:
                    rating = rating.text.strip().split(' ')[0]
                else:
                    rating = 'Not available'

                products.append({
                    'Name': name,
                    'Price': price,
                    'Rating': rating
                })

            return products
        elif response.status_code == 503:
            print(f"Retrying... ({retries + 1}/{max_retries})")
            retries += 1
            time.sleep(2 ** retries)  # Exponential backoff
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

    print("Maximum number of retries reached. Exiting.")
    return None

def save_to_csv(products, filename='product_data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == "__main__":
    url = 'https://www.amazon.com/s?k=laptop'
    product_data = get_product_data(url)

    if product_data:
        save_to_csv(product_data)
        print("Product data saved to 'product_data.csv'")
