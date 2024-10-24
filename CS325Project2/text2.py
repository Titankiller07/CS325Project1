import requests
from bs4 import BeautifulSoup
import time
import random

input_file_path = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325Project2\\Website_url.txt"
output_file_path = "C:\\Users\\cmthi\\OneDrive\\Documents\\Java\\CS325Project2\\Reviews_{}.txt"  # Output file

# Set up the User-Agent to mimic a browser
def get_bestbuy_reviews(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive"
    }
    
    reviews = []
    response = requests.get(product_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the page: {product_url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    for review in soup.find_all('div', class_="ugc-review-body"):
        body = review.find('p', class_="pre-white-space")
        if body:
            review_text = body.get_text(separator=' ').strip()
            reviews.append(review_text)
    
    return reviews

# Read the product URLs from the input file
with open(input_file_path, 'r') as file:
    urls = [line.strip() for line in file if line.strip()]

# Process each URL and write reviews to the output file every 2 URLs
for i in range(0, len(urls), 2):
    reviews_to_write = []
    
    # Collect reviews for the next two URLs
    for j in range(2):
        if i + j < len(urls):
            product_url = urls[i + j]
            reviews = get_bestbuy_reviews(product_url)
            reviews_to_write.append(f"\nReviews for {product_url}:\n")
            reviews_to_write.extend(review + "\n" for review in reviews)

    # Write the reviews to the output file (overwrite) 
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
    with open(output_file_path.format(index), 'w', encoding='utf-8') as file:  # Open the file in write mode
        file.writelines(reviews_to_write)  # Write all collected reviews
        print(f"Wrote reviews for URLs {i+1} and {i+2} to {output_file_path.format(index)}")

    time.sleep(random.uniform(1, 3))  # Wait between requests





