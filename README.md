# CS325Project2
This project is about using python to grab reviews from a website and pulling only the text and pushing it into a text file to save and pulling the URLS form a text file
1. download beautifulSoup for pyhton if you have python installed if not please do for this to work the you need to go to the python terminal an use pip install beautifulsoup4.
2. Then grab links for the website that you want to scrape with reviews like Amazon or other websites(Amazon has problems using multiple URLS and acessing them fast and will not pull all reviews from this site some reviews with work)
3. If using my code change the file that it is pulling the URLs from with your own and change the div class to match the reviews on the website
4. BeautifulSoup uses the URL and acceses the HTML Code and can pull speciffic items with is but you have to go to the website and inspect it to find what the div nad classes are called so you can chaneg the code to match so it can work and pull the reviews using the class for the div and span/p depending on the website
5. This code also pushes the reviews into a text file with the name Reviews_# with the number changing so each text file only has the reviews for one item changing evey 2 URLS to another text file and item
