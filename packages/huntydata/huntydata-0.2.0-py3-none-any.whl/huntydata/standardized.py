import re
import requests
import json
import numpy as np
import pandas as pd
from huntydata.errors import Errors



class General_standardization:

    #Todo: Quizas esta clase no es necesaria si no comparten atributos

    def standardize_nans(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:

        """
        standardized types of NANs values for an specific  a column
        :return df: cleaned column of a dataframe  with standardized types of NANs
        :param : a dataframe
        :param columns: a list of column that you want to clean
        """
        method_name = General_standardization.standardize_nans.__name__
        try:

            df[columns].replace({'Nan': None, 'NAN': None, np.nan: None, 'None': None, pd.NaT: None,
                                'NaT': None, np.NaN: None, " ": None, "": None}, inplace=True)

        except Exception as error:
            raise Errors(method_name, error)

        return df

    def clean_special_characters(self, df: pd.DataFrame, col_list: list) -> pd.DataFrame:
        """
        Clean special characters in multiple columns
        :return df: cleaned columns of a dataframe  with no  special characters
        :param : a dataframe
        :param col_list: List of columns to remove special characters
        """
        method_name = General_standardization.clean_special_characters.__name__
        try:
            df[col_list] = df[col_list].applymap(lambda x: re.sub("[!*\)-><@#%?(&_/^']", " ", str(x)))
        except Exception as error:
            raise Errors(method_name, error)

        return df

    def define_regex(self, to_replace) -> str:
        '''
        Defines a Regex string by taking values from a list and concatenate them
        :return regx: a regx string
        :param to_replace: values to concatenate and convert into regex
        '''

        method_name = General_standardization.define_regex.__name__
        try:
            regx = r"({})".format("|".join(to_replace))
        except Exception as error:
            raise Errors(method_name, error)

        return regx

    def replace_with_rgx(self, df:pd.DataFrame , output_col: str,
                               input_col: str, regx: str, new_val) -> pd.DataFrame:
        '''
        with a regex string replace values of a specific column.
        :return df: a dataframe with
        :param output_col: output column with replace result
        :param input_col: base column to find values to replace
        :param regx: values that you want to replace
        :param new_val: value to set after the replacement
        '''

        method_name = General_standardization.replace_with_rgx.__name__
        try:
            df[input_col] = df[input_col].apply(lambda x: str(x).lower())
            df[output_col] = df[input_col].str.replace(regx, new_val).fillna(df[input_col])
        except Exception as error:
            raise Errors(method_name, error)

        return df


class GmapsAPI:

    def __init__(self, gmaps_api_key: str, ctl_gmaps_locations: dict):
        '''
        initialization function. Loads parameters for every instance of the of GmapsAPI class
        :param gmaps_api_key: api key to use google maps api
        :param ctl_gmaps_locations: catalogue with google maps standardized locations
        '''

        self.gmaps_api_key = gmaps_api_key
        self.gmaps_locations = ctl_gmaps_locations

    def search_standardized_locations(self, locations_list: list)-> list :
        """
        Search which location we should standardize with Google Maps Catalogue.
        We will only pass unseen locations to reduces cost of using the API

        :returns to_standardize_list:  a list with locations that we should pass through GMAPS API
                                      (those that we do not have in the ctl_gmaps)
        :param locations_ctl_list: a list of unique locations in our catalogue.
        """
        method_name = GmapsAPI.search_standardized_locations.__name__
        to_standardize_list = []
        try:
            for value in locations_list:
                if value not in self.gmaps_locations.keys():
                    to_standardize_list.append(value)

        except Exception as error:
            raise Errors(method_name, error)

        return to_standardize_list

    def request_api(self, to_standardize_list: list)-> dict :

        """
        Request Gmaps Api to Standardized locations

        in a dictionary returns 2 keys:
        :returns dict_new_locations: a dictionary with standardized locations  from Gmaps API
        :returns no_standardized_locations: a list with locations that Gmaps API can't standardized
        
        :param to_standardize_list: list of locations to standardize with Gmaps (those that are not inside ctl_gmaps)
        """
        method_name = GmapsAPI.request_api.__name__
        try:
            dict_new_locations = {}
            no_standardized_locations = []

            if len(to_standardize_list) > 0:
                for location in to_standardize_list:
                    try:
                        location = location.replace("(", "").replace(")", "")
                    except:
                        pass
                    params = {"key": self.gmaps_api_key, "address": location}
                    base_ulr = "https://maps.googleapis.com/maps/api/geocode/json"  # components = country:CO
                    response = requests.get(base_ulr, params=params).json()

                    if response["status"] == "OK":
                        dict_address = {}
                        formatted_address = response["results"][0]["formatted_address"]
                        split_formatted_address = formatted_address.split(", ")
                        if len(split_formatted_address) == 1:
                            dict_address["state"] = np.nan
                            dict_address["city"] = np.nan
                            dict_address["country"] = split_formatted_address[0]
                        elif len(split_formatted_address) == 2:
                            dict_address["country"] = split_formatted_address[-1]
                            dict_address["state"] = np.nan
                            dict_address["city"] = split_formatted_address[0]
                        elif len(split_formatted_address) == 3:
                            dict_address["country"] = split_formatted_address[-1]
                            dict_address["state"] = split_formatted_address[1]
                            dict_address["city"] = split_formatted_address[0]
                        else:
                            dict_address["country"] = split_formatted_address[-1]
                            dict_address["state"] = split_formatted_address[2]
                            dict_address["city"] = split_formatted_address[1]

                        dict_new_locations.update({f"{location}": dict_address})

                    else:
                        no_standardized_locations.append(location)
            else:
                dict_new_locations = {}

        except Exception as error:
            raise Errors(method_name, error)

        return {'dict_new_locations': dict_new_locations, 'no_standardized_locations':no_standardized_locations}


    def update_gmaps_locations(self, dict_new_locations: dict) -> None:
        """
        update gmaps location catalogue (locally) by adding recent standardized locations
        :returns None:

        :param dict_new_locations: recently standardized locations with Gmaps api
        """
        method_name = GmapsAPI.update_gmaps_locations.__name__
        try:
            self.gmaps_locations.update(dict_new_locations)

        except Exception as error:
            raise Errors(method_name, error)


        return None

    def expand_json_to_columns(self, df: pd.DataFrame,input_col:str, json_col:str) -> pd.DataFrame:

        """
        Use recently updated CTL_GMAPS_LOCATIONS to standardize locations of vacancies


        :returns df_expanded: dataframe with a json expanded in columns

        :param json_col: output column that will have json with encapsulated columns
        :param input_col: base column to map a json
        :param df: a dataframe with recently updated CTL_GMAPS_LOCATIONS

        """

        method_name = GmapsAPI.expand_json_to_columns.__name__
        try:

            df_expanded = df.copy()
            df_expanded[json_col] = df_expanded[input_col].map(self.gmaps_locations)

            df_expanded = pd.concat([df_expanded,df_expanded[json_col].apply(pd.Series)], axis=1)
            df_expanded.drop(columns=[json_col], inplace=True)

            try:
            # expand of json might generate a columns named 0
                df_expanded.drop(columns=[0], inplace=True)
            except:
                pass

        except Exception as error:
            raise Errors(method_name, error)

        return df_expanded
