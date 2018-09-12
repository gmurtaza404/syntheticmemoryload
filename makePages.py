#imports
import itertools # for computing permutations
from itertools import chain, combinations,permutations
from bs4 import BeautifulSoup
import os

# Globals
headerHtml ="<html lang=\"en\"><head><meta charset=\"UTF-8\"> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\"><title>Proxy server</title></head>"
rootHtml = "<div id=\"root\"> <p> This page is just an artificial memeory load </p> <p> for sake of comaparison each div will take same amount of space on disk</p></div>"

#powerset
def powerset(iterable):
    "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

#generates all possible htmls from list of strings
def generateHtmls(listofEntries):
    allPermutes = list(permutations(listofEntries))
    allPages = []
    print len(allPermutes)
    for permutes in allPermutes:
        #print permutes
        tempHtml = headerHtml + "<body>" + rootHtml
        for htmls in permutes:
            tempHtml = tempHtml + htmls
        tempHtml = tempHtml + "</body>" + "</html>"
        soup = BeautifulSoup(tempHtml, 'html.parser')
        tempHtml = soup.prettify()
        allPages.append(tempHtml)
    return allPages




def main():
    imageHtml = " <div id =\"images\"> <img src = \"world.topo.bathy.png\" /></div>"
    videoHtml = "<div id = \"video\"> <video width=\"320\" height=\"240\" controls><source src=\"Horses_2.mp4\" type=\"video/mp4\"></video></div>"
    codeHtml = "<div id = \"code\"><script src = \"client.js\"> </script></div>"
    html_list = [imageHtml,codeHtml,videoHtml]
    allHtmlPages = []

    powerset_html = list(powerset(html_list))
    for sets in powerset_html:
        allHtmlPages = allHtmlPages + generateHtmls(sets)
    
    count = 0
    old_dir = os.getcwd()
    os.chdir("pages")

    for page in allHtmlPages:

        with open(str(count)+".html","wb") as f:
            f.write(page)
        count = count+1
    os.chdir(old_dir)

main()