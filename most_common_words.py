import collections
def main():
    books = ["grey", "love_letter", "quenya", "spongebob"]
    symbols = [',', '.', '\"', '?', '!'] # TODO: to complete the list
    generate_common("grey", symbols)
    symbols = [',', '.', '?', '!', '“'] # TODO: to complete the list
    generate_common("love_letter", symbols)
    symbols = [',', '.', '\"', '?', '!'] # TODO: to complete the list
    generate_common("quenya", symbols)
    symbols = [',', '.', '\"', '?', '!', '[', ']', ':'] # TODO: to complete the list
    generate_common("spongebob", symbols)



def generate_common(file_name, symbols):
    common_words = {}
    with open("src/" + file_name + ".txt", encoding="utf-8") as file_in:
        for line in file_in:
            for i in range(len(symbols)):
                line = line.replace(symbols[i], " ").lower()
            for word in line.split():
               if word in common_words:
                   common_words[word] += 1
               else:
                   common_words[word] = 1

    file_out = open("output/common_" + file_name + ".txt", "w", encoding="utf-8")
    file_out_filtered = open("output/common_" + file_name + "_filtered.txt", "w", encoding="utf-8")
    common_words = collections.OrderedDict(sorted(common_words.items(), key=lambda x: x[1], reverse=True))

    for word, count in common_words.items():
        file_out.write(word + " : " + str(count) + "\n")
        if len(word) >= 4:
            file_out_filtered.write(word + " : " + str(count) + "\n")

if __name__ == '__main__':
    main()
