# io.py --- 
# 
# Filename: DataIO.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sun Mar 25 17:09:06 2018 (-0500)
# Version: 
# Last-Updated: Wed Aug 22 11:44:04 2018 (-0500)
#           By: yulu
#     Update #: 105
# 

import numpy as np
import pandas as pd
from scibeam.core import base

class Loader:
    
    def __init__(self, addressDict):
        self.fileDict = addressDict
        
    @property
    def fileDict(self):
        return self.__fileDict
    
    @fileDict.setter
    def fileDict(self, addressDict):
        self.__fileDict = addressDict
        self.data = None
        
        

    
    def load(self, ncol = base.Defaults.data_file_num_column):
        addressDict = self.fileDict
        dataDict = {}
        # check if path is given in the address dictionary, if not, ask for input
        try:
            path = addressDict['path']
        except KeyError:
            print("[!] No [path] key found in dictionary, please give a path")
            raise KeyError
        
        print("[*] In folder %s, loading..." %path)
        for key1 in sorted(list(addressDict.keys())):
            if key1 == 'path':
                continue
            try:
                subpath = addressDict[key1]['path']
            except TypeError:
                subpath = None
                pass
            
            if subpath:
                print('Key1: %s,  Key2:' %key1, end=" ")
                dataDict[key1] = {}
                for key2 in sorted(list(addressDict[key1].keys() - ['path'])):
                    print(key2, end = " ")
                    dataDict[key1][key2] = []
                    for fileName in addressDict[key1][key2]:
                        data = np.fromfile(path + subpath + fileName,  sep = '\t').reshape(-1,ncol)
                        
                        dataDict[key1][key2].append(data)
                print('\n')
                        
            else:
                print('key: %s' %key1, end = " ")
                
                if type(addressDict[key1]) == str:
                    filePath = base.pathJoin(path, addressDict[key1])
                    data = np.fromfile(filePath,  sep = '\t').reshape(-1,ncol)
                    dataDict[key1] = data
                else:
                    dataDict[key1] = []
                    for fileName in addressDict[key1]:
                        filePath = base.pathJoin(path, fileName)
                        data = np.fromfile(filePath,  sep = '\t').reshape(-1,ncol)
                        dataDict[key1].append(data)
        self.data = self.toDataFrame(dataDict)
        return self

    @staticmethod
    def toDataFrame(data):
        """
        toDataFrame
        ---------------------
        Convert dictionary structured time series data into pandas DataFrame
        
        [Input]
        Data loaded by method loadFromDict

        [Output]
        Pandas dataframe if 2D data 
        or dictionary of dataframes if 3D data 
        """
        
        
        dataKeys = data.keys()
        df = {}
        for key in dataKeys: # e.g. chamber position 
            try:
                subKeys = data[key].keys()
            except AttributeError:
                subKeys = None
            if not subKeys is None:
                df[key] = {}
                subKeys = sorted(list(subKeys))
                for i, subkey in enumerate(subKeys): # e.g. scan position
                    
                    if i == 0:
                        df[key]['time'] = data[key][subkey][:,0] if type(data[key][subkey][:,0]) == str else data[key][subkey][0][:,0]
                    else:
                        pass
                    repeatNum = len(data[key][subkey]) # repeated data number (for average reason
                    if repeatNum > 1 and type(data[key][subkey]) == list:
                        for i in range(repeatNum):
                            df[key][subkey + str(i)] = data[key][subkey][i][:,1]
                    else:
                        df[key][subkey] = data[key][subkey][:,1]
            else:
                if not 'time' in df:
                    df['time'] = data[key][0][:, 0] if type(data[key]) == list else data[key][:, 0]
                else:
                    pass
                repeatNum = len(data[key])
                if repeatNum > 1 and type(data[key]) == list:
                    for i in range(repeatNum):
                        df[key + str(i)] = data[key][i][:,1]
                else:
                    df[key] = data[key][:,1]

        if 'time' in df: # if single dataset, df = pandas DataFrame
            df = pd.DataFrame(df)
            # make sure time comes as the 0th column 
            df = df[['time'] + [x for x in sorted(df.columns) if x!= 'time']]
        else: # else df = a dictionary of pandas DataFrame 
            for key in df:
                df[key] = pd.DataFrame(df[key])
                df[key] = df[key][['time'] + [x for x in sorted(df[key].columns) if x!='time']]
                
        
        return df
    
    
    
