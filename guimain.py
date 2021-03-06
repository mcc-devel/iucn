from typing import *
import exceptions
from tkinter import *
from tkinter import messagebox
import guimatch
import refresh
import parser
import parsed

warnAsError:bool = False
old:parsed.oldtype = parsed.oldtype(False, False, parser.parse(''))
results:parsed.searchresult = parsed.searchresult([])

def warnAsErr()->None:
    global warnAsError
    if messagebox.askyesno(title = 'Warnings as Errors?', message = 'Do you want to treat all warning as errors?'):
        warnAsError = True
        print('All warnings shall be treated as errors now')

def selectcallback(res:Any)->None:
    res:str = schlst.index(ACTIVE)
    if results.result[res][1] != 'None':
        messagebox.showinfo(title = 'Details about %s' % results.result[res][1], message = '''Scientific name: %s

Common name: %s

Danger level: %s

Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        if messagebox.askyesno(title = 'Copy?', message = 'Copy to clipboard?'):
            frame.clipboard_clear()
            frame.clipboard_append('''Scientific name: %s
Common name: %s
Danger level: %s
Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        frame.update()
        return
    else:
        messagebox.showinfo(title = 'Details about %s' % results.result[res][0], message = '''Scientific name: %s

Common name: %s

Danger level: %s

Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        if messagebox.askyesno(title = 'Copy?', message = 'Copy to clipboard?'):
            frame.clipboard_clear()
            frame.clipboard_append('''Scientific name: %s
Common name: %s
Danger level: %s
Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        frame.update()
        return

def sciselectcallback(res:Any)->None:
    res:str = schscilist.index(ACTIVE)
    if results.result[res][1] != 'None':
        messagebox.showinfo(title = 'Details about %s' % results.result[res][1], message = '''Scientific name: %s

Common name: %s

Danger level: %s

Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        if messagebox.askyesno(title = 'Copy?', message = 'Copy to clipboard?'):
            frame.clipboard_clear()
            frame.clipboard_append('''Scientific name: %s
Common name: %s
Danger level: %s
Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        frame.update()
        return
    else:
        messagebox.showinfo(title = 'Details about %s' % results.result[res][0], message = '''Scientific name: %s

Common name: %s

Danger level: %s

Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        if messagebox.askyesno(title = 'Copy?', message = 'Copy to clipboard?'):
            frame.clipboard_clear()
            frame.clipboard_append('''Scientific name: %s
Common name: %s
Danger level: %s
Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (results.result[res][0], results.result[res][1], results.result[res][2], results.result[res][3], results.result[res][4], results.result[res][5], results.result[res][6], results.result[res][7], results.result[res][8]))
        frame.update()
        return

def refcallback()->None:
    refresh.slowref()
    messagebox.showinfo(title = 'Completed!', message = 'Completed refreshing!')

def reffcallback()->None:
    refresh.fastref()
    messagebox.showinfo(title = 'Completed!', message = 'Completed fast refreshing!')

def schcallback()->None:
    schlst.delete(0, END)
    schscilist.delete(0, END)
    ans:list = guimatch.calculate(warnAsError, isComm.get(), isSci.get(), parser.parse(schinput.get()))
    global old
    old = parsed.oldtype(isComm.get(), isSci.get(), parser.parse(schinput.get()))
    global results
    results = parsed.searchresult(ans)
    disp:list = []
    dispsci:list = []
    for elem in ans:
        if elem[1] != 'None':
            disp.append(elem[1])
        else:
            disp.append(elem[0] + ' (Scientific name, no common name avaliable)')
        dispsci.append(elem[0])
    for elem in disp:
        schlst.insert(END, elem)
    for elem in dispsci:
        schscilist.insert(END, elem)
    schlst.pack(side = LEFT)
    schscilist.pack(side = RIGHT)

def helpcallback()->None:
    messagebox.showinfo(title = 'Help', message = '''Search syntax:
[opts]animal[opts]
Option format: 'kind':'settings'
'kind' should be one of
type, kingdom, phylum,
class, order, family, genus
If 'kind' is type, 'settings' should be one of
DD, LC, NT, VU, EN, CR, EW, EX
with both lower-case and upper-case versions
If 'kind' is any other setting, 'settings' should be a valid name.
'''
)

if __name__ == '__main__':
    frame:Tk = Tk()
    frame.title('IUCN animal searcher')
    frame.geometry('700x600')
    warnAsErr()
    global isSci
    global isComm
    global opt
    isSci = BooleanVar()
    isComm = BooleanVar()
    opt = StringVar()
    reflab:Label = Label(frame, text = 'Refresh Database (1min)')
    refbtn:Button = Button(frame, text = 'Refresh', command = refcallback)
    refflab:Label = Label(frame, text = 'Fast refresh from GitHub (20s-)')
    reffbtn:Button = Button(frame, text = 'Fast Refresh', command = reffcallback)
    reflab.pack()
    refbtn.pack()
    refflab.pack()
    reffbtn.pack()
    schlab:Label = Label(frame, text = 'Search the animal you want')
    schinput:Entry = Entry(frame)
    options:Frame = Frame(frame)
    schcomm:Checkbutton = Checkbutton(options, text = 'Use common names', variable = isComm, offvalue = False, onvalue = True)
    schsci:Checkbutton = Checkbutton(options, text = 'Use scientific names', variable = isSci, offvalue = False, onvalue = True)
    schbtns:Frame = Frame(frame)
    schbtn:Button = Button(schbtns, text = 'Search', command = schcallback)
    schhelp:Button = Button(schbtns, text = 'Help on syntax', command = helpcallback)
    schres:Frame = Frame(frame)
    schlst:Listbox = Listbox(schres, selectmode = SINGLE, width = 37, height = 20)
    schscilist:Listbox = Listbox(schres, selectmode = SINGLE, width = 37, height = 20)
    schlst.bind('<Double-Button-1>', selectcallback)
    schscilist.bind('<Double-Button-1>', sciselectcallback)
    schlab.pack()
    schinput.pack()
    options.pack()
    schcomm.pack(side = LEFT)
    schsci.pack(side = RIGHT)
    schbtns.pack()
    schbtn.pack(side = LEFT)
    schhelp.pack(side = RIGHT)
    schres.pack()
    frame.mainloop()
else:
    raise exceptions.notMainError()