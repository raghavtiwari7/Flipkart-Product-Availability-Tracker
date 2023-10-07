


import requests
from bs4 import BeautifulSoup
import time
from send_email import send_info

# Define the ScraperAPI request payload
def check_product_availability(product_url, recipient_email):
    api_key = 'KKKKKKKKKKKKKKKKKKKKK'
    scraperapi_endpoint = 'https://api.scraperapi.com/'

    payload = {
        'api_key': api_key,
        'url': product_url,
        'follow_redirect': True,
        'render': True,
        'retry_404': True,
        'autoparse': True
    }

    while True:
        # Make the API request
        response = requests.get(scraperapi_endpoint, params=payload)


















































# import requests
# from bs4 import BeautifulSoup
# import time

# # Define the API key and ScraperAPI endpoint
# api_key = '693020c26c7156542c1600e28dfedb35'
# scraperapi_endpoint = 'https://api.scraperapi.com/'

# # Prompt the user to enter the product URL
# product_url = input("Enter the Flipkart product URL: ")

# # Define the ScraperAPI request payload
# payload = {
#     'api_key': api_key,
#     'url': product_url,
#     'follow_redirect': True,
#     'render': True,
#     'retry_404': True,
#     'autoparse': True
# }

# while True:
#     # Make the API request
#     response = requests.get(scraperapi_endpoint, params=payload)

#     if response.status_code == 200:
#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Check if the product is available based on the presence of a "Buy Now" button
#         buy_now_button = soup.find('button', {'class': '_2KpZ6l _2U9uOA _3v1-ww'})
        
#         if buy_now_button:
#             print("Product is available.")
#             break
#         else:
#             print("Product is currently out of stock. Checking again in 2 seconds...")
#             time.sleep(2)  # Wait for 2 seconds before checking again
#     else:
#         print(f"Failed to fetch data. Status code: {response.status_code}")
#         break

    
    
    
    
    
# import requests
# from bs4 import BeautifulSoup

# # Define the API key and request payload
# api_key = '693020c26c7156542c1600e28dfedb35'
# url = 'https://www.flipkart.com/asus-zenfone-max-pro-m1-grey-32-gb/p/itmf4hg4z55waayn?pid=MOBF3A8UMME3H2BZ&lid=LSTMOBF3A8UMME3H2BZPJPNUD'

# payload = {
#     'api_key': api_key,
#     'url': url,
#     'follow_redirect': True,
#     'render': True,
#     'retry_404': True,
#     'autoparse': True
# }

# # Make the API request
# response = requests.get('https://api.scraperapi.com/', params=payload)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Print the parsed HTML content
# print(soup)
