<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

## **Ironhack Data PT MAD - Project Module 1**

This README file includes the details of the repository elements required for the module 1 project within Data Analytics Bootcamp in Ironhack Madrid.
The project consists of creating a data pipeline that shows the nearest stations by service (Bicimad or Bicipark) to the place of interest given by the project details. 

**Data**

- CSV file Bicimad stations
- CSV file Bicipark stations
- API REST connection with Portal de datos abiertos del Ayuntamiento de Madrid, with the following data /catalogo/202162-0-instalaciones-accesibles-municip.json, from now known as 'Places of interest'

**Resources in this repository**

This repository will include the following elements (apart from the ones defined in **Data**): 

- Modules:

    - Modules_database py file with all the details on data acquisition and wrangling of the place of interest list, Bicimad, and Bicipark data
    - Modules_function py file with the auxiliary functions to be used during the data pipeline
    - Geo_calculations py file includes the two given functions in the project to calculate distances with coordinates. This module is given for project execution, not created while developing the code.
    - General map creation module to create visual maps of all the places of interest and Bicimad or Bicipark stations
    - Key map creation module to create visual maps of the place of interest input by the user with the nearest station, as well as a line of relation among two points
    - Module api data with all the details of the connection with Bicimad API, extraction in real-time bases, and bikes available in the stations.
-Pipeline:

    - Main.py file with all the data pipeline execution, applying all the auxiliary resources from the modules 
-Notebooks: 

    - A jupyter notebook used for practise and experimentation
-Ouput: 

Output folder with all the results that the pipeline can create.
-Others:

    - Presentation file for the project introduction on project day
    - Trash folder with all the iterations of the main file and modules
```

📁 Folder structure
└── project
    ├── __trash__
    ├── .gitignore
    ├── README.md
    ├── LICENSE
    ├── main.py
    ├── output
    ├── notebooks
    │   ├── dev_notebook_.ipynb
    ├── modules
    │   ├── .env
    │   ├── general_map_creation.py
    │   ├── module_api_data.py
    │   ├── key_api_creation.py
    │   ├── geo_calculations.py
    │   ├── modules_database
    │   ├── modules_function
    └── data
        ├── bicimad_stations.csv
        ├── bicipark_stations.csv

```

🥤**Usage**

At the execution of pipeline with main.py, the user must input through argparse the service that he is interested in ('bicimad or bicipark, as "-p" or "--service") and the place of interest where he is situated (as -t or "--title"). 

The output will be the following: 

- A string with the nearest station to him, total distance and the availability of free bases and bikes in each stations in real-time with the API connection for Bicimad input; in Bicipark case, the result comes from the given CSV.
- A visual map with the position of both points (in the folder output) and a line of correlation.
- A CSV file (in the folder output) indicating th nearest stations with free bases and bikes available. In the case of Bicimad inputs, the results are in real-time; in Bicipark case, the result comes from the given CSV.


In case the user defines the location as "All", the out put will be as it follows: 

- A CSV file with the list of places of interest aligned with the calculated nerest stations from the services of choice,  the distance from each point and the availability of free bases and bikes in each stations in real-time with the API connection (for Bicimad, Bicipark is static data from CSV)
- A visual map including all the places of interest in Madrid with all the existing stations (depending on the service choice, Bicimad or Bicipark).


🔧**Configuration**

The following libraries are used in the pipeline, so they should be downloaded in the environment to be executed

```
import numpy as np
import argparse
from scipy.spatial.distance import cdist
import geopandas as gpd
from shapely.geometry import Point
import requests
import pandas as pd 
import folium 
from fuzzywuzzy import process
from dotenv import load_dotenv
import os
```

💥**Technology stack**

Python, Pandas, Scipy, Scikit-learn, Numpy, Geopandas, Shapely, Fuzzywuzzy, Folium, Os, Dotenv, ArgParse and Requests.

👀**Context**

This repository is the final project for Module 1 project for the Part Time Data Analytics Bootcamp in November 2023, which had the following requirements: 

- Main Challenge:

You must create a Python App (Data Pipeline) allowing potential users to find the nearest BiciMAD station to a set of places of interest using the methods included in the module geo_calculations.py.
Your project must meet the following requirements:

- It must be contained in a GitHub repository with a README file that explains the aim and content of your code. You may follow the structure suggested here.

- It must create, at least, a .csv file including the requested table (i.e. Main Challenge). Alternatively, you may create an image, pdf, plot or any other output format that you may find convenient. You may also send your output by e-mail, upload it to a cloud repository, etc.

- It must provide, at least, two options for the final user to select when executing using argparse: (1) To get the table for every 'Place of interest' included in the dataset (or a set of them), (2) To get the table for a specific 'Place of interest' imputed by the user.

- Additionally:

    You must prepare a 4 minutes presentation (ppt, canva, etc.) to explain your project (Instructors will provide further details about the content of the presentation). The last slide of your presentation must include your candidate for the 'Ironhack Data Code Beauty Pageant'.

- Bonus 1:
You may include in your table the availability of bikes in each station.

- Bonus 2:
You may improve the usability of your app by using FuzzyWuzzy.

- Bonus 3:
Feel free to enrich your output data with any data you may find relevant (e.g.: wiki info for every place of interest) or connect to the BiciMAD API and update bikes availability in realtime or find a better way to calculate distances...there's no limit!!!

💩 **ToDo**

As next steps and continuous improvements: 

- Improve map visualization and data input for usability 
- Create interactive maps to include walkable and transport approaches from the places of interest to the stations, rather than a straight line.


💌 **Contact info**

Hi! I am Ana! 🎟
Feel free to contact me at teamurjc@gmail.com. Happy to chat!
