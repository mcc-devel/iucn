import exceptions
import os

flist:list = ['dd.json', 'lc.json', 'nt.json', 'vu.json', 'en.json', 'cr.json', 'ew.json', 'ex.json']

def doFileExistanceCheck(aserr:bool)->None:
    for elem in flist:
        try:
            f = open(elem, 'x')
            f.close()
        except FileExistsError:
            pass
        else:
            os.system('rm -rf %s' % elem)
            if aserr == False:
                raise exceptions.fileNotFoundWarning(elem)
            else:
                raise exceptions.fileNotFoundError(elem)