import json
import requests

def getjson():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4541.0 Safari/537.36 Edg/93.0.932.0',
        'content-type': 'application/json; charset=UTF-8'
    }
    # Payloads
    # Real info
    dd = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["dd"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Data Deficient
    lc = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["lc"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Least Concern
    nt = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["nt"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Near Threatened
    vu = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["vu"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Vulnerable
    en = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["en"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Endangered
    cr = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["cr"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Critically Endangered
    ew = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["ew"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Extinct In The Wild
    ex = '''{"stored_fields":["hasImage","hasPoints","hasRanges","image.id","image.url","image.urlThumb","image.credit","scopes.id","scopes.code","scopes.jsonDescription","kingdomName","className","commonName","scientificName","sisTaxonId","redListCategory.scaleCode","redListCategory.order","redListCategory.code","redListCategory.jsonDescription","populationTrend.id","populationTrend.code","populationTrend.jsonDescription"],"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["ex"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}},"should":[{"term":{"hasImage":{"value":true,"boost":6}}}]}},"sort":[{"_score":{"order":"desc"}}]}'''  # Extinct
    # Info count
    ddc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["dd"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Data Deficient
    lcc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["lc"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Least Concern
    ntc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["nt"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Near Threatened
    vuc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["vu"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Vulnerable
    enc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["en"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Endangered
    crc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["cr"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Critically Endangered
    ewc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["ew"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Extinct In The Wild
    exc = '''{"aggs":{"list":{"terms":{"field":"measuresUpToRoots","size":100000,"min_doc_count":0}}},"query":{"bool":{"must":[],"filter":{"bool":{"filter":[{"terms":{"scopes.code":["1"]}},{"terms":{"redListCategory.scaleCode":["ex"]}},{"terms":{"taxonLevel":["Species"]}}],"should":[],"minimum_should_match":0}}}}}'''  # Extinct
    link1 = r'https://www.iucnredlist.org/dosearch/assessments/_search?size=0&_source_excludes=ranges%2C%20legends&track_total_hits=true'
    # place1 = hits/total/value
    # link2 = r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % ${...}
    # place2 = hits/hits/0~xxx/fields/{commonName, scientificName}/0
    # method = requests.post(link{1, 2}, data = {...}, headers = headers);
    # Info count
    ddcc = requests.post(link1, data=ddc, headers=headers).json()['hits']['total']['value']
    lccc = requests.post(link1, data=lcc, headers=headers).json()['hits']['total']['value']
    ntcc = requests.post(link1, data=ntc, headers=headers).json()['hits']['total']['value']
    vucc = requests.post(link1, data=vuc, headers=headers).json()['hits']['total']['value']
    encc = requests.post(link1, data=enc, headers=headers).json()['hits']['total']['value']
    crcc = requests.post(link1, data=crc, headers=headers).json()['hits']['total']['value']
    ewcc = requests.post(link1, data=ewc, headers=headers).json()['hits']['total']['value']
    excc = requests.post(link1, data=exc, headers=headers).json()['hits']['total']['value']
    # Real info
    ddi = []
    lci = []
    nti = []
    vui = []
    eni = []
    cri = []
    ewi = []
    exi = []
    ddii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % ddcc, data=dd, headers=headers).json()['hits']['hits']
    lcii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % lccc, data=lc, headers=headers).json()['hits']['hits']
    ntii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % ntcc, data=nt, headers=headers).json()['hits']['hits']
    vuii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % vucc, data=vu, headers=headers).json()['hits']['hits']
    enii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % encc, data=en, headers=headers).json()['hits']['hits']
    crii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % crcc, data=cr, headers=headers).json()['hits']['hits']
    ewii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % ewcc, data=ew, headers=headers).json()['hits']['hits']
    exii = requests.post(r'https://www.iucnredlist.org/dosearch/assessments/_search?size=%s&_source=false&from=0&track_total_hits=true' % excc, data=ex, headers=headers).json()['hits']['hits']

    for elem in ddii:
        try:
            ddi.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Data Deficient', 'notice': '''We don't have enough data to determine the species' status.'''})
        except KeyError:
            ddi.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Data Deficient', 'notice': '''We don't have enough data to determine the species' status.'''})
    for elem in lcii:
        try:
            lci.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Least Concern', 'notice': '''This species is perfectly fine.'''})
        except KeyError:
            lci.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Least Concern', 'notice': '''This species is perfectly fine.'''})
    for elem in ntii:
        try:
            nti.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Near Threatened', 'notice': '''This species might be threatened in the future, protect it!'''})
        except KeyError:
            nti.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Near Threatened', 'notice': '''This species might be threatened in the future, protect it!'''})
    for elem in vuii:
        try:
            vui.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Vulnerable', 'notice': '''This species is at risk of extinction, protect it!'''})
        except KeyError:
            vui.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Vulnerable', 'notice': '''This species is at risk of extinction, protect it!'''})
    for elem in enii:
        try:
            eni.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Endangered', 'notice': '''This species is at high risk of extinction, protect it!'''})
        except KeyError:
            eni.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Endangered', 'notice': '''This species is at high risk of extinction, protect it!'''})
    for elem in crii:
        try:
            cri.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Critically Endangered', 'notice': '''This species is at very high risk of extinction, protect it!'''})
        except KeyError:
            cri.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Critically Endangered', 'notice': '''This species is at very high risk of extinction, protect it!'''})
    for elem in ewii:
        try:
            ewi.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Extinct In The Wild', 'notice': '''This species is already extinct in the wild.'''})
        except KeyError:
            ewi.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Extinct In The Wild', 'notice': '''This species is already extinct in the wild.'''})
    for elem in exii:
        try:
            exi.append({'sci': elem['fields']['scientificName'][0], 'comm': elem['fields']['commonName'][0], 'level': 'Extinct', 'notice': '''Sorry, this species is already extinct.'''})
        except KeyError:
            exi.append({'sci': elem['fields']['scientificName'][0], 'comm': 'None', 'level': 'Extinct', 'notice': '''Sorry, this species is already extinct.'''})
    with open('dd.json', 'w', encoding='utf-8') as f:
        json.dump(ddi, f)
    with open('lc.json', 'w', encoding='utf-8') as f:
        json.dump(lci, f)
    with open('nt.json', 'w', encoding='utf-8') as f:
        json.dump(nti, f)
    with open('vu.json', 'w', encoding='utf-8') as f:
        json.dump(vui, f)
    with open('en.json', 'w', encoding='utf-8') as f:
        json.dump(eni, f)
    with open('cr.json', 'w', encoding='utf-8') as f:
        json.dump(cri, f)
    with open('ew.json', 'w', encoding='utf-8') as f:
        json.dump(ewi, f)
    with open('ex.json', 'w', encoding='utf-8') as f:
        json.dump(exi, f)