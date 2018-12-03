# -*- coding: utf-8 -*-
import numpy as np
from random import random as rdn

'''
说明：我们构造1000条数据，每条数据有三个属性(用a1 , a2 , a3表示)
a1 离散型  取值 1 到 10 ， 均匀分布
a2 离散型  取值 1 到 10 ， 均匀分布
a3 连续型  取值 1 到 100 ， 且符合正态分布 
各属性之间独立。

共2个分类(0 , 1)，属性值与类别之间的关系如下，
0 : a1 in [1 , 3]  and a2 in [4 , 10] and a3 <= 50
1 : a1 in [1 , 3]  and a2 in [4 , 10] and a3 > 50
0 : a1 in [1 , 3]  and a2 in [1 ,  3] and a3 > 30
1 : a1 in [1 , 3]  and a2 in [1 ,  3] and a3 <= 30
0 : a1 in [4 , 10] and a2 in [4 , 10] and a3 <= 50
1 : a1 in [4 , 10] and a2 in [4 , 10] and a3 > 50
0 : a1 in [4 , 10] and a2 in [1 ,  3] and a3 > 30
1 : a1 in [4 , 10] and a2 in [1 ,  3] and a3 <= 30
'''


def genData() :
    #为a3生成符合正态分布的数据
    a3_data = np.random.randn(1000) * 30 + 50
    data = []
    for i in range(1000) :
        #生成a1
        a1 = int(rdn()*10) + 1
        if a1 > 10 :
            a1 = 10
        #生成a2
        a2 = int(rdn()*10) + 1
        if a2 > 10 :
            a2 = 10
        #取a3
        a3 = a3_data[i] 
        #计算这条数据对应的类别
        c_id = 0
        if a1 <= 3 and a2 >= 4 and a3 <= 50 :
            c_id = 0 
        elif a1 <= 3 and a2 >= 4 and a3 > 50 :
            c_id = 1 
        elif a1 <= 3 and a2 < 4 and a3 > 30 :
            c_id = 0
        elif a1 <= 3 and a2 < 4 and a3 <= 30 :
            c_id = 1
        elif a1 > 3 and a2 >= 4 and a3 <= 50 :
            c_id = 0 
        elif a1 > 3 and a2 >= 4 and a3 > 50 :
            c_id = 1 
        elif a1 > 3 and a2 < 4 and a3 > 30 :
            c_id = 0
        elif a1 > 3 and a2 < 4 and a3 <= 30 :
            c_id = 1
        else :
            print('error')
        #拼合成字串
        str_line = str(i) + ',' + str(a1) + ',' + str(a2) + ','  + str(a3) + ',' + str(c_id)
        data.append(str_line)
    return '\n'.join(data)
        
