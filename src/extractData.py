import xml.etree.ElementTree as et
import os
import io
import csv

doc = et.parse("example.kml")

data = []

nmsp = '{http://www.opengis.net/kml/2.2}'


def extractdata():
    for pm in doc.iterfind('.//{0}Placemark'.format(nmsp)):
        marker = pm.find('{0}name'.format(nmsp)).text

        for ls in pm.iterfind('.//{0}coordinates'.format(nmsp)):
            coordinates = ls.text.strip().replace('\n','')

            data.append({"marker": marker, "coordinates": coordinates})

extractdata()

def createcsv():
    try:
        with io.open('coordinates.csv', mode='w', newline='') as crtcsv:
            write = csv.writer(crtcsv)
            write.writerow(['Marker', 'Coordinate 1', 'Coordinate 2', 'Coordinate 3'])
    except csv.Error as e:
        print(e)

def writedatacsv():
    try:
        with io.open('coordinates.csv', mode='a', newline='') as csvw:
            write = csv.writer(csvw)
            for entry in data:
                name = entry['marker']
                position = entry['coordinates'].split(",")
                write.writerow([name,position[0],position[1],position[2]])
    except csv.Error as e:
        print(e)

if os.path.exists('coordinates.csv'):
    writedatacsv()
else:
    createcsv()
    writedatacsv()


# if __name__ == '__main__':
#     pass
