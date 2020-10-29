import requests
from bs4 import BeautifulSoup
import csv

ranges = [{
        "url": "https://www.artcollectorz.com/artworks/artwork-detail?artwork_id={}",
        "start": 19540,
        "end": 19550
    }, {
        "url": "https://www.artcollectorz.com/artists/artist-detail?artist_id={}",
        "start": 1,
        "end": 3142
    }, {
        "url": "https://www.artcollectorz.com/publishers?publisher_id={}",
        "start": 1,
        "end": 1301
    }
]
#
#
with open('Range1.csv', 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    headers = 'Name,Image URL,Artist Name,Colab,Description,Member Informations,Edition,Published By,Published On,Number in Edition,Artwork Dimensions,Price on Release,Artwork Mediums,Owned By'
    headers = headers.split(",")
    writer.writerow(headers)
    for i in range(1, ranges[0]['end']):
        source = requests.get(ranges[0]['url'].format(i)).text
        soup = BeautifulSoup(source, "html.parser")
        name = soup.select_one(".big-artwork-content h1").text
        if name == '':
            continue
        try:
            headings = soup.select_one(".artist-heading")
            headings = [heading.text.strip(":") for heading in headings]
            print(ranges[0]['url'].format(i))
            cells = soup.select(".artist-heading")
            for cell in cells:
                cell.select_one("h4").decompose()
            cells = [cell.text.strip() for cell in cells]
            data_dict = {}
            data_dict['artist_name'] = data_dict['colab'] = data_dict
            for heading, cell in zip(headings, cells):
                data_dict[heading] = cell
            # cells_data = soup.select(".artist-heading ")
            data = [name, iname, artist_name, colab, description, data_dict['Published By'], data_dict['Published On'], data_dict['Number In Edition'], data_dict['Artwork Dimensions'], data_dict['Price On Release'], data_dict['Artwork Mediums'], data_dict['Owned By']]
            writer.writerow(data)
        except AttributeError:
            continue
        image = soup.select_one(".big-artwork img")['src']
        iname = image.split("/")[-1]
        r = requests.get("https://www.artcollectorz.com/" + image, stream=True)
        if r.status_code == 200:
            with open("Range1/{}".format(iname), 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        try:
            description = soup.select_one(".description .inner").text
        except AttributeError:
            description = ''
        headings = soup.select(".cell h4")
        headings = [heading.text.strip(":") for heading in headings]
        print(ranges[0]['url'].format(i))
        cells = soup.select(".cell")
        for cell in cells:
            cell.select_one("h4").decompose()
        cells = [cell.text.strip() for cell in cells]
        data_dict = {}
        data_dict['Edition'] = data_dict['Published By'] = data_dict['Published On'] = data_dict['Number In Edition'] = \
        data_dict['Artwork Dimensions'] = data_dict['Price On Release'] = data_dict['Artwork Mediums'] = data_dict[
            'Owned By'] = ''
        for heading, cell in zip(headings, cells):
            data_dict[heading] = cell
            # cells_data = soup.select(".cell ")
            data = [name, iname, artist_name, colab, description, data_dict['Published By'], data_dict['Published On'], data_dict['Number In Edition'], data_dict['Artwork Dimensions'], data_dict['Price On Release'], data_dict['Artwork Mediums'], data_dict['Owned By']]
            writer.writerow(data)


with open('Range2.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in range(1, ranges[1]['end']):
        source = requests.get(ranges[1]['url'].format(i)).text
        soup = BeautifulSoup(source, "html.parser")
        name = soup.select_one(".artist-heading h1").text
        if name == '':
            continue
        print(ranges[1]['url'].format(i))
        image = soup.select_one(".col-a .artist-image img")['src']
        iname = image.split("/")[-1]
        r = requests.get("https://www.artcollectorz.com/" + image, stream=True)
        if r.status_code == 200:
            with open("Range2/{}".format(iname), 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        bio = soup.select_one(".artist-bio").text.strip()
        connections = soup.select(".social-links a")
        connections = [conn['href'] for conn in connections]
        conn = ['', '', '', '']
        for connection in connections:
            if "instagram" in connection:
                conn[1] = connection
            elif "facebook" in connection:
                conn[0] = connection
            elif "twitter" in connection:
                conn[2] = connection
            else:
                conn[3] = connection
        data = [name, iname, bio]
        data.extend(conn)
        writer.writerow(data)

with open('Range3.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in range(1, ranges[2]['end']):
        source = requests.get(ranges[2]['url'].format(i)).text
        soup = BeautifulSoup(source, "html.parser")
        name = soup.select_one(".publisher-heading h1").text
        if name == '':
            continue
        print(ranges[2]['url'].format(i))
        image = soup.select_one(".publisher-image img")['src']
        iname = image.split("/")[-1]
        r = requests.get("https://www.artcollectorz.com/" + image, stream=True)
        if r.status_code == 200:
            with open("Range3/{}".format(iname), 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        bio = soup.select_one(".publisher-bio").text.strip()
        connections = soup.select(".social-links a")
        connections = [conn['href'] for conn in connections]
        conn = ['', '', '', '']
        for connection in connections:
            if "instagram" in connection:
                conn[1] = connection
            elif "facebook" in connection:
                conn[0] = connection
            elif "twitter" in connection:
                conn[2] = connection
            else:
                conn[3] = connection
        data = [name, iname, bio]
        data.extend(conn)
        writer.writerow(data)
