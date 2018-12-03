# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:49:31 2018

@author: congpeiqing
"""
import os
from SimpleBP import SimpleBP
from GenData import genData

if not os.path.exists('data'):
    os.makedirs('data')  

#构造训练和测试数据
data_file = open('data/trainning_data.dat' , 'w')
data_file.write(genData())
data_file.close()

data_file = open('data/test_data.dat' , 'w')
data_file.write(genData())
data_file.close()


#文件格式：rec_id,attr1_value,attr2_value,attr3_value,class_id
#读取和解析训练数据
trainning_data_file = open('data/trainning_data.dat')
trainning_data = []
for line in trainning_data_file :
    line = line.strip()
    fld_list = line.split(',')
    trainning_data.append(tuple([float(field) for field in fld_list[1:]]))
trainning_data_file.close()

#读取和解析测试数据
test_data_file = open('data/test_data.dat')
test_data = []
for line in test_data_file :
    line = line.strip()
    fld_list = line.split(',')
    test_data.append(tuple([float(field) for field in fld_list[1:]]))
test_data_file.close()


#构造一个二分类网络 输入节点3个，隐层节点10个，输出节点一个
simple_bp = SimpleBP(3 , 10 , trainning_data , test_data)
#训练网络
simple_bp.trainByItem()
#测试分类准确率
print('Accuracy : ' , simple_bp.getAccuracy())
#训练时长比较长，准确率可以达到97%