import requests
import bs4
import operator
from collections import Counter
import re




def start(url):
 
    wordlist = []
    source_code = requests.get(url).text
    soup = bs4(source_code, 'html.parser')

   
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)




def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)



def create_dictionary(clean_list, url="https://pesapal.freshteam.com/jobs/-z8xM8RCgTx7/junior-developer"):
    unique_word = {}

    for word in clean_list:
        if word in unique_word:
            unique_word[word] += 1
        else:
            unique_word.update({word: 1})

            c = Counter(unique_word)

            # returns the unique elements
            top = c.most_unique(10)
            print(top)

    if __name__ == '__main__':
        url = "https://pesapal.freshteam.com/jobs/-z8xM8RCgTx7/junior-developer"
        listOfWords = re.split("[\W]+", url)
        for words in listOfWords:
            unique_word(word)
        for element in unique_word:
            if unique_word[element] == 1:
                print(element)

        
        start(url)





