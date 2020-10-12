# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:18:09 2020

@author: Larissa
"""

def read_data(filename):
    data = open(filename, 'r')
    
    data_list = [item.strip('\n').split('\t') for item in data.readlines()]
    data.close()
    return data_list

data_blastx = read_data("malaria.blastx.tab")
data_fasta = read_data("malaria.fna")

dict_blastx={}
for l in data_blastx:
    dict_blastx.update({l[0]:l[9]})
    
    
def add_prot_name (i):
    if i[0][0] == '>':
        if dict_blastx[i[0][1:]] != 'null':
            i.append(dict_blastx[i[0][1:]])
    return i

output_list = [add_prot_name(i) for i in data_fasta]


output = open("output.txt", 'w')

def add_tab(i):
    if len(i) > 1:
        val = ''
        for f in i[:-1]:
            val = val + f + '\t'
        val = val + i[-1] + '\n'
    else: val = i[0] + '\n'
    return val

for i in output_list:
    output.write(add_tab(i))