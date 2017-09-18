'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 17, 2017
'''
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://pomax.github.io/bezierinfo/legendre-gauss.html").read()
soup = bs.BeautifulSoup(sauce, "lxml")

order = input("Which order? 2, 4, 8, 16, 32 or \"quit\"? ")
weights = []
nodes = []

while (order != "quit"):
    div = soup.find("div", id = "n" + order)
    rows = div.find("table", class_ = "tbl").find("tbody").find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        cells.pop(0)
        for cell in cells:
            cell = str(cell).replace("<td>", "").replace("</td>", "")
            print(float(cell))
    order = input("Which order? 2, 4, 8, 16, 32 or \"quit\"? ")