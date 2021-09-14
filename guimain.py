import exceptions
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import guimatch
import time
import refresh

warnAsError = False
lvls = ['Everything', 'DD/Data Deficient', 'LC/Least Concern', 'NT/Near Threatened', 'VU/Vulnerable', 'EN/Endangered', 'CR/Critically Endangered', 'EW/Extinct In The Wild', 'EX/Extinct']

def warnAsErr():
    global warnAsError
    if messagebox.askyesno(title = 'Warnings as Errors?', message = 'Do you want to treat all warning as errors?'):
        warnAsError = True
        print('All warnings shall be treated as errors now')

def selectcallback(res):
    res = schlst.get(ACTIVE)
    res = res.replace(' (Scientific name, no common name avaliable)', '')
    ans = guimatch.calculate(schinput.get(), warnAsError, isComm.get(), isSci.get(), opt.get())
    for elem in ans:
        if elem[1] == res:
            messagebox.showinfo(title = 'Details about %s' % elem[1], message = '''Scientific name: %s

Common name: %s

Danger level: %s

Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7], elem[8]))
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
Genus: %s''' % (elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7], elem[8]))
            frame.update()
            return
        elif elem[1] == 'None' and elem[0] == res:
            messagebox.showinfo(title = 'Details about %s' % elem[0], message = '''Scientific name: %s

Common name: %s

Danger level: %s

Kingdom: %s
Phylum: %s
Class: %s
Order: %s
Family: %s
Genus: %s''' % (elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7], elem[8]))
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
Genus: %s''' % (elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], elem[7], elem[8]))
            frame.update()
            return
    time.sleep(5)

def refcallback():
    refresh.slowref()
    messagebox.showinfo(title = 'Completed!', message = 'Completed refreshing!')

def reffcallback():
    refresh.fastref()
    messagebox.showinfo(title = 'Completed!', message = 'Completed fast refreshing!')

def schcallback():
    schlst.delete(0, END)
    ans = guimatch.calculate(schinput.get(), warnAsError, isComm.get(), isSci.get(), opt.get())
    disp = []
    for elem in ans:
        if elem[1] != 'None':
            disp.append(elem[1])
        else:
            disp.append(elem[0] + ' (Scientific name, no common name avaliable)')
    for elem in disp:
        schlst.insert(END, elem)
    schlst.pack()

def optcallback(res):
    schlst.delete(0, END)
    res = guimatch.calculate(schinput.get(), warnAsError, isComm.get(), isSci.get(), opt.get())
    disp = []
    for elem in res:
        if elem[1] != 'None':
            disp.append(elem[1])
        else:
            disp.append(elem[0] + ' (Scientific name, no common name avaliable)')
    for elem in disp:
        schlst.insert(END, elem)
    schlst.pack()

if __name__ == '__main__':
    frame = Tk()
    frame.title('IUCN animal searcher')
    frame.geometry('700x600')
    warnAsErr()
    global isSci
    global isComm
    global opt
    isSci = BooleanVar()
    isComm = BooleanVar()
    opt = StringVar()
    reflab = Label(frame, text = 'Refresh Database (1min)')
    refbtn = Button(frame, text = 'Refresh', command = refcallback)
    refflab = Label(frame, text = 'Fast refresh from GitHub (20s-)')
    reffbtn = Button(frame, text = 'Fast Refresh', command = reffcallback)
    reflab.pack()
    refbtn.pack()
    refflab.pack()
    reffbtn.pack()
    schlab = Label(frame, text = 'Search the animal you want')
    schinput = Entry(frame)
    options = Frame(frame)
    schcomm = Checkbutton(options, text = 'Use common names', variable = isComm, offvalue = False, onvalue = True)
    schsci = Checkbutton(options, text = 'Use scientific names', variable = isSci, offvalue = False, onvalue = True)
    schfil = Combobox(frame, values = lvls, state = 'readonly', textvariable = opt)
    schfil.bind('<<ComboboxSelected>>', optcallback)
    schfil.current(0)
    schbtn = Button(frame, text = 'Search', command = schcallback)
    schlst = Listbox(frame, selectmode = SINGLE, width = 75, height = 20)
    schlst.bind('<Double-Button-1>', selectcallback)
    schlab.pack()
    schinput.pack()
    options.pack()
    schcomm.pack(side = LEFT)
    schsci.pack(side = RIGHT)
    schfil.pack()
    schbtn.pack()
    frame.mainloop()
else:
    raise exceptions.notMainError()