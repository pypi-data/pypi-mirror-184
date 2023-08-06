'''
Name: Code.
Author: Monarchdos
Date: 2023-01-06
'''
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    url = "https://api.ayfre.com/py.php?t=mon"
    res = requests.get(url)
    print(res.text)

def wcq():
    url = "https://api.ayfre.com/py.php?t=wcq"
    res = requests.get(url)
    print(res.text)

if __name__ == "__main__":
    main()