import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from time import sleep


def get_data_from_rate():
    cookies = {
        'ASP.NET_SessionId': 'pex4ltra0y34kkncerwftw55',
        '__utma': '128827151.384477387.1695110688.1695110688.1695110688.1',
        '__utmb': '128827151.1.10.1695110688',
        '__utmc': '128827151',
        '__utmz': '128827151.1695110688.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        'drift_campaign_refresh': 'c8f7e8cb-3453-48f3-a0cb-7b2f46a8a068',
        '_ym_uid': '1695110691619172842',
        '_ym_d': '1695110691',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'drift_aid': '7ba36bf2-83cb-4b2b-b44c-97598d20f43b',
        'driftt_aid': '7ba36bf2-83cb-4b2b-b44c-97598d20f43b',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        # 'Cookie': 'ASP.NET_SessionId=pex4ltra0y34kkncerwftw55; __utma=128827151.384477387.1695110688.1695110688.1695110688.1; __utmb=128827151.1.10.1695110688; __utmc=128827151; __utmz=128827151.1695110688.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; drift_campaign_refresh=c8f7e8cb-3453-48f3-a0cb-7b2f46a8a068; _ym_uid=1695110691619172842; _ym_d=1695110691; _ym_isad=2; _ym_visorc=b; drift_aid=7ba36bf2-83cb-4b2b-b44c-97598d20f43b; driftt_aid=7ba36bf2-83cb-4b2b-b44c-97598d20f43b',
        'Upgrade-Insecure-Requests': '1',
    }

    response = requests.get('http://rate.am/', cookies=cookies, headers=headers)
    return response.text


def get_banks_data(html):
    soup = BeautifulSoup(html)
    table = soup.find("table", {"id": "rb"})
    trs = table.find_all("tr")[2:-5]
    banks = {}
    for tr in trs:
        tds = tr.find_all("td")
        bank_name = tds[1].text.strip()
        banks[bank_name] = {}
        banks[bank_name]["USD"] = {"Arq": tds[5].text, "Vacharq": tds[6].text}
        banks[bank_name]["EUR"] = {"Arq": tds[7].text, "Vacharq": tds[8].text}
        banks[bank_name]["RUB"] = {"Arq": tds[9].text, "Vacharq": tds[10].text}
        banks[bank_name]["GBP"] = {"Arq": tds[11].text, "Vacharq": tds[12].text}
    return banks


while True:
    html = get_data_from_rate()
    banks = get_banks_data(html)
    with open("rate_data.json", "w") as file:
        json.dump(banks, file)
    sleep(10*60)
