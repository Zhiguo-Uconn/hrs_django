import pandas as pd
import numpy as np
import os


def getMortality():
    file_folder = os.path.join(os.path.dirname(__file__), 'supports')
    file_name = 'Mortality.csv'
    file_path = os.path.join(file_folder, file_name)
    df = pd.read_csv(file_path)
    return df

def getIncidenceRate():
    file_folder = os.path.join(os.path.dirname(__file__), 'supports')
    file_name = 'incidenceRate.csv'
    file_path = os.path.join(file_folder, file_name)
    df = pd.read_csv(file_path)
    return df


def get_hle(adjustment, patient):
    age = patient.age
    gender = patient.gender
    mortality = getMortality()[age:]
    i_df = getIncidenceRate()
    q = mortality['H_Male'].to_numpy()
    #d = mortality['D_Male'].to_numpy()
    i = i_df.iloc[0:(q.size), age+1].to_numpy()
    p_hh = (1-i)*(1-q)
    p1 = np.delete(p_hh, p_hh.size-1).cumprod()
    x = 1 - np.delete(p_hh, 0)
    hle = sum(x * p1 * np.arange(1, p_hh.size))
    
    print(age)
    print(gender)
    return hle