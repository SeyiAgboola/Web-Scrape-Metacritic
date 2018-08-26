import requests
from bs4 import BeautifulSoup as soup

#Open Metacritic High Scores, Select All Platforms
#Filter by Year
#Request, test, response and parse Page Link
#Loop through Review Links
#Extract Game name, Review Link, Overall Score
#Extract Other Scores, Developer, User Score in Review Link

#Filter by Year
#oneSeven = "http://www.metacritic.com/browse/games/score/metascore/year/all/filtered?sort=desc&year_selected=2017"
#Request, test, response and parse Page Link
#reqLink = requests.get(oneSeven, headers={'User-Agent':'Mozilla/5.0'})

def mainParser(link):
    import requests
    from bs4 import BeautifulSoup as soup
    reqLink = requests.get(link, headers={'User-Agent':'Mozilla/5.0'})
    if reqLink.status_code == 200:
        return soup(reqLink.text, 'lxml')
    else:
        print('Link has failed')

#Loop through Review Links
def reviewLinks(link):
    rows = link.find_all('div', attrs={'class':'product_row game'})
    for game in range(len(rows)):
        newRow = []
        title = rows[game].find('a').get_text().strip()
        #'The Legend of Zelda: Breath of the Wild\n                                            (WIIU)'
        link = rows[game].find('a').get('href').strip()
        #'/game/wii-u/the-legend-of-zelda-breath-of-the-wild'
        rank = rows[game].find('div', attrs={'class':'product_item row_num'}).get_text().strip()
        metascore = rows[game].find('div', attrs={'class':'product_item product_score'}).get_text().strip()
        userscore = rows[game].find('div', attrs={'class':'product_item product_userscore_txt'}).get_text().strip()
        productDate = rows[game].find('div', attrs={'class':'product_item product_date'}).get_text().strip()
        newRow.append((title,link,rank,metascore,userscore,productDate))
        myDict[title] = newRow
        print(str(title) + ' has been added to myDict')
        
#Extract Game name, Review Link, Overall Score
#Extract Other Scores, Developer, User Score in Review Link


#upload to csv
def createCSV(filename):
    import csv
    with open("\\Game Reviews\\" + filename + '.csv', 'w', newline='') as file:
        #,encoding="utf-8"
        a = csv.writer(file, delimiter=',')
        #Only run headers 1 time in write mode, then append mode for new entries
        headers = ['Name','URL', 'MetaRank', 'Metascore', 'User score', 'Product Date']
        a.writerow(headers)
        for row in myDict:
            a.writerow(myDict[row][0])
            print(row + " has been uploaded")
    #close file

#titles = metaPage.find_all('h3', attrs={'class':'product_title'})
#supermario = 'www.metacritic.com' + str(titles[0].find('a').get('href'))


myDict = {}
print('Please input Metacritic year list below')
url = input()
metaSoup = mainParser(url)
reviewLinks(metaSoup)
print('What would like to call the csv file?')
fileplz = input()
createCSV(fileplz)
