import requests
import json

def getjson():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4541.0 Safari/537.36 Edg/93.0.932.0',
        'content-type': 'application/json; charset=UTF-8'
    }
    token = '9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee'
    tplist = ['DD/Data Deficient', 'LC/Least Concern', 'NT/Near Threatened', 'VU/Vulnerable', 'EN/Endangered', 'CR/Critically Endangered', 'EW/Extinct In The Wild', 'EX/Extinct']
    tpshort = ['DD', 'LC', 'NT', 'VU', 'EN', 'CR', 'EW', 'EX']
    tot = int(requests.get('http://apiv3.iucnredlist.org/api/v3/speciescount?token=%s'%(token), headers = headers).json()['count'])
    print('Got total')
    pgs = int(tot/10000)+1
    fin = [[], [], [], [], [], [], [], []]
    for i in range(pgs):
        rs = requests.get('http://apiv3.iucnredlist.org/api/v3/species/page/%s?token=%s'%(i, token)).json()['result']
        print('Got page %s'%(i+1))
        for elem in rs:
            for j in range(8):
                if elem['category'] == tpshort[j]:
                    if elem['main_common_name'] is not None:
                        fin[j].append({'sci':elem['scientific_name'], 'comm':elem['main_common_name'], 'level':tplist[j], 'level_short':tpshort[j], 'kingdom':elem['kingdom_name'], 'phylum':elem['phylum_name'], 'class':elem['class_name'], 'order':elem['order_name'], 'family':elem['family_name'], 'genus':elem['genus_name']})
                    else:
                        fin[j].append({'sci':elem['scientific_name'], 'comm':'None', 'level':tplist[j], 'level_short':tpshort[j], 'kingdom':elem['kingdom_name'], 'phylum':elem['phylum_name'], 'class':elem['class_name'], 'order':elem['order_name'], 'family':elem['family_name'], 'genus':elem['genus_name']})
        print('Completed page %s'%(i+1))
    for i in range(8):
        with open('%s.json'%(tpshort[i].lower()), 'w', encoding = 'utf-8') as f:
            json.dump(fin[i], f)