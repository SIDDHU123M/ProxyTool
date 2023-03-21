import requests
import time

url = 'https://api.proxyscrape.com/v2/online_check.php'

def check_api_status():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    try:
        response = requests.post(url, headers=headers, data={})
        if 'error' in response.text:
            return 'banned'
        elif 'Temporarily Banned' in response.text:
            return 'temporarily banned'
        else:
            return 'ok'
    except requests.exceptions.RequestException as e:
        print(f"Error while checking API status: {e}")
        return 'error'

# Check API status before running the code
api_status = check_api_status()
if api_status == 'banned':
    print("API is temporarily banned. Waiting for 5 minutes before trying again...")
    time.sleep(300)
elif api_status == 'temporarily banned':
    print("API is temporarily banned. Waiting for 5 minutes before trying again...")
    time.sleep(300)
else:
    working_proxies = []
    print("""
1. Https / Http
2. Socks4
3. Socks5""")
    inputt_filename = int(input("Which type of protocol you want to check: ")) # convert input to int
    if inputt_filename == 1:
        filename = "Https.txt"
    elif inputt_filename == 2:
        filename = "Socks4.txt"
    elif inputt_filename == 3:
        filename = "Socks5.txt"
    else:
        print("Invalid input. Exiting...")
        exit()

    with open(filename, 'r') as f:
        proxies = f.readlines()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://proxyscrape.com/',
        'Upgrade-Insecure-Requests': '1'
    }

    request_interval = 5 # in seconds
    max_requests_per_interval = 5
    requests_made = 0
    start_time = time.time()

    for proxy in proxies:
        proxy = proxy.strip()
        payload = {'ip_addr[]': [proxy]}

        if requests_made >= max_requests_per_interval:
            elapsed_time = time.time() - start_time
            if elapsed_time < request_interval:
                time.sleep(request_interval - elapsed_time)
            requests_made = 0
            start_time = time.time()

        try:
            response = requests.post(url, data=payload, headers=headers)
            print(f"{proxy}: {response.text}")
            if response.text.strip() == '1':
                working_proxies.append(proxy)
        except requests.exceptions.RequestException as e:
            print(f"Error while checking proxy {proxy}: {e}")
            continue

        requests_made += 1
        print("Total Requests Made : " , requests_made)
