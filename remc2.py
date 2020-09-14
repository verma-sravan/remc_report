# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:31:47 2020

@author: cr5
"""

import pandas as pd

#ARINSUN.csv
df_ab=pd.read_csv('C:/Users/LENOVO/Desktop/Sravan/remc_report_generator/ARINSUN.csv',\
               skiprows=6,header=None)
df_ab.rename(columns={0:'TB',1:'Timestamp',2:'Forecast',3:'Actual',4:'Avc',5:'Error'},inplace=True)

time_block=20
df_ab=df_ab[:time_block]





def calcErrPercWithRespectToAvc(actVals, forecastVals, avcVals):
    if (len(actVals) != len(forecastVals)) and (len(actVals) != len(avcVals)):
        return None
    errVals = []
    for valIter in range(len(actVals)):
        if avcVals[valIter] != 0:
            errVal = (actVals[valIter] - forecastVals[valIter]) * \
                100/avcVals[valIter]
        else:
            errVal = 0
        errVals.append(errVal)
    return errVals

def getNumBlksWithErrLessThan15(df):
    actVals=df['Actual'].tolist()
    forecastVals=df['Forecast'].tolist()
    avcVals=df['Avc'].tolist()
    errPercVals = calcErrPercWithRespectToAvc(actVals, forecastVals, avcVals)
    numBlks15 = len([x for x in errPercVals if abs(x) <= 15])
    return numBlks15

getNumBlksWithErrLessThan15(df_ab)


#
#
#df_cd=pd.read_csv('C:/Users/LENOVO/Desktop/Sravan/remc_report_generator/WRISTS.csv',\
#               skiprows=6,header=None)
#df_cd.rename(columns={0:'TB',1:'Timestamp',2:'Forecast',3:'Actual',4:'Avc',5:'Error'},inplace=True)
#
#time_block=20
#df_cd=df_cd[:time_block]





'''

section c tablec of remc report 
'''



def get_df(path):    
    df=pd.read_csv(path,\
                   skiprows=6,header=None)
    df.rename(columns={0:'TB',1:'Timestamp',2:'Forecast',3:'Actual',4:'Avc',5:'Error'},inplace=True)
    
    time_block=20
    df=df[:time_block]
    return df


def get_sec_b_data(df_cd,name):
    df_cd['actual_minus_forecast']=df_cd['Actual']-df_cd['Forecast']
    index_min=df_cd['actual_minus_forecast'].idxmin()
    index_max=df_cd['actual_minus_forecast'].idxmax()
    df_cd.loc[index_min]['TB']
    #l=[]
    dic={'name':name,'pos_max_err':df_cd.loc[index_min]['actual_minus_forecast'],'pos_max_err_tb':df_cd.loc[index_min]['TB'],'neg_max_err':df_cd.loc[index_max]['actual_minus_forecast'],'neg_max_err_tb':df_cd.loc[index_max]['TB']}
    #l.append(dic)
    #dff=pd.DataFrame(l)
    return(dic)
#
#resValsList=[]
#resValsList.append(get_sec_b_data(df_cd,'WR_ISTS'))
#resValsList.append(get_sec_b_data(df_cd,'Gujrat'))
#resValsList.append(get_sec_b_data(df_cd,'Maharashtra'))
#resValsList.append(get_sec_b_data(df_cd,'Madhya Pradesh'))
#resValsList.append(get_sec_b_data(df_cd,'WR Combined'))
#dff=pd.DataFrame(resValsList)

import glob
files=glob.glob(r'C:\Users\LENOVO\Desktop\Sravan\remc_report_generator\section_c_data\*.csv')
resValsList=[]
list_con=['WR_ISTS','Gujrat','Maharashtra','Madhya Pradesh','WR Combined']
i=0
resValsList=[]
for f in files:
    print(f)
    df=get_df(f)
    resValsList.append(get_sec_b_data(df,list_con[i]))
    i=i+1
    print(df)
dff=pd.DataFrame(resValsList)
