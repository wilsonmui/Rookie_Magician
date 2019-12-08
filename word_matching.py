def word_matching(keywords, text):
    keywords = convert_keywords(keywords)
    text = convert_text(text)

def convert_keywords(keywords):
    # add spaces to both front and end of each keywords
    for i in range(len(keywords)):
        keywords[i] = " " + keywords[i].lower() + " "
    return keywords

def convert_text(text):
    # convert symbols in the text into spaces
    symbols = [',', '.', '\'', '\"', '?', '!'] # TODO: to complete the list
    for i in range(len(symbols)):
        text = text.replace(symbols[i], " ")
    return text
