import requests
import csv

headers = {
    'authority': 'www.list.am',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.list.am/category/60',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}


def get_list_ad_price(list_url, headers):
    print(list_url)
    response = requests.get(list_url, headers=headers)
    html = response.text
    if 'id="xprice"' in html:
        return html.split('id="xprice"')[1].split("span>")[1].split("<")[0].replace(",", "")
    return None


def get_list_category_urls(category_url, headers):
    list_urls = []
    response = requests.get(category_url, headers=headers)
    html = response.text
    for i in html.split('<a href="'):
        url = "https://www.list.am" + i.split('">')[0].replace('" class="h', '')
        if "/item" in url:
            list_urls.append(url)
    return list_urls


category_url = "https://www.list.am/category/23"

list_urls = get_list_category_urls(category_url, headers)
list_prices = []
for list_url in list_urls:
    list_prices.append(
        {
            "price": get_list_ad_price(list_url, headers),
            "url": list_url
        }
    )

with open('ListPricesCars.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["url", "price"])
    writer.writeheader()
    writer.writerows(list_prices)
