from bs4 import BeautifulSoup

htmlFileOpen = open("C:\\Users\\vitor.vargem\\PycharmProjects\\AutomationProjects\\Robots Course\\tableWebScraping.html", mode="r", encoding="utf-8")
htmlRead = BeautifulSoup(htmlFileOpen, "html.parser")
pageTable = htmlRead.find(id="main_table")
tableLines = pageTable.find_all('tr')

student = {}
studentsData = []

for x in tableLines :
    tableAttributtes = x.find_all("td")
    if len(tableLines) > 0 :
        teste01 = tableAttributtes[0].text
        teste02 = tableAttributtes[1].text
        teste03 = tableAttributtes[2].text
        print(teste01 + " " + teste02 + " " + teste03)

print(studentsData)
