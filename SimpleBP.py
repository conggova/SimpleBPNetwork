# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:49:31 2018

@author: congpeiqing
"""

from activation_funcs import sigmoid
from random import random

class InputNode(object) :
    def __init__(self , idx) :
        self.idx = idx
        self.output = None
            
    def setInput(self , value) :
        self.output = value
        
    def getOutput(self) :
        return self.output
        
    def refreshParas(self , p1 , p2) :
        pass
    
    
class Neurode(object) :
    def __init__(self , layer_name , idx , input_nodes , activation_func = None , powers = None , bias = None) :
        self.idx = idx 
        self.layer_name = layer_name
        self.input_nodes = input_nodes 
        if activation_func is not None :
            self.activation_func = activation_func
        else :
            #默认取 sigmoid
            self.activation_func = sigmoid
        if powers is not None :
            self.powers = powers
        else :
            self.powers = [random() for i in range(len(self.input_nodes))]
        if bias is not None :
            self.bias = bias
        else :
            self.bias = random()
        self.output = None
            
    def getOutput(self) :
        self.output = self.activation_func(sum(map(lambda x : x[0].getOutput()*x[1] , zip(self.input_nodes, self.powers))) + self.bias)
        return self.output
            
    def refreshParas(self , err , learn_rate) :
        err_add = self.output * (1 - self.output) * err  
        for i in range(len(self.input_nodes)) :
            #调用子节点
            self.input_nodes[i].refreshParas(self.powers[i] * err_add , learn_rate)
            #调节参数
            power_delta = learn_rate * err_add * self.input_nodes[i].output   
            self.powers[i] += power_delta
            bias_delta = learn_rate * err_add
            self.bias += bias_delta
    
    
class SimpleBP(object) :
    def __init__(self , input_node_num , hidden_layer_node_num , trainning_data , test_data) :
        self.input_node_num = input_node_num
        self.input_nodes = [InputNode(i) for i in range(input_node_num)]
        self.hidden_layer_nodes = [Neurode('H' , i , self.input_nodes) for i in range(hidden_layer_node_num)]
        self.output_node = Neurode('O' , 0 , self.hidden_layer_nodes)
        self.trainning_data = trainning_data
        self.test_data = test_data
        
        
    #逐条训练
    def trainByItem(self) :
        cnt = 0
        while True :
            cnt += 1
            learn_rate = 1.0/cnt
            sum_diff = 0.0
            #对于每一条训练数据进行一次训练过程
            for item in self.trainning_data :
                for i in range(self.input_node_num) :
                    self.input_nodes[i].setInput(item[i])
                item_output = item[-1]
                nn_output = self.output_node.getOutput()
                #print('nn_output:' , nn_output)
                diff = (item_output-nn_output)
                sum_diff += abs(diff)
                self.output_node.refreshParas(diff , learn_rate)
                #print('refreshedParas')
            #结束条件        
            print(round(sum_diff / len(self.trainning_data) , 4))
            if sum_diff / len(self.trainning_data) < 0.1 :
                break
        
    def getAccuracy(self) :
        cnt = 0
        for item in self.test_data :
            for i in range(self.input_node_num) :
                self.input_nodes[i].setInput(item[i])
            item_output = item[-1]
            nn_output = self.output_node.getOutput()
            if (nn_output > 0.5 and item_output > 0.5) or (nn_output < 0.5 and item_output < 0.5) :
                cnt += 1
        return cnt/(len(self.test_data) + 0.0)
            
        
    