# Diction

## Description

This is  an application which, when given a web page will download the text on it and output a sorted list of the unique words on the page, with counts of the occurrences.



## Live-Link
 -  The project runs on the terminal.
 
## BDD


1.  Python3 program for a word frequency
# counter after crawling/scraping a web-page
import requests
import bs4 - Beautiful Soup which we use it as bs4 is a Python library for pulling data out of HTML and XML files. 
It works with a parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 

import operator
from collections import Counter- to collect the counts of the unique words.
import re

the def start() Function defines the web-crawler/core spider, which will fetch information from a given website, and push the contents to
the second function clean_wordlist()


def start(url):
    - i initilize an  empty list to store the contents of the website fetched from our web-crawler
    wordlist = []
    source_code = requests.get(url).text

   - soup is a BeautifulSoup object which will pick the requested url for data
    soup = bs4(source_code, 'html.parser')

    - Text in given web-page is stored under the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

     - I use split() to break the sentence into words and convert them into lowercase using .lower
        words = content.lower().split()

        for each_word in words:
        - .append adds the words picked into the lisr\t
            wordlist.append(each_word)
        clean_wordlist(wordlist)


-def clean_wordlist() Function removes any unwanted symbols


def clean_wordlist(wordlist):
    clean_list = [] - initialising an empty list
    for word in wordlist: - looping through the wordlist
        symbols = "!@#$%^&*()_-+={[}]|\;:\<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


#def create_dictionary() -Creates a dictionary containing each word's count and top_20 occurring words


def create_dictionary(clean_list, url="https://pesapal.freshteam.com/jobs/-z8xM8RCgTx7/junior-developer"):
    unique_word = {} - initializing an empty dictionary 

    for word in clean_list: - loop through the clean_list to get the unique words.
        if word in unique_word:
            unique_word[word] += 1
        else:
            unique_word.update({word: 1})

            c = Counter(unique_word) - counts the unique words

            - top returns the unique elements by printing it.
            top = c.most_unique(10)
            print(top)

    if __name__ == '__main__':
        url = "https://pesapal.freshteam.com/jobs/-z8xM8RCgTx7/junior-developer"
        listOfWords = re.split("[\W]+", url)
        for words in listOfWords:- loops through the listOfWords to get the unique word.
            unique_word(word)
        for element in unique_word: - get the unique word by making sure it doesn't look like any other.
            if unique_word[element] == 1:
                print(element)

        -start() -starts crawling and prints output
        start(url)
        


## Set Up Instructions

- Open your terminal and move to a directory where you would like to store the project eg. cd Documents
- Use the command `git clone` to clone the aplication at `https://github.com/fridahnamudu/Blog`.
- After cloning navigate to the project.
- Run `pip install` to install all the dependencies
- Now run the project using your terminal with the command 'python main.py'

## Technologies Used

- PYTHON
- 

## Licence

The MIT License (MIT)
Copyright (c) 2020 FRIDAH JOY NAMUDU.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

@FRIDAH JOY NAMUDU

## Contact Details

- You can reach me through:

  fridah.namudu@gmail.com

## Author

**FRIDAH JOY NAMUDU**
