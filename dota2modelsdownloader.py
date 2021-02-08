#!/usr/bin/env python3

import os
import sys
import requests
from bs4 import BeautifulSoup


def download_all(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    download_page_url_pattern = 'http://media.steampowered.com/apps/dota2/workshop/{}.zip?v=6350872'
    source_page_url = 'http://www.dota2.com/workshop/requirements'
    source_page_html = requests.get(source_page_url, headers = {'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6'})
    bs = BeautifulSoup(source_page_html.text, 'lxml')
    data = bs.select('#hero_table > tr > td > a')
    for a in data:
        href = a.get('href')
        zip_name = href.rsplit('/', 1)[1]
        dest_name = dest_path + '/' + zip_name + '-' + a.get_text() + '.zip'
        r = requests.get(download_page_url_pattern.format(zip_name))
        with open(dest_name, 'wb') as f:
            f.write(r.content)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: dota2modelsdownloader dest_path')
    download_all(sys.argv[1])