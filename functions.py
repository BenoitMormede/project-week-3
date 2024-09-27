import pandas as pd

# Function to fetch movie data from the OMDB API

def fetch_movie_data(title):
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

#import re
# Function to extract wins and nominations from the awards string
def extract_awards_info(awards_str):
    if pd.isna(awards_str) or "No awards" in awards_str:
        return 0, 0
    wins = 0
    nominations = 0

    # Find wins using regex
    win_match = re.search(r'(\d+)\s+win', awards_str)
    if win_match:
        wins = int(win_match.group(1))

    # Find nominations using regex
    nomination_match = re.search(r'(\d+)\s+nomination', awards_str)
    if nomination_match:
        nominations = int(nomination_match.group(1))

    # Handle cases like "Won 3 Oscars", "Won 1 Golden Globe", etc.
    special_wins = re.findall(r'Won\s+(\d+)\s+[\w\s]+\.?', awards_str)
    if special_wins:
        wins += sum(int(win) for win in special_wins)

    return wins, nominations

import numpy as np

# Create a function to compute the aggregated score
def compute_aggregated_score(row):
    # Check if both 'imdb_rating' and 'metascore' are not NaN
    if not pd.isna(row['imdb_rating']) and not pd.isna(row['metascore']):
        # Take the mean of 'imdb_rating' and 'metascore' (dividing 'metascore' by 10 to bring it to the same scale)
        return (row['imdb_rating'] + row['metascore']) / 2
    # If only 'imdb_rating' is available
    elif not pd.isna(row['imdb_rating']):
        return row['imdb_rating']
    # If only 'metascore' is available (divided by 10 to match the scale)
    elif not pd.isna(row['metascore']):
        return row['metascore']
    # If both are NaN, return NaN
    else:
        return np.nan

    
import requests
from bs4 import BeautifulSoup

# Define a function to scrape the cumulative worldwide gross from the IMDB page
def scrape_gross(imdb_id):
    url = f"https://www.imdb.com/title/{imdb_id}/"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(f"Success: {imdb_id} returned status 200")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        gross_worldwide = soup.find('li', {'data-testid': 'title-boxoffice-cumulativeworldwidegross'})
        
        if gross_worldwide:
            gross_value = gross_worldwide.find('span', class_='ipc-metadata-list-item__list-content-item').text
            return gross_value
        else:
            return None
    else:
        print(f"Failed: {imdb_id} returned status {response.status_code}")
        return None
    
import ast

def clean_column_data(col):
    # Try to safely evaluate the string, remove extra brackets and escape characters
    try:
        return str(ast.literal_eval(col)).replace("\\", "").replace("[", "").replace("]", "").replace("'", "").replace('"', '').strip()
    except:
        # In case of evaluation issues, return the original but cleaned version
        return str(col).replace("\\", "").replace("[", "").replace("]", "").replace("'", "").replace('"', '').strip()