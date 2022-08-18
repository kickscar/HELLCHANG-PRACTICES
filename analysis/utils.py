import ssl
import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(url='', encoding='utf-8', err=lambda e: print(f'{e} : {datetime.now()}', file=sys.stderr), *procs):
    try:
        request = Request(url)

        ssl._create_default_https_context = ssl._create_unverified_context
        response = urlopen(request)
        print(f'{datetime.now()}: success for request [{url}]')

        receive = response.read()
        return receive.decode(encoding, errors='replace')
    except Exception as e:
        err(e)


def clean_strings(strings, *funcs):
    results = []

    for string in strings:
        for func in funcs:
            string = func(string)

        results.append(string)

    return results


def filters(data, *procs):
    results = data

    for proc in procs:
        results = proc(results)

    return results