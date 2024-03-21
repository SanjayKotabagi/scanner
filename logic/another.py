import requests
import json
from prettytable import PrettyTable
from apikeys import *
import time
import urllib.parse

pt = PrettyTable()


def get_detailed_data(data):
    results = [
    ["Score", data["verdicts"]["overall"]["score"]],
    ["Categories", data["verdicts"]["overall"]["categories"] if data["verdicts"]["overall"]["categories"] else "No Category"],
    ["Malicious", data["verdicts"]["engine"]["malicious"] if data["verdicts"]["overall"]["categories"] else "No Malicious Score"],
    ["Screenshot", data["task"]["screenshotURL"]],
    ["DOM URL", data["task"]["domURL"]]
    ]
    return results

    

def get_url_reports(urls):
    for url in urls:
        res = url_scan_res(url)
        res2 = url_qual(url)
    return res,res2

def url_scan_res(url):
    headers = {'API-Key':urlscan_api,'Content-Type':'application/json'}
    data = {"url": url, "visibility": "private"}
    res = []
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    data = response.json()
    if data.get('result', 'Error') != "Error":
        ur = ["URL : ", data.get('url')]
        url_rep = ["URL Report : ", data.get('result')]
        res.extend([ur])
        res.extend([url_rep])
        api_uri = data.get('api')
        time.sleep(10)
        api_uri = requests.get(api_uri)
        json_data = api_uri.json()
        d_res = get_detailed_data(json_data)
        res.extend(d_res)
    else:
        res = data.get('message'), data.get('description')
    return res

def url_qual(url_to_scan):
    encoded_url = urllib.parse.quote_plus(url_to_scan)
    endpoint = f'https://www.ipqualityscore.com/api/json/url/{url_qual_api}/{encoded_url}'
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        results = [
        ["Results for", url_to_scan],
        ["Safe", not data["unsafe"]],
        ["IP Addr", data["ip_address"]],
        ["Age", f"{data['domain_age']['human']} , {data['domain_age']['iso']}"],
        ["Phishing", data["phishing"]],
        ["Malware", data["malware"]],
        ["Suspicious", data["suspicious"]],
        ["Risk Score", data["risk_score"]],
        ["Page Title", data["page_title"]],
        ["Mx Records", ', '.join(data["mx_records"])],
        ["Categories", data["category"]]
        ]
    else:
        results = ["Error:", response.text]
    return results

def get_reports(urls):
    urlscanreport = get_url_reports(urls)
    pt.add_rows(urlscanreport)
    return pt

get_reports(["7blue.in"])


