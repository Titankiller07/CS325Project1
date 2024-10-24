import requests
from bs4 import BeautifulSoup
import time
import random

input_file_path = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325Project2\\Website_url.txt"  # Path to the URL text file
output_file_path_template = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325Project2\\Reviews_{}.txt"  # Path template for the output reviews file

# Set up the User-Agent to mimic a browser
def get_bestbuy_reviews(product_url):
    headers = {#What the browser sends to the server to identify
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive"
    }
    reviews = []
    response = requests.get(product_url, headers=headers)#Sends a GET request to the specified URL and returns a response object
    if response.status_code != 200:#Checks if the request was successful (status code 200 means success)
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')#Parses the HTML content of the page using BeautifulSoup
    reviews = []#List to store the reviews
    # Update to find the specific review class
    for review in soup.find_all('div', class_="ugc-review-body"):#Finds all the review elements on the page using the specified class name
        body = review.find('p', class_="pre-white-space")#Finds the text of the review within the review element
        if body:#Checks if the review text was found
            review_text = body.get_text(separator=' ').strip()
            reviews.append(review_text)
    return reviews#Returns the list of reviews

# Read the product URLs from the input file
with open(input_file_path, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]  # Read URLs and remove extra whitespace

# Process each URL and write reviews to a new file every 3 URLs
for i, product_url in enumerate(urls):
    # Define the product URL with pagination placeholder
    product_url_with_pagination = product_url
    reviews = get_bestbuy_reviews(product_url_with_pagination)

    # Change output file based on URL index
    if i >= 0 and i < 2:
        index  = 1  # First three URLs
    elif i >= 2 and i < 4:
        index  = 2  # Second three URLs
    elif i >= 4 and i < 6:
        index = 3  # Third three URLs
    elif i >= 6 and i < 8:
        index = 4  # Fourth three URLs
    elif i >= 8 and i < 10:
        index = 5  # Fith three URLs    

    # Write the reviews to the output file
    if reviews:
        with open(output_file_path_template.format(index), 'w', encoding='utf-8') as file:  # Open the file in write mode
            file.writelines(review + "\n" for review in reviews)#Writes the review to the file
            print(reviews)  # Optionally print to console
    else:
        print(f"No reviews found for {product_url}.")#If no reviews are found, it prints that no reviews were found for that product

time.sleep(random.uniform(1, 3))  # Wait between requests
