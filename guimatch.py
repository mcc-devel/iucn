import json
import fcheck
import parsed

ddi:list = []
lci:list = []
nti:list = []
vui:list = []
eni:list = []
cri:list = []
ewi:list = []
exi:list = []

def finded(a:tuple, b:list)->bool:
    for elem in b:
        if (elem[0].lower(), elem[1].lower(), elem[2].lower(), elem[3].lower(), elem[4].lower(), elem[5].lower(), elem[6].lower(), elem[7].lower(), elem[8].lower(), elem[9].lower()) == (a[0].lower(), a[1].lower(), a[2].lower(), a[3].lower(), a[4].lower(), a[5].lower(), a[6].lower(), a[7].lower(), a[8].lower(), a[9].lower()):
            return True
    return False

def openf(aserr:bool)->None:
    fcheck.doFileExistanceCheck(aserr)
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

def calculate(aserr:bool, iscomm:bool, issci:bool, opts:parsed.parsed):
    target:str = opts.targett
    openf(aserr)
    #stores as (sciname, comname, level, notice)
    ans:list = []
    flag:bool = False
    if len(target.split(' ')) > 1:
        flag = True
    tgetlst:list = []
    found:list = []
    pos:dict = {}
    if flag == True:
        tgetlst = target.split(' ')
        for i in range(0, len(tgetlst)):
            tgetlst[i] = tgetlst[i].lower()
        for i in range(0, len(tgetlst)+1):
            found.append(0)
        for i in range(0, len(tgetlst)):
            pos[tgetlst[i]] = i+1
    for elem in ddi:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in lci:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in nti:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in vui:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in eni:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in cri:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in ewi:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in exi:
        wordlst = []
        if issci == True:
            wordlst = wordlst + elem['sci'].split(' ')
        if iscomm == True:
            wordlst = wordlst + elem['comm'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            elif flag == True and word.lower() != target.lower():
                try:
                    if(pos[word.lower()] > 0):
                        found[pos[word.lower()]] += 1
                except KeyError:
                    pass
        if flag == True:
            tmp = True
            for i in range(1, len(tgetlst)+1):
                if found[i] == 0:
                    tmp = False
                    break
            if tmp == True:
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['kingdom'], elem['phylum'], elem['class'], elem['order'], elem['family'], elem['genus'], elem['level_short']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    ans.sort(key = lambda elem:elem[1])
    actans = []
    ev = 'Everything'
    for elem in ans:
        if opts.type != ev and elem[9].lower() not in opts.type:
            continue
        if opts.kingdom != ev and elem[3].lower() not in opts.kingdom:
            continue
        if opts.phylum != ev and elem[4].lower() not in opts.phylum:
            continue
        if opts.classs != ev and elem[5].lower() not in opts.classs:
            continue
        if opts.order != ev and elem[6].lower() not in opts.order:
            continue
        if opts.family != ev and elem[7].lower() not in opts.family:
            continue
        if opts.genus != ev and elem[8].lower() not in opts.genus:
            continue
        if not finded(elem, actans):
            actans.append(elem)
    return actans