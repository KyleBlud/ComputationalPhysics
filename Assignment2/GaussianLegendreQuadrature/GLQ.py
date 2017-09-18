'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 17, 2017
'''
import bs4 as bs
import urllib.request
import numpy as np

def f(x):
    return np.arctan(np.sqrt(x**2 + 2))/(np.sqrt(x**2 + 2) * (x**2 + 1))

sauce = urllib.request.urlopen("https://pomax.github.io/bezierinfo/legendre-gauss.html").read()
soup = bs.BeautifulSoup(sauce, "lxml")

a, b = 0, 1
legendre_roots = []
actual = (5 * np.pi**2)/96

order = input("Which order? 2, 4, 8, 16, 32 or \"quit\"? ")

while (order != "quit"):
    div = soup.find("div", id = "n" + order)
    rows = div.find("table", class_ = "tbl").find("tbody").find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        cells.pop(0)
        cells[0] = float(str(cells[0]).replace("<td>", "").replace("</td>", ""))
        cells[1] = float(str(cells[1]).replace("<td>", "").replace("</td>", ""))
        legendre_roots.append((cells[0], cells[1]))
    estimation = 0
    for weight, node in legendre_roots:
        estimation += weight * ((0.5 * (b - a)) * f(node))
    print("Estimation: " + str(estimation))
    print("Actual: " + str(actual))
    print("Difference: " + str(abs(actual - estimation)))
    legendre_roots.clear()
    order = input("Which order? 2, 4, 8, 16, 32 or \"quit\"? ")
    