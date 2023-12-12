import os
import json
import requests
from bs4 import BeautifulSoup
from aocd import get_data

day = 12
year = 2023

url = f"https://adventofcode.com/{year}/day/{day}"

with open(".scripts\cookies.json") as f:
    cookies = json.load(f)

response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')
    main_content = soup.find('main')

    # Format text for MD file
    md_content = f"""{main_content}"""

    # Save MD file
    with open(f"day_{day:02}/puzzle_text_day_{day:02}.md", "w") as f:
        f.write(md_content)
    
else:
    
    print('Error: Could not extract text from URL.')
    

data = get_data(session=cookies["session"] , day=day, year=year)

with open(f"day_{day:02}/input_day_{day:02}.txt", "w") as f:
    f.write(data)
