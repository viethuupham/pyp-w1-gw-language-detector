# -*- coding: utf-8 -*-

"""This is the entry point of the program."""
def count_words(list_of_words, language):
    count = 0
    for word in list_of_words:
        if word in language:
            count +=1
            
    return count

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    
    #Clean text and seperate into list of words
    temp_list = text.split()
    list_of_words = []
    for word in temp_list:
        word = word.strip("-,()-.")
        list_of_words.append(word.lower())
    
    #Count words for each language
    word_counts = {}
    for language in languages:
        word_counts[language['name']] = count_words(list_of_words, language['common_words'])
    
    return max(word_counts.keys(), key=(lambda key: word_counts[key]))


