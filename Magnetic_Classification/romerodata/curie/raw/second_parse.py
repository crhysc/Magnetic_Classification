#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 13:03:01 2021

@author: lllang
"""
import json

file_object = open('curie_data.json','r')
neal_dict = json.load(file_object)
j = len(neal_dict)



rf = open('left_over_curie_data_reformated.txt' ,"r")
lines = rf.readlines()
rf.close()
compounds =  [] 
lineNum = []
for iline in range(len(lines)):
    print(iline)
    if iline + 1 != len(lines)  and lines[iline+1][0] == "-" and lines[iline][0] != '-':
        i = 1
        neal_uncertain = []
        line_numbers = []
        additional_info = []
        reference_numbers = []
        compound = lines[iline].split()[0]
       
        avgCounter = 0
       
        neal_uncertain.append(lines[iline].split()[1])
        avgCounter += 1
        if '-' in lines[iline].split()[1]:
            neal_T = (float(lines[iline].split()[1].split('-')[0]) + float(lines[iline].split()[1].split('-')[1]))/2
        elif '±' in lines[iline].split()[1]:
            neal_T = float(lines[iline].split()[1].split('±')[0])
        elif '<' in lines[iline].split()[1]:
            neal_T = float(lines[iline].split()[1].replace('<',""))
        elif '>' in lines[iline].split()[1]:
            neal_T = float(lines[iline].split()[1].replace('>',""))
        else:
            neal_T = float(lines[iline].split()[1])
        
        
        
       
        reference_numbers.append(lines[iline].split()[2])
        if len(lines[iline].split()) ==4:
            additional_info.append(lines[iline].split()[3])
            
        #curie_T = float(lines[iline].split()[1])
        
       
        
        # Deals with the dash cases
        while iline +i != len(lines) and "-" == lines[iline+i][0]:
            avgCounter += 1
            
            if '-' in lines[iline+i].split()[1]:
                neal_T += (float(lines[iline+i].split()[1].split('-')[0]) + float(lines[iline+i].split()[1].split('-')[1]))/2
            elif '±' in lines[iline+i].split()[1]:
                neal_T += float(lines[iline+i].split()[1].split('±')[0])
            elif '<' in lines[iline+i].split()[1]:
                neal_T += float(lines[iline+i].split()[1].replace('<',""))
            elif '>' in lines[iline+i].split()[1]:
                neal_T += float(lines[iline+i].split()[1].replace('>',""))
            else:
                neal_T += float(lines[iline+i].split()[1])
            # curie_T += float(lines[iline+i].split()[1])
            neal_uncertain.append(lines[iline+i].split()[1])
         
            
            reference_numbers.append(lines[iline+i].split()[2])
            
            if len(lines[iline+i].split()) == 4:
              
       
                additional_info.append(lines[iline+i].split()[3])
            line_numbers.append(iline+i)
              
      
                
            i+=1
            
        neal_T = float(neal_T)/avgCounter
        neal_dict.update({'id' + str(j) : {'composition': compound, 
                                                'curie_temperature': neal_T, 
                                                'curie_temperature_uncertaintity':  neal_uncertain,
                                                'reference_numbers': reference_numbers,
                                                'line_in_neal_file': line_numbers,
                                                'additional_info':additional_info
                                                }})
        j+=1
        
        
    elif lines[iline][0] != '-':
            neal_uncertain = []
            line_numbers = []
            additional_info = []
            reference_numbers = []
            compound = lines[iline].split()[0]
            
            neal_uncertain.append(lines[iline].split()[1])
            
            
            if '-' in lines[iline].split()[1]:
                neal_T = (float(lines[iline].split()[1].split('-')[0]) + float(lines[iline].split()[1].split('-')[1]))/2
            elif '±' in lines[iline].split()[1]:
                neal_T = float(lines[iline].split()[1].split('±')[0])
            elif '<' in lines[iline].split()[1]:
                neal_T = float(lines[iline].split()[1].replace('<',""))
            elif '>' in lines[iline].split()[1]:
                neal_T = float(lines[iline].split()[1].replace('>',""))
            else:
                neal_T = float(lines[iline].split()[1])
                
                
            if len(lines[iline].split()) == 4:
                additional_info.append(lines[iline].split()[3])
            reference_numbers.append(lines[iline].split()[2])
            
            neal_dict.update({'id' + str(j) : {'composition': compound, 
                                                'curie_temperature': neal_T, 
                                                'curie_temperature_uncertaintity':  neal_uncertain,
                                                'reference_numbers': reference_numbers,
                                                'line_in_neal_file': line_numbers,
                                                'additional_info':additional_info
                                                }})
            
            
            
            j+=1
with open('curie_data_afterLeftOver.json', 'w') as fp:
    json.dump(neal_dict, fp,indent = 4)
            
            
            
            

