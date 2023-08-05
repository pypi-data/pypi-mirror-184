# Data Library - V.1.0
This library contains functions that are useful for daily programing problems in Hunty operation.
- This first version is mainly focused on standardizing and augmenting the vacancies data that cames from linkedin and scrapers

The following graph  shows the state of the library:

<img width="1446" alt="Screen Shot 2022-12-09 at 10 21 42 AM" src="https://user-images.githubusercontent.com/64613638/206734901-1dda6d91-c8d1-4725-b16b-15b81ab1070d.png">


How to use it:
1. Install the library 
```
pip install hunty_dat_lib
```

2. Import the library 

```
from huntydata.standardization import GmapsAPI, Companies_standardization
from huntydata.augmentation import Remote_augmentation
```

A. Remote_augmentation:  this process is useful to extract unstructured information inside columns like location,vacancy_name or description. 
- df_vacancies: recently extracted vacancies dataframe
- remote_types: different ways in which a company can refer to a remote vacancy 
- cols_for_augm: cols that we are going to use for remote augmentation. 

```
Remote_augmentation(df_vacancies,
                     remote_types,
                     cols_for_augm)
```

<img width="746" alt="Screen Shot 2022-12-09 at 10 22 37 AM" src="https://user-images.githubusercontent.com/64613638/206735204-f11e0694-a48c-4c68-b5ad-002f7bd7750a.png">


B. GMAPS: This process uses gmaps API to standardize locations of the vacancies.
To use GmapsAPI Standardization you should pass the following parameters to the class
- locations_to_remove: a list of locations that Data team knows that Api Gmaps cant standardized. this is to avoid requesting the API without a reason, remember Gmaps API costs. 
- df_defined_remotes: before standardization a process called augmentation takes place. This process augments the data but it also cleans the vacancies dataframe to improve standardizing process. 
- ctl_gmaps_locations: a catalogue that contains standardizations that we already made in the past with the API. If we store this we can reduce costs by not passing to the API what we already obtain from it. 
- ctl_locations: this is the main catalogue that we use in hunty to set an id with to  an specific location. 
- gmap_api_key: Gmaps API key
- dict_match_ratio_location: after standardizing data with gmaps API we try to macth those location with ctl_location and we do this by comparing  tensorflow embeddings. this dictionary contains match ratios ( between two cities) that we calculated in the past (is useful to improve efficiency of the library)

```
GmapsAPI(locations_to_remove,
            df_defined_remotes,
            ctl_gmaps_locations, 
            ctl_locations,
            gmap_api_key, 
            dict_match_ratio_location)
```

<img width="558" alt="Screen Shot 2022-12-09 at 10 23 05 AM" src="https://user-images.githubusercontent.com/64613638/206735247-09bc1c38-8702-46ea-8267-e8195d11676b.png">


C. Companies Standardization
- df_defined_remotes: before standardization a process called augmentation takes place. This process augments the data but it also cleans the vacancies dataframe to improve standardizing process. 
- df_ctl_companies: catalogue that set and id to an specific company
- dict_match_ratio_companies: by comparing tensorflow embeddings we created a dictionary that contains match ratios (between two companies)  that we calculated in the past (is useful to improve efficiency of the library)
```
Companies_standardization(df_defined_remotes, 
                          df_ctl_companies,
                          dict_match_ratio_companies)
```

<img width="539" alt="Screen Shot 2022-12-09 at 10 23 15 AM" src="https://user-images.githubusercontent.com/64613638/206735330-209a866c-7c01-43e9-939b-3a30c5bc485a.png">

To watch this library working you can take a look at input directory inside this repo, that directory contains every input that the library need to run. In the tester file of the same directory you can try it.

