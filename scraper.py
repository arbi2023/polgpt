import requests
from bs4 import BeautifulSoup
import json
import random
import time
from urllib.parse import urljoin


def scrape_quotes_with_pagination(base_url):
    quotes = []
    current_url = base_url
    while True:
        response = requests.get(current_url)
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.content, 'html.parser')
        quote_elements = soup.find_all('blockquote')
        for quote_element in quote_elements:
            quotes.append(quote_element.text.strip())
        
        pagination_link = soup.find('a', class_='pagination-prev')
        if pagination_link:
            current_url = urljoin(current_url, pagination_link['href'])  # Assumes absolute URL; adjust if relative
        else:
            break
        time.sleep(1)

    return quotes


def save_to_jsonl(quotes, filename):
    with open(filename, 'w+') as file:
        for quote in quotes:
            record = {"prompt": "", "completion": f"{quote}"}
            file.write(json.dumps(record) + '\n')

base_url = 'https://comemesuunaslavina.retrocog.org/'  # Replace with the actual base URL
quotes = scrape_quotes_with_pagination(base_url)
random.shuffle(quotes)
split_index = int(len(quotes) * 0.8)
training_quotes = quotes[:split_index]
validation_quotes = quotes[split_index:]
save_to_jsonl(training_quotes, './datasets/training_dataset.jsonl')
save_to_jsonl(validation_quotes, './datasets/validation_dataset.jsonl')
