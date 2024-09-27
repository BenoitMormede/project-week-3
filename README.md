# project-week-3
Benoît &amp; Olivier

Readme fileREADME file with the following structure:30 Years of movies data exploration
The project aims at providing data exploration insights on 30 years of movies with data aggregation and visual displays
Data used:

* start with a CSV file from Kaggle list all movies for the 20th & 21st Centuries
* enriched initial dataframe with API calls on OMDB
* web scraping on IMDB database for worldwide Gross Revenue


Questions you want to answer : 

* Growth dynamic of the movie market (historical graph #movies / year)
* Which countries are the top contributors in movie production (top10 bar chart #movies cummulated 30 years)
* Which movies were most profitable (
* Top 5 movies gross revenue by genre
* Top 5 highest grossing directors
* Correlation average score / gross revenue
* Correlation average score / imdb votes (popularity)
* Correlation nominations / imdb votes (popularity) + gross revenue
* Correlation wins / imdb votes (popularity) + gross revenue
* Correlation rated / budget (+revenue ?)

Describe the methodology:

* created 2 dataframes: one from the csv file and a second one from API calls to OMDB data base
* merged the 2 data frames
* added the worldwide gross revenue in a new column to the merged dataframe
* Cleaning operations on merged dataframe
    * renamed / streamlined header columns
    * converted rating and revenue columns in numeric format
    * parsed "awards" column (string) into # of awards and # of nominations in integer format
    * created an average score based on metacritic and Imdb scores handling null values
    * mapped the "rated" columns into main categories


Conclusions after your analysis:

Further questions:

* Even when passed with a list of unique values for "Title" the API returned a few duplicates
* After analysis the duplicates are strictly the same for values in all columns


EDA

* Summary statistics => filter and aggregations
* Visualisation
* Relationships / correlation



* Teamwork & Project Management (1 slide) 
* Did you follow your workflow plan or did you add something after starting the project?
    * globally we followed our plan
    * vital piece of info was missing in original df (worlwide gross product) => web scraping IMDB 
* What worked well in your teamwork and what could be improved?
    * Good communication
    * Good balance of skills
* Did you think about the risk management?
    * anticipation of web scraping lenghty process (7000 calls => x hours)
    * maximum number of daily request authorized for API

Major Obstacle (1-2 slides): 

* Discuss the biggest obstacle or mistake you encountered during this project.
    * difficulty in chosing a topic and finding an adequate API with enough data
    * parsing text to extract data is challenging w/o mastering Regex 
* Share what you learned from it and how it influenced your project.
    * Data is the new currency!! (Imdb full API access = 400 K$)
    * Easier to work and perform meaningful analysis with data you have an interest for
    * Avoid passing duplicates values to the API when making a large amount of queries
* Is there anything you would do differently in hindsight?
    * Sequencing & structure of the code (focus on API and scraping first then cleaning the merged dataframe)

