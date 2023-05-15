#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def nalog_calc(df):

    df = df.reset_index()
    
    na = pd.DataFrame() # создаём отдельный датафрейм для всех показателей, 
                        # связанных с расчётом налога и соответствием разлиным границам
    
    na['coef11'] = (df['Цена']>3000000)
    na['coef12'] = (df['Цена']<=5000000)
    na['coef13'] = (2023-df['Год выпуска'])<= 3
    na['coef21'] = (df['Цена']>5000000)
    na['coef22'] = (df['Цена']<=10000000)
    na['coef23'] = (2023-df['Год выпуска'])<= 5
    na['coef31'] = (df['Цена']>10000000)
    na['coef32'] = (df['Цена']<=15000000)
    na['coef33'] = (2023-df['Год выпуска'])<= 10
    na['coef41'] = (df['Цена']>15000000)
    na['coef42'] = (2023-df['Год выпуска'])<= 10
    na.insert(11, 'coef', 1)

    # коэффицент домножения для дорогих машин
    na['coef'][np.where((na[['coef11','coef12','coef13']]).all(axis = 1) == True)[0]] = 1.1
    na['coef'][np.where((na[['coef21','coef22','coef23']]).all(axis = 1) == True)[0]] = 2
    na['coef'][np.where((na[['coef31','coef32','coef33']]).all(axis = 1) == True)[0]] = 3
    na['coef'][np.where((na[['coef41','coef42']]).all(axis = 1) == True)[0]] = 3
    na.insert(12, 'sil', 1)

    # ЛС умножаются на кол-во рублей за одну ЛС (зависит от ЛС)
    na['sil'][np.where((df['ЛС'] < 100).values  == True)[0]] = 12
    na['sil'][np.where((pd.DataFrame({'1': df['ЛС'] >= 100,
                                      '2': df['ЛС'] < 125})).all(axis=1)  == True)[0]] = 25
    
    na['sil'][np.where((pd.DataFrame({'1': df['ЛС'] >= 125,
                                      '2': df['ЛС'] < 150})).all(axis=1)  == True)[0]] = 35
    
    na['sil'][np.where((pd.DataFrame({'1': df['ЛС'] >= 150,
                                      '2': df['ЛС'] < 175})).all(axis=1)  == True)[0]] = 45
    
    na['sil'][np.where((pd.DataFrame({'1': df['ЛС'] >= 175,
                                      '2': df['ЛС'] < 200})).all(axis=1)  == True)[0]] = 50
    
    na['sil'][np.where((pd.DataFrame({'1': df['ЛС'] >= 200,
                                      '2': df['ЛС'] < 225})).all(axis=1)  == True)[0]] = 65
    
    na['sil'][np.where((pd.DataFrame({'1': df['ЛС'] >= 225,
                                      '2': df['ЛС'] < 250})).all(axis=1)  == True)[0]] = 75
    
    na['sil'][np.where((df['ЛС'] >= 250).values  == True)[0]] = 150
    df['Налог'] = df['ЛС']* na['coef'] * na['sil'] * 1 # непосредсвтенно налог
    df['Налог'][np.where(df['Тип двигателя'] == 'Электро')[0]] = 0 # для электрокаров налога нет
    df['Налог'] = df['Налог'].astype(int)
    
    df= df.drop('index', axis=1)

    return df

def class_(df):

    df.insert(12, 'Класс', 1)
    q=(df['Цена'].quantile([0.2, 0.4, 0.6, 0.8])).values # делим все цены на 5 частей равного размера
    df['Класс'][np.where((df['Цена'] < q[0]).values  == True)[0]] = 1
    df['Класс'][np.where((pd.DataFrame({'1': df['Цена'] >= q[0],'2': df['Цена'] < q[1]})).all(axis=1)  == True)[0]] = 2
    df['Класс'][np.where((pd.DataFrame({'1': df['Цена'] >= q[1],'2': df['Цена'] < q[2]})).all(axis=1)  == True)[0]] = 3
    df['Класс'][np.where((pd.DataFrame({'1': df['Цена'] >= q[2],'2': df['Цена'] < q[3]})).all(axis=1)  == True)[0]] = 4
    df['Класс'][np.where((df['Цена'] > q[3]).values  == True)[0]] = 5
    
    return df


# In[ ]:




