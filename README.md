# CS325Project2(WebScrapper)
## Project Overview
This project scrapes user reviews Best Buy for version of the Ryzen CPU. It Automaticly grabs the reviews from Best Buy and puts the reviews into text files changing the files for each version of the CPU.

## Functionality 
- **Automatic Scrapping**: Retriving user reviews/comments from Best Buy on Ryzen CPU models
- **Version Orginazation**: Each Version of the Ryzen CPU has the reviews seperated into different text files
- **Data Cleaning**: Grabs comments from the model while getting rid of unnecessary data

  ## Products Selection/Version
  For this Project/Code uses the Ryzen CPU and only pulls the first 2 pages of reviews for each
  1. AMD - Ryzen 9 7900X 12-core - 24-Thread 4.7 GHz (5.6 GHz Max Boost) Socket AM5 Desktop Processor - Silver 
    [View](https://www.bestbuy.com/site/reviews/amd-ryzen-9-7900x-12-core-24-thread-4-7-ghz-5-6-ghz-max-boost-socket-am5-desktop-processor-silver/6519473?variant=A)
  2. AMD - Ryzen 9 5900X 4th Gen 12-core, 24-threads Unlocked Desktop Processor Without Cooler - Black
     [View](https://www.bestbuy.com/site/reviews/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler-black/6438942?variant=A)
  4. AMD - Ryzen 5 7600X 6-core - 12-Thread 4.7GHz (5.3 GHz Max Boost) Socket AM5 Desktop Processor - Silver
    [View](https://www.bestbuy.com/site/reviews/amd-ryzen-5-7600x-6-core-12-thread-4-7ghz-5-3-ghz-max-boost-socket-am5-desktop-processor-silver/6519479?variant=A)  
  5. AMD - Ryzen 7 5800X 4th Gen 8-core, 16-threads Unlocked Desktop Processor Without Cooler - Black
    [View](https://www.bestbuy.com/site/reviews/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler-black/6439000?variant=A)
  6.  AMD - Ryzen 9 7950X3D 16-Core - 32-Thread 4.2 GHz (5.7 GHz Max Boost) Socket AM5 Unlocked Desktop Processor - Black
    [View](https://www.bestbuy.com/site/reviews/amd-ryzen-9-7950x3d-16-core-32-thread-4-2-ghz-5-7-ghz-max-boost-socket-am5-unlocked-desktop-processor-black/6537138?variant=A)

## Prerequisite
  Make sure you have Python installed I myself am using at this time Python 3.12.4 and have a basic understanding of python as well.
  Also make sure you have beautifulsoup4 installed with python as it is a required package for this to work I am using beautifulsoup4==4.12.3 as well as needing request package.

## How to use Code
  If you are going to use this code you need to know a few things as well as need to set up the reqirments.
  1. You will need to create a text file that holds all the URLS of the website that you want to scrape the reviews from(I'm not sure if this works for all websites I know it works for Best Buy and somewhat works for Amazon but not fully)
  2. You can clone this repository following this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
  3. Then you can pull form the repository if you have trouble you might be able to just copy and paste the code if you have python and beautifulsoup installed
  4. You will also need to have multiple text files for the reviews to be put in.
  5. This code is used to grab 10 URLS 2 for each product and write them into a text file so you will need to adjust the counter if you have more or less and if you have more or less than 2 URLS for each product and you will need to change the input file path and output file path to match your text files.
  6. You will have to change what the code is looking for in lines 26 & 27 with the div and p class because each website used different named classes and the p might be something else.
  
