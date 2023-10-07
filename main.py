import requests
from bs4 import BeautifulSoup
import time

# Define the API key
api_key = '693020c26c7156542c1600e28dfedb35'

# Function to scrape and analyze the data for a given URL
def scrape_and_analyze(url, option, target_price=None):
    # Set up the API request payload
    payload = {
        'api_key': api_key,
        'url': url,
        'follow_redirect': True,
        'render': True,
        'retry_404': True,
        'autoparse': True
    }

    while True:
        # Make the API request
        response = requests.get('https://api.scraperapi.com/', params=payload)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            if option == 1:
                # Option 1: Check for offers
                keyword = 'offer'  # Modify as per the actual content
                if keyword in soup.get_text().lower():
                    print(f"Keyword '{keyword}' found on the page. An offer may be available for this product.")
                    break
                else:
                    print(f"Keyword '{keyword}' not found. No offer detected for this product.")
                    break

            elif option == 2:
                # Option 2: Automate price checking
                price_element = soup.find("span", class_="product-price")  # Modify the selector as needed
                if price_element:
                    product_price = float(price_element.text.replace('₹', '').replace(',', ''))
                    if product_price <= target_price:
                        print("Product is available at or below the target price.")
                        break
                    else:
                        print(f"Product price is ₹{product_price}. Checking again in 10 seconds...")
                else:
                    print("Product price not found. Checking again in 10 seconds...")

            elif option == 3:
                # Option 3: Automate product availability checking
                keyword = 'out of stock'
                if keyword in soup.get_text().lower():
                    print("Product is out of stock. Checking again in 10 seconds...")
                else:
                    print("Product is available.")
                    break

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

        time.sleep(1)

# Get the user's input URL
user_url = input("Enter the URL of the product->  ")
option = int(input("Select an option:\n1. Check for offers\n2. Automate price checking\n3. Automate product availability checking\nEnter the option number: "))

if option == 2:
    target_price = float(input("Enter the target price you want to purchase the product for: "))
else:
    target_price = None

# Call the function to scrape and analyze the data based on the user's choice
scrape_and_analyze(user_url, option, target_price)
