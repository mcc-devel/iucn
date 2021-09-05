import json
import fcheck

ddi = []
lci = []
nti = []
vui = []
eni = []
cri = []
ewi = []
exi = []

def openf(aserr):
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

def calculate(target, aserr, assci):
    openf(aserr)
    #stores as (sciname, comname, level, notice)
    ans = []
    flag = False
    if len(target.split(' ')) > 1:
        flag = True
    tgetlst = []
    found = []
    pos = {}
    wordlst = []
    if flag == True:
        tgetlst = target.split(' ')
        for i in range(0, len(tgetlst)):
            tgetlst[i] = tgetlst[i].lower()
        for i in range(0, len(tgetlst)+1):
            found.append(0)
        for i in range(0, len(tgetlst)):
            pos[tgetlst[i]] = i+1
    for elem in ddi:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in lci:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in nti:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in vui:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in eni:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in cri:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in ewi:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    for elem in exi:
        if assci == False:
            wordlst = elem['comm'].split(' ')
        else:
            wordlst = elem['sci'].split(' ')
        for word in wordlst:
            if flag == False and word.lower() == target.lower():
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
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
                ans.append((elem['sci'], elem['comm'], elem['level'], elem['notice']))
            for i in range(0, len(tgetlst)+1):
                found[i] = 0
    ans.sort(key = lambda elem:elem[1])
    actans = []
    for elem in ans:
        if elem not in actans:
            actans.append(elem)
    return actans