from tkinter import *
import main

# class definition 
class Application(Frame):  
    def __init__(self, master=None):
        Frame.__init__(self, master, height = 700, width = 700, background='orange')
        self.master.title('ComfyPlanner')
        #self.master.geometry('300x300')
        self.grid()
        self.createButtons()
        self.createEntries()
        self.createText()

    def createEntries(self):
        # From entry
        self.labelFrom = Label(self, text='From:', background='orange')  
        self.labelFrom.grid(column = 0, row = 0, sticky=E)
        self.entryFrom = Entry(self)
        self.entryFrom.grid(column = 1, columnspan = 2, row = 0)
        # To entry
        self.labelTo = Label(self, text='To:', background='orange')  
        self.labelTo.grid(column = 0, row = 1, sticky=E)
        self.entryTo = Entry(self)
        self.entryTo.grid(column = 1, columnspan = 2, row = 1)

    def createButtons(self):
        # quit button
        self.quitButton = Button(self, text='Quit',
            command=self.quit)  
        self.quitButton.grid(column = 1, row = 2)
        # plan button
        self.planButton = Button(self, text='Plan',
            command=self.planCallBack)  
        self.planButton.grid(column = 2, row = 2)

    def createText(self):
        # quit button
        self.text = Text(self)
        self.text.insert(INSERT, "The trip plan will written here...")
        self.text.grid(column = 0, columnspan = 4, row = 4, rowspan = 2)

    def planCallBack(self):
        self.depStation = self.entryFrom.get()
        self.arrStation = self.entryTo.get()
        # call planner + deviation
        self.Result = main.main(self.depStation, self.arrStation)
        # show results
        self.text.delete(1.0, END)
        self.text.insert(INSERT, self.Result+'\r\n')
        """self.text.insert(INSERT, "Results of the plan from " \
            + self.depStation + " to " + self.arrStation + " goes here...i\n" \
            + self.Result)"""
        #self.text.insert(INSERT, main.main(self.depStation, self.arrStation))

# GUI creation
app = Application()
app.mainloop()

