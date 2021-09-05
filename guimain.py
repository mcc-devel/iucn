import exceptions
from tkinter import *
from tkinter import messagebox
import iucn
import guimatch
import time

warnAsError = False

def warnAsErr():
    global warnAsError
    if messagebox.askyesno(title = 'Warnings as Errors?', message = 'Do you want to treat all warning as errors?'):
        warnAsError = True
        print('All warnings shall be treated as errors now')

def selectcallback(res):
    res = schlst.get(ACTIVE)
    res = res.replace(' (Scientific name, no common name avaliable)', '')
    ans = guimatch.calculate(schinput.get(), warnAsError, isComm.get(), isSci.get())
    for elem in ans:
        if elem[1] == res:
            messagebox.showinfo(title = 'Details about %s' % elem[1], message = '''Scientific name: %s

Common name: %s

Danger level: %s

A notice for you: %s''' % (elem[0], elem[1], elem[2], elem[3]))
            if messagebox.askyesno(title = 'Copy?', message = 'Copy to clipboard?'):
                frame.clipboard_clear()
                frame.clipboard_append('''Scientific name: %s
Common name: %s
Danger level: %s
A notice for you: %s''' % (elem[0], elem[1], elem[2], elem[3]))
            frame.update()
            return
        elif elem[1] == 'None' and elem[0] == res:
            messagebox.showinfo(title = 'Details about %s' % elem[0], message = '''Scientific name: %s

Common name: %s

Danger level: %s

A notice for you: %s''' % (elem[0], elem[1], elem[2], elem[3]))
            if messagebox.askyesno(title = 'Copy?', message = 'Copy to clipboard?'):
                frame.clipboard_clear()
                frame.clipboard_append('''Scientific name: %s
Common name: %s
Danger level: %s
A notice for you: %s''' % (elem[0], elem[1], elem[2], elem[3]))
            frame.update()
            return
    time.sleep(5)

def refcallback():
    iucn.getjson()
    messagebox.showinfo(title = 'Completed!', message = 'Completed refreshing!')

def schcallback():
    schlst.delete(0, END)
    ans = guimatch.calculate(schinput.get(), warnAsError, isComm.get(), isSci.get())
    disp = []
    for elem in ans:
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
    frame.geometry('700x500')
    warnAsErr()
    global isSci
    global isComm
    isSci = BooleanVar()
    isComm = BooleanVar()
    reflab = Label(frame, text = 'Refresh Database (this will take up to 5-6 minutes)')
    refbtn = Button(frame, text = 'Refresh', command = refcallback)
    reflab.pack()
    refbtn.pack()
    schlab = Label(frame, text = 'Search the animal you want')
    schinput = Entry(frame)
    schcomm = Checkbutton(frame, text = 'Use common names', variable = isComm, offvalue = False, onvalue = True)
    schsci = Checkbutton(frame, text = 'Use scientific names', variable = isSci, offvalue = False, onvalue = True)
    schbtn = Button(frame, text = 'Search', command = schcallback)
    schlst = Listbox(frame, selectmode = SINGLE, width = 75, height = 25)
    schlst.bind('<Double-Button-1>', selectcallback)
    schlab.pack()
    schinput.pack()
    schcomm.pack()
    schsci.pack()
    schbtn.pack()
    frame.mainloop()
else:
    raise exceptions.notMainError()