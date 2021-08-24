from fuzzywuzzy import fuzz
import json

ddi = []
lci = []
nti = []
vui = []
eni = []
cri = []
ewi = []
exi = []
anss = []
ansc = []

def openf():
    global ddi
    global lci
    global nti
    global vui
    global eni
    global cri
    global ewi
    global exi
    with open('dd.json', 'r') as f:
        ddi = json.load(f)
    with open('lc.json', 'r') as f:
        lci = json.load(f)
    with open('nt.json', 'r') as f:
        nti = json.load(f)
    with open('vu.json', 'r') as f:
        vui = json.load(f)
    with open('en.json', 'r') as f:
        eni = json.load(f)
    with open('cr.json', 'r') as f:
        cri = json.load(f)
    with open('ew.json', 'r') as f:
        ewi = json.load(f)
    with open('ex.json', 'r') as f:
        exi = json.load(f)

def calculate(target):
    global anss
    global ansc
    #stores as (score, sciname, comname, level, notice)
    for elem in ddi:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    for elem in lci:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    for elem in nti:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    for elem in vui:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    for elem in eni:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    for elem in cri:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    for elem in ewi:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    for elem in exi:
        anss.append((fuzz.UWRatio(elem['sci'], target, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
        ansc.append((fuzz.partial_token_sort_ratio(elem['comm'], target, force_ascii = False, full_process = False), elem['sci'], elem['comm'], elem['level'], elem['notice']))
    anss.sort(key = lambda elem:elem[0], reverse = True)
    ansc.sort(key = lambda elem:elem[0], reverse = True)

def search(target, aus):
    openf()
    calculate(target)
    print('First, the results accoring to scientific names')
    for elem in anss:
        flag = False
        for us in aus:
            if elem[1] == us:
                flag = True
                break
        if flag == True:
            continue
        res = input('Is your desired species %s (scientific name)/%s (common name) with match score %s (y/n, s to skip the rest (without flagging as searched)): ' % (elem[1], elem[2], elem[0])).lower()
        if res == 'y':
            print('\n', end = '')
            print('Information below:')
            print('Scientific name: %s' % elem[1])
            print('Common name: %s' % elem[2])
            print('Danger level: %s' % elem[3])
            print('A note for you: %s' % elem[4])
            print('\n', end = '')
            aus.append(elem[1])
            return (True, aus)
        elif res == 'n':
            aus.append(elem[1])
        elif res == 's':
            break
    print('Then, the results accoring to common names')
    for elem in ansc:
        flag = False
        for us in aus:
            if elem[1] == us:
                flag = True
                break
        if flag == True:
            continue
        res = input('Is your desired species %s (scientific name)/%s (common name) with match score %s (y/n, s to skip the rest (without flagging as searched)): ' % (elem[1], elem[2], elem[0])).lower()
        if res == 'y':
            print('\n', end = '')
            print('Information below:')
            print('Scientific name: %s' % elem[1])
            print('Common name: %s' % elem[2])
            print('Danger level: %s' % elem[3])
            print('A note for you: %s' % elem[4])
            print('\n', end = '')
            aus.append(elem[1])
            return (True, aus)
        elif res == 'n':
            aus.append(elem[1])
        elif res == 's':
            break
    return (False, aus)