import json
import iucn_getmore
from requests import get

def fastref()->None:
    nms:list = ['dd', 'lc', 'nt', 'vu', 'en', 'cr', 'ew', 'ex']
    headers:dict = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4541.0 Safari/537.36 Edg/93.0.932.0',
        'content-type': 'application/json; charset=UTF-8'
    }
    for nm in nms:
        rs:list = get('https://raw.fastgit.org/mcc-devel/iucn/main/%s.json' % nm, headers = headers).json()
        with open('%s.json' % nm, 'w', encoding = 'utf-8') as f:
            json.dump(rs, f)

def slowref()->None:
    iucn_getmore.getjson()