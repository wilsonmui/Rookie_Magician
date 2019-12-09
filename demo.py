from tkinter import *
from tkinter.scrolledtext import ScrolledText
import text_generator as tg
import word_matching
chosen_spell_book = "spongebob"


text_generating_length = 500
text_generating_temperature = 0.7

# initial menu
class Spellbooks:
    spellbooks = ["spongebob", "love_letter", "grey"]

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
        self.app = GamePlay(self.newWindow, self.spellbook.get(), self.sess, self.equipment.keywords)

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

    player_health = 100
    enemy_health = 100

    def __init__(self, master, spellbook, sess, player_keywords):
        self.master = master
        self.frame = Frame(self.master)
        self.spellbook = spellbook
        self.player_keywords = player_keywords
        self.sess = sess

        # display generated text
        self.gen_text_label = Label(master, text="generated text:")
        self.gen_text_label.grid(row=0, column=0, sticky=W, pady=2)
        self.gen_text_list = ScrolledText(master, width=30, height=10, bg='beige')
        self.gen_text_list.grid(row=1, column=0, sticky=W, pady=2)

        # show equipped keywords
        self.keywords_label = Label(master, text="player entered keywords:")
        self.keywords_label.grid(row=0, column=1, sticky=W, pady=2)
        self.keywords_list = ScrolledText(master, width=30, height=10, bg='beige')
        self.keywords_list.grid(row=1, column=1, sticky=W, pady=2)
        keywords = self.get_keywords()
        for i in range(len(keywords)):
            self.keywords_list.insert('insert', keywords[i] + '\n')

        # create prompt
        # self.prompt_label = Label(master, text="Prompt")
        # self.prompt_label.grid(row=2, column=0, sticky=W, pady=2)

        self.prompt_entry = Entry(master)
        self.prompt_entry.grid(row=2, column=0, pady=4)

        self.prompt_button = Button(master, text="Cast Spell", command=self.process_entry)
        self.prompt_button.grid(row=2, column=1, sticky=E)

        # action events window
        self.events_label = Label(master, text="events:")
        self.events_label.grid(row=3, column=1, sticky=W, pady=2)
        self.events_list = ScrolledText(master, width=30, height=10, bg='beige')
        self.events_list.grid(row=4, column=1, sticky=W, pady=2)


    def close_windows(self):
        self.master.destroy()

    def process_entry(self):
        print("spellbook selected :" + self.spellbook)
        print("prefix : " + self.prompt_entry.get() + " generating text...")
        length, temperature = self.get_text_generating_length_and_temperature()
        text_result = tg.generate(self.spellbook, length, temperature, str(self.prompt_entry.get()), self.sess)
        text_result = self.prune_text_result(text_result, length)
        print(text_result + "...", flush = True)
        self.show_generated_text(text_result + "...")
        self.matching_keyword(text_result, self.get_keywords())
        #self.prompt_entry.delete(0, 'end')

    def matching_keyword(self, text_result, keywords):
        matching_count = word_matching.word_matching(text_result, keywords)
        print("keywords match:" + str(matching_count), flush = True)
        damage_dealt = pow(2, matching_count) / matching_count
        spell_cast = ""
        if self.spellbook == "spongebob":
            spell_cast = "enchanted krabby patty magic bomb"
        elif self.spellbook == "love_letter":
            spell_cast = "affection aura"
        elif self.spellbook == "grey":
            spell_cast = "magic duct tape and chains"
        self.events_list.insert('insert', spell_cast + " dealt " + str(damage_dealt) + " damage\n")

        # update health
        self.player_health = self.player_health - 10
        self.enemy_health = self.enemy_health - damage_dealt

        if self.enemy_health <= 0:
            self.events_list.insert('insert', "You defeated the enemy!\n")
        elif self.player_health <= 0:
            self.events_list.insert('insert', "The enemy has killed you.\n")
        else:
            self.events_list.insert('insert', "Your health: " + str(self.player_health) + "\n")
            self.events_list.insert('insert', "Enemy health: " + str(self.enemy_health) + "\n")


    def show_generated_text(self, text):
        # TODO: display text_result to interface
        self.gen_text_list.insert('insert', text + '\n')
        pass

    def get_keywords(self):
        # TODO: get keywords of both player and spellbook
        spellbook_keywords = []
        # Start of testing block
        if self.spellbook == "spongebob":
            spellbook_keywords = ["spongebob", "run", "squidward"]
        elif self.spellbook == "love_letter":
            spellbook_keywords = ["will", "like", "hope"]
        elif self.spellbook == "grey":
            spellbook_keywords = ["take", "grey", "into"]

        keywords =  self.player_keywords[0:7] + spellbook_keywords

        print_keywords = "keywords: "
        for i in range(len(keywords)):
            print_keywords += keywords[i] + ", "
        # print(print_keywords, flush = True)
        return keywords
        # End of testing block

    def prune_text_result(self, text_result, length):
        text_end_index = 0
        min_text_length = length - 100
        acceptable_end_symbol = [".", ",", "!", "?"]
        for i in range(len(acceptable_end_symbol)):
            text_end_index = text_result.find(acceptable_end_symbol[i], min_text_length)
            if text_end_index != -1:
                text_result = text_result[0:text_end_index]
                break
        return text_result.replace("’", "\'").replace("”", "\"").replace("“", "\"")

    def get_text_generating_length_and_temperature(self):
        if self.spellbook == "spongebob":
            return 500, 0.8
        elif self.spellbook == "love_letter":
            return 500, 0.7
        elif self.spellbook == "grey":
            return 700, 0.8
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
