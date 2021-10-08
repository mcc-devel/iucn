import parsed
import exceptions

def parse(s):
    mapped = {
        'type':0,
        'kingdom':1,
        'phylum':2,
        'class':3,
        'order':4,
        'family':5,
        'genus':6
    }
    res = s.split(' ')
    specified = ['Everything', 'Everything', 'Everything', 'Everything', 'Everything', 'Everything', 'Everything']
    i = 0
    j = len(res)-1
    if ':' in res[0]:
        while ':' in res[i] and i < len(res):
            ans = res[i].split(':')
            if len(ans) > 2:
                raise exceptions.wrongOptionError()
            else:
                if specified[mapped[ans[0]]] != 'Everything':
                    raise exceptions.multipleOptionsError(ans[0])
                else:
                    specified[mapped[ans[0]]] = ans[1].split(',')
            i = i + 1
    if ':' in res[len(res)-1]:
        while ':' in res[j] and j >= 0:
            ans = res[j].split(':')
            if len(ans) > 2:
                raise exceptions.wrongOptionError()
            else:
                if specified[mapped[ans[0]]] != 'Everything':
                    raise exceptions.multipleOptionsError(ans[0])
                else:
                    specified[mapped[ans[0]]] = ans[1].split(',')
            j = j - 1
    tgt = ''
    for k in range(i, j+1):
        if k != j:
            tgt = tgt + res[k] + ' '
        else:
            tgt = tgt + res[k]
    return parsed.parsed(specified[0], specified[1], specified[2], specified[3], specified[4], specified[5], specified[6], tgt)