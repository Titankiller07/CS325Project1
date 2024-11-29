# CS325Project2(WebScrapper)
## Project Overview
This project combines the other 2 projects by using the reivews from the web scrapper and feeding the reviews into the phi3 model and asking if the reviews are positive, negative, or neutral and putting the responses into a text file for each product

## Functionality 
- **Read Input Files**: The FileReader class reads multiple text files (up to 5 by default) that contain statements, typically reviews or opinions.
- **Analyze Sentiment**: The SentimentAnalyzer class uses the Ollama model (in this case, Phi3) to classify each statement's sentiment.
For each line in the input file, a prompt is sent to the Ollama model asking it to classify whether the sentiment is positive, negative, or neutral.
The Ollama model responds with one of these labels, which is then written to an output file.
- **Store and Output Results**: The analysis results (sentiment classification for each line) are saved into new text files

  ## Products Selection/Version
  For this Project/Code uses the Ryzen CPU and only pulls the first 2 pages of reviews for each:
  1. **AMD - Ryzen 9 7900X 12-core - 24-Thread 4.7 GHz (5.6 GHz Max Boost) Socket AM5 Desktop Processor - Silver** 
    [View](https://www.bestbuy.com/site/reviews/amd-ryzen-9-7900x-12-core-24-thread-4-7-ghz-5-6-ghz-max-boost-socket-am5-desktop-processor-silver/6519473?variant=A)
  2. **AMD - Ryzen 9 5900X 4th Gen 12-core, 24-threads Unlocked Desktop Processor Without Cooler - Black**
       [View](https://www.bestbuy.com/site/reviews/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler-black/6438942?variant=A)
  3. **AMD - Ryzen 5 7600X 6-core - 12-Thread 4.7GHz (5.3 GHz Max Boost) Socket AM5 Desktop Processor - Silver**
      [View](https://www.bestbuy.com/site/reviews/amd-ryzen-5-7600x-6-core-12-thread-4-7ghz-5-3-ghz-max-boost-socket-am5-desktop-processor-silver/6519479?variant=A)  
  4. **AMD - Ryzen 7 5800X 4th Gen 8-core, 16-threads Unlocked Desktop Processor Without Cooler - Black**
      [View](https://www.bestbuy.com/site/reviews/amd-ryzen-7-5800x-4th-gen-8-core-16-threads-unlocked-desktop-processor-without-cooler-black/6439000?variant=A)
  5.  **AMD - Ryzen 9 7950X3D 16-Core - 32-Thread 4.2 GHz (5.7 GHz Max Boost) Socket AM5 Unlocked Desktop Processor - Black**
      [View](https://www.bestbuy.com/site/reviews/amd-ryzen-9-7950x3d-16-core-32-thread-4-2-ghz-5-7-ghz-max-boost-socket-am5-unlocked-desktop-processor-black/6537138?variant=A)
## Graph
  ![alt text]("[CS325.png](https://github.com/Titankiller07/CS325Project1/blob/Project3/CS325.png)")
## Prerequisite
  Make sure you have Python installed I myself am using at this time Python 3.12.4 and have a basic understanding of python as well.
  Ollama is needed to make this work and phi 3 depending on what device you are using you may change how to intall which can be found [here](https://ollama.com/download)

## How to use Code
  If you are going to use this code you need to know a few things as well as need to set up the reqirments.
  1. You will need the reviews that were made from the webScrapping branch or a text file but each review needs to be one line.
  2. You can clone this repository following this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
  3. Then you can pull form the repository if you have trouble you might be able to just copy and paste the code if you have python and ollama installed and phi3 pulled or any ai model.
  4. You will also need to have multiple text files for the responses to be put in.
  5. This code uses phi3 but just needs one line changed if using another model but should run 
  
