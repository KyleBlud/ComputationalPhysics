'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 17, 2017
'''
import bs4 as bs
import urllib.request
import numpy as np

def f(x):
    return np.arctan(np.sqrt(x**2 + 2))/(np.sqrt(x**2 + 2)*(x**2 + 1))

sauce = urllib.request.urlopen("https://pomax.github.io/bezierinfo/legendre-gauss.html").read()
soup = bs.BeautifulSoup(sauce, "lxml")

weights = []
nodes = []
actual = (5 * np.pi**2)/96
counter = 1

order = input("Which order? 2, 4, 8, 16, 32 or \"quit\"? ")

while (order != "quit"):
    div = soup.find("div", id = "n" + order)
    rows = div.find("table", class_ = "tbl").find("tbody").find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        cells.pop(0)
        for cell in cells:
            cell = str(cell).replace("<td>", "").replace("</td>", "")
            if (counter % 2 == 0):
                nodes.append(float(cell))
            else:
                weights.append(float(cell))
            counter += 1
    estimate = 0
    for i in range(int(order)):
        estimate += weights[i] * f(nodes[i])
    print(str(estimate))
    print(str(actual))
    weights.clear()
    nodes.clear()
    order = input("Which order? 2, 4, 8, 16, 32 or \"quit\"? ")