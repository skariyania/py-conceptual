import threading
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


# Global variables for synchronization
lock = threading.Lock()
max_words = 0
total_words = 0

# Function to fetch and parse a webpage
def crawl_page(url):
    global max_words, total_words
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        words = len(soup.get_text().split())

        with lock:
            total_words += words
            max_words = max(max_words, words)

        print(f"URL: {url}, Words: {words}")

    except Exception as e:
        print(f"Error processing {url}: {str(e)}")

# Function to control the number of threads per host
def crawl_host(host, urls):
    threads = []
    for url in urls:
        while threading.active_count() >= 100 or threading.active_count(host) >= 5:
            pass  # Wait if the thread limit is reached

        thread = threading.Thread(target=crawl_page, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Main function to initiate crawling
def main():
    global max_words, total_words
    seed_urls = ["https://example.com/page1", "https://example.com/page2", "https://example2.com/page1"]

    # Extract hosts from seed URLs
    hosts = set(urlparse(url).hostname for url in seed_urls)

    # Create threads for each host
    for host in hosts:
        host_urls = [url for url in seed_urls if urlparse(url).hostname == host]
        thread = threading.Thread(target=crawl_host, args=(host, host_urls))
        thread.start()
        thread.join()

    print(f"Total words: {total_words}")
    print(f"Max words in a page: {max_words}")

if __name__ == "__main__":
    main()
