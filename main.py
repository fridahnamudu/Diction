# Python3 program for a word frequency
# counter after crawling/scraping a web-page
import requests
import bs4
import operator
from collections import Counter
import re

'''Function defining the web-crawler/core
spider, which will fetch information from
a given website, and push the contents to
the second function clean_wordlist()'''


def start(url):
    # empty list to store the contents of
    # the website fetched from our web-crawler
    wordlist = []
    source_code = requests.get(url).text

    # BeautifulSoup object which will
    # ping the requested url for data
    soup = bs4(source_code, 'html.parser')

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


# Function removes any unwanted symbols


def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


# Creates a dictionary containing each word's
# count and top_20 occurring words


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

        # starts crawling and prints output
        start(url)


'''
To get the count of each word in the crawled page -->

# operator.itemgetter() takes one
# parameter either 1(denotes keys)
# or 0 (denotes corresponding values)for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
print ("% s : % s " % (key, value))<-- 
'''

# Driver code
