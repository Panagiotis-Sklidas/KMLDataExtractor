import argparse
import defusedxml.ElementTree as et
import io
import csv
import math

def extractdata(doc):
    rawdata = []
    nmsp = '{http://www.opengis.net/kml/2.2}'

    for pm in doc.iterfind('.//{0}Placemark'.format(nmsp)):
        marker = pm.find('{0}name'.format(nmsp)).text

        for ls in pm.iterfind('.//{0}coordinates'.format(nmsp)):
            coordinates = ls.text.strip().replace('\n', '')

            rawdata.append({"marker": marker, "coordinates": coordinates})

    return rawdata

def writerawdatacsv(rawdata):
    try:
        with io.open('rawcoordinates.csv', mode='a', newline='') as csvw:
            write = csv.writer(csvw)
            write.writerow(['Marker', 'Latitude', 'Longitude', 'Altitude'])
            for entry in rawdata:
                name = entry['marker']
                position = entry['coordinates'].split(",")
                write.writerow([name, position[0], position[1], position[2]])
        print('Your data csv with latitude, longitude coordinates is ready!')
    except csv.Error as e:
        print(e)

def longlattoxy(rawdata):
    data = []
    R = 6371

    for entry in rawdata:
        name = entry['marker']
        position = entry['coordinates'].split(",")

        x = R * math.cos(float(position[0])) * math.cos(float(position[1]))
        y = R * math.cos(float(position[0])) * math.sin(float(position[1]))
        z = R * math.sin(float(position[0]))

        data.append({"marker": name, "x": x, "y": y, "z": z})

    return data

def writedatacsv(data):
    try:
        with io.open('coordinates.csv', mode='a', newline='') as csvw:
            write = csv.writer(csvw)
            write.writerow(['Marker', 'x', 'y', 'z'])
            for entry in data:
                name = entry['marker']
                x = entry['x']
                y = entry['y']
                z = entry['z']
                write.writerow([name, x, y, z])
        print('Your data csv with x,y,z coordinates is ready!')
    except csv.Error as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description='Convert KML data to CSV.')
    parser.add_argument('filepath', type=str, help='Path to the KML file')

    args = parser.parse_args()

    doc = et.parse(args.filepath)

    rawdata = extractdata(doc)
    writerawdatacsv(rawdata)

    data = longlattoxy(rawdata)
    writedatacsv(data)

if __name__ == '__main__':
    main()
