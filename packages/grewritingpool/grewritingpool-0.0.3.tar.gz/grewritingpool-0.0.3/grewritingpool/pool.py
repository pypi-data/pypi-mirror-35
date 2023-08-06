#!/usr/bin/env python3

import sys
import getopt
import json
import requests
from bs4 import BeautifulSoup as bs
from bs4 import element

def fetch_pool(writing_type):
    base_req = requests.get("https://www.ets.org/gre/revised_general/prepare/analytical_writing/"+writing_type+"/pool")
    base_req.encoding = 'utf-8'
    base_res = base_req.text
    base_soup = bs(base_res,'lxml')

    pool = []
    first_seperator = (base_soup.select("div.divider-50"))[0]
    status = 1
    tmp = {}
    for item in first_seperator.next_siblings:
        if isinstance(item,element.NavigableString):
            continue
        elif repr(item).startswith("<h2>"):
            break
        elif status == 1 and item.name == "p":
            tmp['first']  = item.contents[0]
            status = 2
        elif status == 2 and item.name == "p":
            tmp['second'] = item.contents[0]
            status = 2
        elif status == 2 and item.name == "div":
            status = 3
            tmp["instru"] = item.contents[1].contents[0]
        elif status == 3 and item.name == "div":
            pool.append(tmp)
            tmp = {}
            status = 1
    return json.dumps(pool)

def download_pool(writing_type):
    print("Downloading GRE "+writing_type+" Pool...")
    base_req = requests.get("https://www.ets.org/gre/revised_general/prepare/analytical_writing/"+writing_type+"/pool")
    base_req.encoding = 'utf-8'
    base_res = base_req.text
    base_soup = bs(base_res,'lxml')

    pool = []
    topiccount=0
    first_seperator = (base_soup.select("div.divider-50"))[0]
    status = 1
    tmp = {}
    for item in first_seperator.next_siblings:
        if isinstance(item,element.NavigableString):
            continue
        elif repr(item).startswith("<h2>"):
            break
        elif status == 1 and item.name == "p":
            tmp['first']  = item.contents[0]
            status = 2
        elif status == 2 and item.name == "p":
            tmp['second'] = item.contents[0]
            status = 2
        elif status == 2 and item.name == "div":
            status = 3
            tmp["instru"] = item.contents[1].contents[0]
        elif status == 3 and item.name == "div":
            pool.append(tmp)
            tmp = {}
            status = 1
            topiccount = topiccount + 1
            print("Fetch "+writing_type+" Topic "+str(topiccount)+" Completed.")
    with open(writing_type+'.json', 'w') as outfile:
        json.dump(pool, outfile)
    print("Written "+str(topiccount)+" topics to "+writing_type+".json.\n")

def fetch_type(fet):
    try:
        if fet in ("issue", "argument"):
            return fetch_pool(fet)
        else:
            raise ValueError("Invalid Fetch Type "+fet+".")
    except ValueError as err:
        print(err.args)

def download_type(fet):
    try:
        if fet in ("issue", "argument"):
            download_pool(fet)
        elif fet == "all":
            download_pool("issue")
            download_pool("argument")
        else:
            raise ValueError("Invalid Fetch Type "+fet+".")
    except ValueError as err:
        print(err.args)

def main(args):
    if len(args) == 1:
        if args[0] in ("-h", "--help"):
            print("grewritingpool.py [all|issue|argument]")
            sys.exit()
        else:
            download_pool(args[0])
    else:
        print("grewritingpool.py [all|issue|argument]")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])