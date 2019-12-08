def word_matching(text, keywords):
    # keywords = convert_keywords(keywords)
    # text = convert_text(text)
    text = text.lower()
    matching_count = 0
    for i in range(len(keywords)):
        start_matching_index = 0
        matching_keyword = keywords[i].lower()
        while(True):
            start_matching_index = text.find(matching_keyword, start_matching_index)
            if start_matching_index != -1: # find the keyword
                start_matching_index += 1 # move on
                matching_count += 1
            else :
                break

    return matching_count
# def convert_keywords(keywords):
#     # add spaces to both front and end of each keywords
#     for i in range(len(keywords)):
#         keywords[i] = " " + keywords[i].lower() + " "
#     return keywords

def convert_text(text):
    # convert symbols in the text into spaces
    symbols = [',', '.', '\'', '\"', '?', '!'] # TODO: to complete the list
    for i in range(len(symbols)):
        text = text.replace(symbols[i], " ")
    return text
