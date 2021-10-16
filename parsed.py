class parsed:
    def __init__(this, tpe:str, kim:str, phm:str, cls:str, orr:str, fay:str, ges:str, tgt:str):
        ev = 'Everything'
        if tpe == ev or tpe == ev.lower():
            this.type = ev
        else:
            for i in range(len(tpe)):
                tpe[i] = tpe[i].lower()
            this.type = tpe
        if kim == ev or kim == ev.lower():
            this.kingdom = ev
        else:
            for i in range(len(kim)):
                kim[i] = kim[i].lower()
            this.kingdom = kim
        if phm == ev or phm == ev.lower():
            this.phylum = ev
        else:
            for i in range(len(phm)):
                phm[i] = phm[i].lower()
            this.phylum = phm
        if cls == ev or cls == ev.lower():
            this.classs = ev
        else:
            for i in range(len(cls)):
                cls[i] = cls[i].lower()
            this.classs = cls
        if orr == ev or orr == ev.lower():
            this.order = ev
        else:
            for i in range(len(orr)):
                orr[i] = orr[i].lower()
            this.order = orr
        if fay == ev or fay == ev.lower():
            this.family = ev
        else:
            for i in range(len(fay)):
                fay[i] = fay[i].lower()
            this.family = fay
        if ges == ev or ges == ev.lower():
            this.genus = ev
        else:
            for i in range(len(ges)):
                ges[i] = ges[i].lower()
            this.genus = ges
        this.targett = tgt

class oldtype:
    def __init__(self, ascomm:bool, assci:bool, pars:parsed):
        self.iscomm = ascomm
        self.issci = assci
        self.parst = pars

class searchresult:
    def __init__(self, res:list):
        self.result = res