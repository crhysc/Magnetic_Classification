#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:04:41 2021

@author: lllang
"""
import json
import copy
import re
import pymatgen.core as pmat


with open('neal_data_afterLeftOver.json','r') as f:
    data = json.load(f)
data2 = copy.deepcopy(data)
#################################################################################
# Fixes compositions with minuses and pluses
#################################################################################
compositions = []

for idNum in list(data.keys()):
    compositions.append(data[idNum]['composition'])

comp_dict = {}
for icomp,comp in enumerate(compositions):

    if '+' in comp and '-'in comp: 
        num1 = re.findall(".*([.\d-]+)-([.\d-]+).*",comp)[0]
        final_doping_neg = round(float(num1[0]) - float(num1[1]),3)
        
        num2 = re.findall(".*([.\d-]+)\+([.\d-]+).*",comp)[0]
        final_doping_pos = round(float(num2[0]) + float(num2[1]),3)
        
        reduced_comp = comp.replace(num1[0]+'-'+num1[1],str(final_doping_neg))
        reduced_comp = reduced_comp.replace(num2[0]+'+'+num2[1],str(final_doping_pos))
        comp_dict[comp] =  reduced_comp
        compositions[icomp] =  reduced_comp
    elif '-' in comp: 
        num = re.findall(".*([.\d-]+)-([.\d-]+).*",comp)[0]
        final_doping = round(float(num[0]) - float(num[1]),3)
        reduced_comp = comp.replace(num[0]+'-'+num[1],str(final_doping))
        compositions[icomp] = reduced_comp
        comp_dict[comp] =   reduced_comp
    elif '+' in comp: 
        num = re.findall(".*([.\d-]+)\+([.\d-]+).*",comp)[0]
        final_doping = round(float(num[0]) + float(num[1]),3)
        reduced_comp = comp.replace(num[0]+'+'+num[1],str(final_doping))
        
        compositions[icomp] = reduced_comp
        comp_dict[comp] =  reduced_comp
    elif '/' in comp: 
        num = re.findall(".*([.\d-]+)/([.\d-]+).*([.\d-]+)/([.\d-]+).*",comp)[0]
        final_doping_1 = round(float(num[0]) / float(num[1]),3)
        final_doping_2 = round(float(num[2]) / float(num[3]),3)
        reduced_comp = comp.replace(num[0]+'/'+num[1],str(final_doping_1))
        reduced_comp = reduced_comp.replace(num[2]+'/'+num[3],str(final_doping_2))
        compositions[icomp] = reduced_comp
        comp_dict[comp] =   reduced_comp
   
       
        
       
for idNum in list(data.keys()): 
    if data2[idNum]['composition'] in list(comp_dict.keys()):
        old_comp = data2[idNum]['composition']
        data2[idNum]['composition'] = comp_dict[old_comp]
       
 
#################################################################################
# Fixes compositions with * and brackets
#################################################################################

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
compositions = []
comp_dict = {}
for idNum in list(data.keys()):
    compositions.append(data[idNum]['composition'])
    
    
for icomp,comp in enumerate(compositions):
    if '[' in comp: 
        revised_comp =  comp.replace("[",'(')
        revised_comp =  revised_comp.replace("]",')')
        comp_dict[comp] =  revised_comp
    else:
        revised_comp = comp
        
    
    if '*' in revised_comp:
        index_of_star = find(revised_comp,'*')
        step = 0
        for i in index_of_star:
            
           
            if not revised_comp[i+1-step].isdigit():
                revised_comp = revised_comp.replace('*',"", 1)
                step+=1
               
        # print(comp)
        # print(revised_comp)
        # print()
        comp_dict[comp] =  revised_comp

    if '*' in revised_comp:
        index1 = find(revised_comp,'*')[0]
        if revised_comp[index1+1].isdigit() and not revised_comp[index1+2].isdigit():
            multiplication_factor = revised_comp[index1+1]
            molecule = revised_comp[index1+2:]
            revised_comp =  revised_comp.replace(revised_comp[index1:],'('+molecule+')'+ multiplication_factor)
        elif revised_comp[index1+1].isdigit() and revised_comp[index1+2].isdigit():
            multiplication_factor = revised_comp[index1+1:index1+3]
            # print(comp)
            # print(multiplication_factor)
            molecule = revised_comp[index1+3:]
            revised_comp =  revised_comp.replace(revised_comp[index1:],'('+molecule+')'+ multiplication_factor)
        comp_dict[comp] =  revised_comp



for idNum in list(data.keys()): 
    if data2[idNum]['composition'] in list(comp_dict.keys()):
        old_comp = data2[idNum]['composition']
        data2[idNum]['composition'] = comp_dict[old_comp]
        
        
#################################################################################
# Fixes 
#################################################################################

compositions = []
comp_dict = {}
for idNum in list(data2.keys()):
    original_formula = data2[idNum]['composition']
    
    print(idNum)
    print(original_formula)
    original_comp = pmat.Composition(original_formula)
    proper_formula = original_comp.get_integer_formula_and_factor()[0]
    print(proper_formula)
    
    composition_dict = dict(pmat.Composition(proper_formula).as_dict())
    
    data2[idNum]['composition'] = proper_formula
    data2[idNum]['original_composition'] = original_formula
    data2[idNum]['composition_dict'] = composition_dict
    
    compositions.append(composition_dict)


with open('processed_neal_data.json', 'w') as fp:
    json.dump(data2, fp,indent = 4)
