from bs4 import BeautifulSoup

# Grab local file I downloaded
htmlDoc = open("2016ElectionResultsPresidentPoliticoFinal.htm")
soup = BeautifulSoup(htmlDoc)

# create a text file in which to put leftover soup
f = open("electionResultsTable3.htm", "w")

# write beginning of html and table skeleton
f.write("<html><head></head><body>")

# Grab just the results table
articles = soup.find_all('article', {'class': 'timeline-group'})

for article in articles:
    # Remove crap before state name
    stateCrap1 = article.header.h3.a.b
    stateCrap1.decompose()
    state = article.header.h3.a.contents

    # write state
    f.write("<h2>" + str(state) + "</h2>" + '\n')

    # write header row
    f.write("<table><tr><th>Candidate</th><th>Party</th><th>Popular</th><th>Percentage</th><th>Electoral</th></tr>")

    trs = article.find_all('tr')

    for tr in trs:
        # Get candidate party
        partytag = tr.find('abbr')
        partyx = partytag.get('title')
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

        f.write("<tr><td>" + str(candidate) + "</td><td>" + str(partyx) + "</td><td>" + str(popular) + "</td><td>" + str(percentage) + "</td><td>" + str(electoralCollege) + "</td></tr>")

    # close this state table
    f.write("</table>" + '\n')

#close html skeleton
f.write("</body></html>")
f.close()
