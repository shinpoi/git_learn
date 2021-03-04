# python3
# pip install requests[socks] beautifulsoup4

import requests as rq
from bs4 import BeautifulSoup

# https://www.wenku8.net/novel/2/12345/index.htm  --> aid = 12345
AID = '****'
URL = 'http://dl.wenku8.com/packtxt.php?aid={aid}&vid={vid}&charset=utf-8'

ss = rq.session()
ss.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

# comment out below line if you are not using proxy
ss.proxies = {'http':'socks5://127.0.0.1:10808', 'https':'socks5://127.0.0.1:10808'}

# get indices
r = ss.get('https://www.wenku8.net/novel/2/{}/index.htm'.format(AID))
soup = BeautifulSoup(r.content)
parts = soup.find_all('td', {'class':['vcss', 'ccss']})

# donwload list
pull_list = {}
for td in parts:
    # part
    if 'vcss' in td['class']:
        current_part = td.text
        pull_list[current_part] = []
        continue
    # chapter
    if td.find('a'):
        # (chapter name, vid)
        pull_list[current_part].append((td.text, td.find('a')['href']))

# download & write to file by part
for part in pull_list:
    part_name = part
    part_content = []
    print('going to download {}'.format(part_name))

    for chapter in pull_list[part]:
        chapter_name = chapter[0]
        vid = chapter[1].replace('.htm', '')
        print('  > {} ({})'.format(chapter_name, vid))
        r = ss.get(URL.format(aid=AID, vid=vid))
        if (r.status_code < 200) or (r.status_code > 300):
            raise RuntimeError('failed to get page {}-{} (vid: {})'.format(part_name, chapter_name, vid))
        # don't ask me why not utf-8 :(
        part_content.append(r.content.decode('utf-16le'))

    with open(part_name + '.txt', 'w') as f:
        f.write('\n'.join(part_content))
