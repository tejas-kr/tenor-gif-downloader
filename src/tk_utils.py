from tkinter import Tk, BOTH, X, LEFT, filedialog
from tkinter.ttk import Frame, Label, Entry, Button
from tkinter import messagebox as mbox

import os

class InputDialog(Frame):

    def __init__(self):
        super().__init__()
        self.search_item = ""
        self.number_items = ""
        self.folder_path = ""
        self.initUI()


    def initUI(self):

        self.master.title("Input Query")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Search String", width=12)
        lbl1.pack(side=LEFT, padx=5, pady=10)

        self.entry1 = Entry(frame1, textvariable=self.search_item)
        self.entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Number of results", width=16)
        lbl2.pack(side=LEFT, padx=5, pady=10)

        self.entry2 = Entry(frame2, textvariable=self.number_items)
        self.entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btn_folder = Button(frame3, text="Select Folder", command=self.selectFolder)
        btn_folder.pack(side=LEFT, padx=5, pady=10)

        self.lbl_folder = Label(frame3, text="")
        self.lbl_folder.pack(fill=X, padx=5)

        frame5 = Frame(self)
        frame5.pack(fill=X)

        btn = Button(frame5, text="Submit", command=self.onSubmit)
        btn.pack(padx=5, pady=10)


    def onSubmit(self):
        try:
            self.search_item = str(self.entry1.get())
            self.number_items = int(self.entry2.get())

            if not (os.path.exists(self.folder_path)): 
                raise ValueError("Folder Path error")

            mbox.showinfo("Information", "Responses Submitted")
            self.quit()
        except ValueError as err:
            mbox.showerror("Error", str(err))

        
    def selectFolder(self):
        self.folder_path = filedialog.askdirectory()
        self.lbl_folder.config(text=str(self.folder_path))


class TKWrapper:
    """ Wrapper for Tk functions """

    def open_dialogue(self) -> tuple:
        """
            Opens the dialog box for search related entries as well as for destination folder selection

            Returns:
                search_item (str): Search Keyword
                number_of_items (int): Number of gifs to be downloaded
                folder_path (str): path of the destination folder
        """

        root = Tk()
        root.geometry("250x180+300+300")
        app = InputDialog()
        root.mainloop()

        search_item, number_of_items, folder_path = (app.search_item, app.number_items, app.folder_path, )

        root.destroy()

        return search_item, number_of_items, folder_path
