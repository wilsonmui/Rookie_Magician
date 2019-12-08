from tkinter import *
from tkinter.scrolledtext import ScrolledText
import text_generator as tg
import word_matching
chosen_spell_book = "spongebob"

player_health = 100
enemy_health = 100
text_generating_length = 150
text_generating_temperature = 0.7

# initial menu
class Spellbooks:
    spellbooks = ["spongebob", "quenya", "love_letter", "grey"]

    def __init__(self, master, equipment):
        self.equipment = equipment
        self.sess = None # for gpt2 model
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.spellbook = StringVar(master)
        self.spellbook.set(self.spellbooks[0])

        self.option = OptionMenu(master, self.spellbook, self.spellbooks[0], self.spellbooks[1], self.spellbooks[2])
        self.option.pack()

        self.select_button = Button(self.frame, text='Select', width=25, command=self.new_window)
        self.select_button.pack()

        # keyword entry
        self.entry_label = Label(master, text="keyword entry:")
        self.entry_label.pack()
        self.keyword_input = Entry(master)
        self.keyword_input.bind('<Return>', self.enter_keyword)
        self.keyword_input.pack()

        # show equipped keywords
        self.keywords_label = Label(master, text="player entered keywords:")
        self.keywords_label.pack()
        self.keywords_list = ScrolledText(master, width=30, height=10)
        self.keywords_list.pack()

    def enter_keyword(self, event=None):
        word = self.keyword_input.get()
        self.equipment.keywords.append(word)
        print("current keywords list length: " + str(len(self.equipment.keywords)))
        self.keywords_list.insert('insert', word + '\n')
        self.keyword_input.delete(0, 'end')

    def new_window(self):
        global sess
        global chosen_spell_book
        print("spellbook " + self.spellbook.get() + " is loading...")
        self.sess = tg.load(self.spellbook.get()) # for gpt2 model
        self.newWindow = Toplevel(self.master)
        self.app = GamePlay(self.newWindow, self.spellbook.get(), self.sess)

    def select(self, master):
        print("value is", self.spellbook.get())
        master.quit()

    def set_spellbook_keywords(self):
        # TODO: set keywords for each spellbook
        pass

    def show_equip_window(self):
        # TODO: show keywords equipment window
        pass
# EOF class spellbook

class GamePlay:
    def __init__(self, master, spellbook, sess):
        self.master = master
        self.frame = Frame(self.master)
        self.spellbook = spellbook
        self.sess = sess
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
        print("spellbook selected :" + self.spellbook)
        print("prefix : " + self.prompt_entry.get() + " generating text...")
        text_result = tg.generate(self.spellbook, text_generating_length, text_generating_temperature, str(self.prompt_entry.get()), self.sess)

        print(text_result, flush = True)
        self.show_generated_text()
        self.matching_keyword(text_result, self.get_keywords())

    def matching_keyword(self, text_result, keywords):
        matching_count = word_matching.word_matching(text_result, keywords)
        print("keywords match:" + matching_count, flush = True)

    def show_generated_text(self):
        # TODO: display text_result to interface
        pass
    def get_keywords(self):
        # TODO: get keywords of both player and spellbook
        pass
    def cut_text_result(self, text_result):
        # TODO: prune text result
        return text_result
# EOF class GamePlay

class Equipment:
    keywords = []
    def __init__(self):
        # TODO: setting layout, including showing player equipped keywords, add/remove keywords, and showing spellbook keywords

        pass
    def add_keywords(self):
        # TODO: allow user add keywords if len(keywords) < limit
        pass
    def remove_keywords(self):
        # TODO: allow user remove keyword in the keywords list
        pass

def main():
    root = Tk()
    equipment = Equipment()
    app = Spellbooks(root, equipment)
    root.mainloop()

if __name__ == '__main__':
    main()
