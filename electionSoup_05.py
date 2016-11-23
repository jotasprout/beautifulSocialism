from bs4 import BeautifulSoup
import csv

# Grab local file I downloaded
htmlDoc = open("2016ElectionResultsPresidentPolitico2.htm")
soup = BeautifulSoup(htmlDoc)

# create a text file in which to put leftover soup
f = csv.writer(open("myElectionResults3.csv", "w"))

# Grab just the results table
articles = soup.find_all('article', {'class': 'timeline-group'})

for article in articles:
    # Remove crap before state name
    stateCrap1 = article.header.h3.a.b
    stateCrap1.decompose()
    state = article.header.h3.a.contents

    f.writerow(state)
    # write header row
    f.writerow(["Candidate", "Percentage", "Popular", "Electoral College"])

    trs = article.find_all('tr')

    for tr in trs:
        # Get candidate name
        candidatex = tr.find('span', {'class': 'name-combo'})
        # Remove crap before candidate name
        canCrap = candidatex.find_all('span')
        for crap in canCrap:
            crap.decompose()
        candidate = candidatex.contents

        # Get popular vote
        popularx = tr.find('td', {'class': 'results-popular'})
        popular = popularx.contents

        # Get percentage of vote
        percentagex = tr.find('span', {'class': 'number'})
        percentage = percentagex.contents

        # Get electoral college vote
        electoralCollegex = tr.find('td', {'class': 'delegates-cell'})
        try:
            electoralCollege = electoralCollegex.contents
        except:
            continue

        f.writerow([candidate,popular,percentage,electoralCollege])
