import concurrent.futures
import requests

# Lista di URL da richiedere
urls = [
    'https://api.github.com',
    'https://httpbin.org/ip',
    'https://httpbin.org/uuid',
    'https://httpbin.org/user-agent',
]

def fetch(url):
    try:
        response = requests.get(url)
        return response.status_code, response.json()
    except requests.RequestException as e:
        return e

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit tasks to the thread pool
        futures = [executor.submit(fetch, url) for url in urls]
        
        # Retrieve results as they complete
        for future in concurrent.futures.as_completed(futures):
            status, result = future.result()
            print(f"Status: {status}, Result: {result}")
    
    print("\n\nIT'S OVER!!")
if __name__ == "__main__":
    main()