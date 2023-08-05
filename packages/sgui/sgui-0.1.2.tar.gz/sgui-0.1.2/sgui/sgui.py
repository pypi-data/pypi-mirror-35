'''
Copyright 2018 Daniel Griffin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import tkinter
from tkinter import ttk 

class SWidget(object):
    """SWidget base widget class
       TODO __init__ never gets called
    """
    def __init__(self):
        super(SWidget, self).__init__()
        self.enabled = True

    @property
    def enabled(self):
        return not self['state'] == 'disabled'

    @enabled.setter
    def enabled(self, s):
        self['state'] = 'normal' if s else 'disabled'

class CreateToolTip(object):
    """create a tooltip for a given widget"""
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        if self.widget.tooltip != "":
            self.schedule()

    def leave(self, event=None):
        if self.widget.tooltip != "":
            self.unschedule()
            self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x, y = self.widget.winfo_pointerxy()
        x += 20
        y += 20
        # creates a toplevel window
        self.tw = tkinter.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tkinter.Label(self.tw, text=self.widget.tooltip, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

class TextBox(tkinter.Text, SWidget):
    """Wrapper for tkinter Text"""
    def __init__(self, parent, string = "", command = None, anchor = "", *args, **kwargs):
        super(TextBox, self).__init__(parent, *args, **kwargs)
        self.bind('<<Modified>>', self.callbackFunc)
        ori = parent.__class__.__name__
        if ori == "HBox":
            anchor = "center" if anchor == "" else anchor
            self.pack(side=tkinter.LEFT)
        else:
            anchor = "w" if anchor == "" else anchor
            self.pack(anchor=anchor, fill=tkinter.BOTH)
        self.command = command
        self.string = string
        self.tooltip = ""
        CreateToolTip(self)

    @property
    def string(self):
        return self.get(1.0, tkinter.END)[:-1]

    @string.setter
    def string(self, s):
        self.delete(1.0, tkinter.END)
        self.insert(tkinter.END, s)

    def callbackFunc(self, value=None):
        flag = self.edit_modified()
        if flag:
            if self.command is not None:
                self.command(self)
        self.edit_modified(False)

class TextEntry(ttk.Entry, SWidget):
    """Wrapper for ttk Text"""
    def __init__(self, parent, string = "", command = None, anchor = "", *args, **kwargs):
        super(TextEntry, self).__init__(parent, *args, **kwargs)

        self.textVar = tkinter.StringVar()
        self.textVar.trace("w", lambda name, index, mode, sv=self.textVar: self.callbackFunc())
        self.configure(textvariable=self.textVar)

        ori = parent.__class__.__name__
        if ori == "HBox":
            anchor = "center" if anchor == "" else anchor
            self.pack(side=tkinter.LEFT)
        else:
            anchor = "w" if anchor == "" else anchor 
            self.pack(anchor=anchor, fill=tkinter.BOTH)
        self.command = command
        self._flag = True
        self.string = string
        self.tooltip = ""
        CreateToolTip(self)

    @property
    def string(self):
        return self.textVar.get()

    @string.setter
    def string(self, s):
        self.delete(0, tkinter.END)
        self.insert(0, s)

    def callbackFunc(self):
        if self._flag:
            self._flag = False
            if self.command is not None:
                self.command(self)
        self._flag = True

class Button(ttk.Button, SWidget):
    """Wrapper for ttk Button"""
    def __init__(self, parent, string = "", command = None, anchor = "", *args, **kwargs):
        super(Button, self).__init__(parent, *args, **kwargs)
        ori = parent.__class__.__name__
        if ori == "HBox":
            anchor = "center" if anchor == "" else anchor 
            self.pack(side=tkinter.LEFT)
        else:
            anchor = "w" if anchor == "" else anchor 
            self.pack(anchor=anchor, fill=tkinter.BOTH)
        self.configure(command=self.callbackFunc)
        self.command = command
        self.string = string
        self.tooltip = ""
        CreateToolTip(self)

    def callbackFunc(self):
        if self.command is not None:
            self.command(self)

    @property
    def string(self):
        return self["text"]

    @string.setter
    def string(self, s):
        self["text"] = s

class VBox(ttk.Frame):
    """Wrapper for ttk Frame"""
    def __init__(self, parent, anchor = "", expand = 1, *args, **kwargs):
        super(VBox, self).__init__(parent, *args, **kwargs)
        ori = parent.__class__.__name__
        if ori == "HBox":
            anchor = "center" if anchor == "" else anchor 
            self.pack(fill=tkinter.BOTH, expand=expand, side=tkinter.LEFT, anchor = anchor)
        else:
            anchor = "w" if anchor == "" else anchor 
            self.pack(fill=tkinter.BOTH, expand=expand, anchor = anchor)
        self.tooltip = ""
        CreateToolTip(self)

class HBox(ttk.Frame):
    """Wrapper for ttk Frame"""
    def __init__(self, parent, anchor = "", expand = 1, *args, **kwargs):
        super(HBox, self).__init__(parent, *args, **kwargs)
        ori = parent.__class__.__name__
        if ori == "HBox":
            anchor = "center" if anchor == "" else anchor
            self.pack(fill=tkinter.BOTH, expand=expand, side=tkinter.LEFT, anchor = anchor)
        else:
            anchor = "w" if anchor == "" else anchor
            self.pack(fill=tkinter.BOTH, expand=expand, anchor = anchor)
        self.tooltip = ""
        CreateToolTip(self)

class Label(ttk.Label, SWidget):
    """Wrapper for ttk Label"""
    def __init__(self, parent, string = "", *args, **kwargs):
        super(Label, self).__init__(parent, *args, **kwargs)
        ori = parent.__class__.__name__
        if ori == "HBox":
            self.pack(side=tkinter.LEFT)
        else:
            self.pack(anchor='w', fill=tkinter.BOTH)
        self.string = string
        self.tooltip = ""
        CreateToolTip(self)

    @property
    def string(self):
        return self["text"]

    @string.setter
    def string(self, s):
        self["text"] = s

class Checkbox(ttk.Checkbutton, SWidget):
    """Wrapper for ttk Checkbutton"""
    def __init__(self, parent, string = "", command = None, *args, **kwargs):
        super(Checkbox, self).__init__(parent, *args, **kwargs)
        ori = parent.__class__.__name__
        if ori == "HBox":
            self.pack(side=tkinter.LEFT)
        else:
            self.pack(anchor='w', fill=tkinter.BOTH)
        self.checkedVar = tkinter.IntVar()
        self.configure(command=self.callbackFunc, variable=self.checkedVar)
        self.command = command
        self.string = string
        self.tooltip = ""
        CreateToolTip(self)

    def callbackFunc(self):
        if self.command is not None:
            self.command(self)

    @property
    def string(self):
        return self["text"]

    @string.setter
    def string(self, s):
        self["text"] = s 

    @property
    def checked(self):
        return self.checkedVar.get()

    @checked.setter
    def checked(self, boolean):
        if boolean:
            self.state(['selected'])
        else:
            self.state(['!selected'])

class Listbox(tkinter.Listbox, SWidget):
    """Wrapper for ttk Listbox"""
    def __init__(self, parent, items = (), command = None, *args, **kwargs):
        super(Listbox, self).__init__(parent, *args, **kwargs)
        ori = parent.__class__.__name__
        if ori == "HBox":
            self.pack(side=tkinter.LEFT)
        else:
            self.pack(anchor='w', fill=tkinter.BOTH)   
        self.configure(exportselection=False, activestyle=tkinter.NONE)  
        self.bind('<<ListboxSelect>>', self.callbackFunc)   
        self.command = command
        self.items = items
        self.tooltip = ""
        CreateToolTip(self)

    def callbackFunc(self, evt):
        if self.command is not None:
            self.command(self)

    @property
    def items(self):
        return self.get(0, tkinter.END)

    @items.setter
    def items(self, lst):
        self.delete(0, tkinter.END)
        for item in lst:
            self.insert(tkinter.END, item)

    @property
    def selection(self):
        return self.curselection()[0]

    @selection.setter
    def selection(self, index):
        self.selection_clear(0, tkinter.END)
        if index == -1:
            index = tkinter.END
        self.selection_set(index)
        self.see(index)

class Radiobutton(ttk.Radiobutton, SWidget):
    """Wrapper for single ttk Radiobutton
    TODO make command work so individual buttons can trigger"""
    def __init__(self, parent, string = "", command = None, *args, **kwargs):
        super(Radiobutton, self).__init__(parent, *args, **kwargs)
        ori = parent.__class__.__name__
        if ori == "HBox":
            self.pack(side=tkinter.LEFT)
        else:
            self.pack(anchor='w', fill=tkinter.BOTH)
        #self.checkedVar = tkinter.IntVar()
        #self.configure(command=self.callbackFunc, variable=self.checkedVar)
        #self.command = command
        self.string = string
        self.tooltip = ""
        CreateToolTip(self)

    #def callbackFunc(self):
    #    if self.command is not None:
    #        self.command(self)

    @property
    def string(self):
        return self["text"]

    @string.setter
    def string(self, s):
        self["text"] = s 

    @property
    def checked(self):
        return self.checkedVar.get()

    @checked.setter
    def checked(self, boolean):
        if boolean:
            self.state(['selected'])
        else:
            self.state(['!selected'])

class Radiobuttons(ttk.Frame):
    """Wrapper for ttk Radiobuttons/Frame"""
    def __init__(self, parent, items = (), command = None, *args, **kwargs):
        super(Radiobuttons, self).__init__(parent, *args, **kwargs)
        self.ori = parent.__class__.__name__
        if self.ori == "HBox":
            self.pack(side=tkinter.LEFT)
        else:
            self.pack(anchor='w', fill=tkinter.BOTH)   
  
        
        self.command = command
        self.buttons = []
        self._selection = tkinter.IntVar()
        self._buttonNames = []
        self.items = items
        self.tooltip = ""
        CreateToolTip(self)

    def callbackFunc(self):
        if self.command is not None:
            self.command(self)

    @property
    def items(self):
        return tuple(self._buttonNames)

    @items.setter
    def items(self, lst):
        self._buttonNames = []
        for i, item in enumerate(lst):
            b = Radiobutton(self, text=item,
                            variable=self._selection, value=i)
            self.buttons.append(b)
            self._buttonNames.append(item)
            b.configure(command=self.callbackFunc)
            if self.ori == "HBox":
                b.pack(side=tkinter.LEFT)
            else:
                b.pack(anchor='w', fill=tkinter.BOTH)

    @property
    def selection(self):
        return self._selection.get()

    @selection.setter
    def selection(self, index):
        self._selection.set(index)

class Canvas(tkinter.Canvas):
    """Wrapper for tk Canvas"""
    def __init__(self, parent, background="#000000", width=512, height=512, *args, **kwargs):
        super(Canvas, self).__init__(parent, *args, **kwargs)
        self.ori = parent.__class__.__name__
        if self.ori == "HBox":
            self.pack(side=tkinter.LEFT)
        else:
            self.pack(anchor='w', fill=tkinter.BOTH)  
        self.configure(width=width, height=height, background=background) 

    @property
    def items(self):
        return self.find_all()

    @property
    def underCursor(self):
        return self.find_withtag("current")

    def arc(self, x1, y1, x2, y2, outline = "#ffffff", *args, **kwargs):
        return self.create_arc(x1, y1, x2, y2, outline=outline, *args, **kwargs)

    def image(self, *args, **kwargs):
        return self.create_image(*args, **kwargs)

    def line(self, x1, y1, x2, y2, fill = "#ffffff", *args, **kwargs):
        return self.create_line(x1, y1, x2, y2, fill=fill, *args, **kwargs)

    def oval(self, x1, y1, x2, y2, outline = "#ffffff", *args, **kwargs):
        return self.create_oval(x1, y1, x2, y2, outline=outline, *args, **kwargs)

    def polygon(self, coords, outline = "#ffffff", *args, **kwargs):
        return self.create_polygon(coords, outline=outline, *args, **kwargs)

    def rectangle(self, x1, y1, x2, y2, outline = "#ffffff", *args, **kwargs):
        return self.create_rectangle(x1, y1, x2, y2, outline=outline, *args, **kwargs)

    def text(self, position, fill = "#ffffff", *args, **kwargs):
        return self.create_text(position, fill=fill, *args, **kwargs)

    def window(self, position, *args, **kwargs):
        return self.create_window(position, *args, **kwargs)


class Tk(tkinter.Tk):
    """Wrapper for ttk Tk"""
    def __init__(self, *args, **kwargs):
        super(Tk, self).__init__(*args, **kwargs)

    def startGUI(self):
        self.mainloop()