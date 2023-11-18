import re
import requests
from urllib.parse import urlparse, urlunparse

# Relevant HTTP response codes
relevant_codes = [301, 302, 307, 308]

def process_url(user_input):
    clean_url = re.sub(r"https?://|www\.", "", user_input)
    final_url = f"https://web.archive.org/cdx/search/cdx?url=*.{clean_url}&output=xml&fl=original&collapse=urlkey"

    try:
        response = requests.get(final_url, timeout=10)
        response.raise_for_status()
        filter_urls(response.text)
    except requests.RequestException as e:
        print(f"Error in fetching the URL: {e}")

def filter_urls(text):
    pattern = r"=http://|=http%3a%2|=https://|=https%3a%2"

    processed_bases = set()
    matching_urls = [line for line in text.splitlines() if re.search(pattern, line)]
    print(f"Number of URLs to process: {len(matching_urls)}")

    for line in matching_urls:
        parsed_url = urlparse(line)
        base_url = urlunparse(parsed_url._replace(params='', query='', fragment=''))

        if base_url not in processed_bases:
            processed_bases.add(base_url)
            try:
                response = requests.get(line, timeout=10, allow_redirects=False)
                if response.status_code in relevant_codes:
                    print(f"Open redirect found: {line}")
            except requests.RequestException:
                pass

# Example usage
user_input = input("What is the URL you would like to check?: ")
process_url(user_input)
