from tkinter import *

chosen_spell = "ex1"

player_health = 100
enemy_health = 100

class Spellbooks:
    spellbooks = ["ex1", "ex2", "ex3"]

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.select_button = Button(self.frame, text='Select', width=25, command=self.new_window)
        self.select_button.pack()
        self.frame.pack()

        self.spellbook = StringVar(master)
        self.spellbook.set(self.spellbooks[0])

        self.option = OptionMenu(master, self.spellbook, self.spellbooks[0], self.spellbooks[1], self.spellbooks[2])
        self.option.pack()

    def new_window(self):
        print(self.spellbook.get())

        self.newWindow = Toplevel(self.master)
        self.app = GamePlay(self.newWindow)

    def select(self, master):
        print("value is", self.spellbook.get())
        master.quit()

class GamePlay:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        # create prompt
        self.prompt_label = Label(master, text="Prompt")
        self.prompt_label.grid(row=0, column=0, sticky=W, pady=2)

        self.prompt_entry = Entry(master)
        self.prompt_entry.grid(row=0, column=1, pady=4)

        self.prompt_button = Button(master, text="Cast Spell", command=self.process_entry)
        self.prompt_button.grid(row=0, column=2, sticky=E)

        # adding image (remember image should be PNG and not JPG)
        self.img = PhotoImage(file=r"magic.gif")
        self.img1 = self.img.subsample(2, 2)

        # setting image with the help of label
        Label(master, image=self.img1).grid(row=0, column=3,
                                       columnspan=2, rowspan=2, padx=5, pady=5)

    def close_windows(self):
        self.master.destroy()

    def process_entry(self):
        print(self.prompt_entry.get())

def main():
    root = Tk()
    app = Spellbooks(root)
    root.mainloop()

if __name__ == '__main__':
    main()