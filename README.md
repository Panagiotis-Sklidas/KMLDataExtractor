# KMLDataExtractor

<!-- <div>
    <div align="center">
        <img src="https://www.ihu.edu.gr/images/logos/IHU_logo_blue_en.jpg" alt="International Hellenic University logo" width="auto", height="200">
    </div>
<br> -->

[![CodeFactor](https://www.codefactor.io/repository/github/panagiotis-sklidas/kmldataextractor/badge?s=d0699cef9b9fb2d401535093cf0e6cbe8a2fba55)](https://www.codefactor.io/repository/github/panagiotis-sklidas/kmldataextractor)

</div>

<!-- Contents -->
# Contents

- [About the Project](#about-the-project)
  * [Features](#features)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Run locally](#run-locally)
  <!-- * [Usage](#usage) -->
- [License](#license)
- [Acknowledgements](#acknowledgements)

<!-- About the Project -->
## About the Project
This project was created during my studies at the University for the course "Optimization Algorithms". The final assignment required us to use optimization algorithms to find a solution to a similar postman problem with coordinates from a kml file. This python script can export the placemarks name and coordinates (latitude and longitude) to a csv file as well as convert the latitude and longitude to x, y, and z coordinates creating a second csv file with them.

<!-- Features -->
### Features
 * Exports a csv file named rawcoordinates, which has all placemarkers name and their latitude, longitude and altitude coordinates
 * Exports a csv file named coordinates, which has all placemarkers name, their x, y and z coordinates

 #### Curenntly working on:
 * Make the script run as a terminal app

<!-- Getting Started -->
## Getting Started

<!-- Prerequisites -->
### Prerequisites

In order to run the application locally you should have the following installed:
* Python 3.9.6 (Download [here](https://www.python.org/downloads/release/python-396/))
* defusedxml module
```
pip install defusedxml
```

<!-- Run Locally-->
### Run Locally
1) In your IDE, change the filepath of the doc variable to show your kml file.
<div>
  <img src="images/KMLdoc.png" alt="" width="auto", height="auto">
</div>

2) Then run and let the script extract and create the csv files with the latitude and longitute and x,y,z coordinates.

<!-- Usage -->
<!-- ## Usage -->


<!-- License -->
## License
See [LICENSE](https://github.com/Panagiotis-Sklidas/KMLDataExtractor/blob/main/LICENSE)

<!-- Acknowledgments-->
## Acknowledgements
SUBJECT AREA: Optimazation Algorithms
<br>
KEYWORDS: Python, KML, Data extraction, Transform coordinates to xyz
