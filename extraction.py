# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd

#This Script requires that you are running it within the //data directory


comp_set = ['06055', # Napa County
            '06053', # Monterey County
            '06083', # Santa Barbara County
            '06085', # Santa Clara County 
            '06097', # Sonoma County
            '06073', # San Diego County
            '06017', # El Dorado County
            '06065', # Riverside County
            '12095', # Orange County
            'CS488'] # San Francisco - San Jose


current_directory = os.getcwd()
data_directory = os.path.join(current_directory, 'data')
all_qtrly_data_directory = os.path.join(data_directory, '04-14_qtrly_by_area')

files = os.listdir(all_qtrly_data_directory)


def generateData():

    masterframe = []   
    for directory in files:
        cur_data_directory = os.path.join(all_qtrly_data_directory, directory)
        flat_files = os.listdir(cur_data_directory)
        for flat_file in flat_files:
            for comp in comp_set:
                if comp in flat_file:
                    current_frame = pd.read_csv(os.path.join(cur_data_directory, flat_file))
                    masterframe.append(current_frame)
                    appended_data = pd.concat(masterframe, axis = 0)

    return appended_data










