
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 00:13:49 2021

@author: lllang
"""

import re
import copy
import json
rf = open('CurieTemperature_data.txt' ,"r")
lines = rf.readlines()
rf.close()
no_comp_index = []
no_comp = []

comp = []
comp_index = []

doping_amt = []
doping_amt_index = []

doping_comp = []
doping_comp_index  = []

new_compounds = []
lines_with_x = []
lines_with_nothing = []
lines_taken_care_of = []
repeated_compounds = []
curie_temps = []
curie_temps2 = []

empty_list =[]

curie_dict = {}
j = 0
for iline in range(len(lines)):
    
    
    if '-' not in  lines[iline].split()[0] and '&' not in  lines[iline].split()[0] and '#' not in  lines[iline].split()[0] and lines[iline+1][0] != "-"  and lines[iline+1][0] != "&"  :
        print(iline)
        lines_with_nothing.append(lines[iline])
        curie_uncertain = []
        additional_info =[]
        line_numbers = []
        reference_numbers = []
        
        curie_uncertain.append(lines[iline].split()[1])
        line_numbers.append(iline)
        
        compound = lines[iline].split()[0]
        if '-' in lines[iline].split()[1]:
            curie_T = (float(lines[iline].split()[1].split('-')[0]) + float(lines[iline].split()[1].split('-')[1]))/2
        elif '±' in lines[iline].split()[1]:
            curie_T = float(lines[iline].split()[1].split('±')[0])
        elif '<' in lines[iline].split()[1]:
            curie_T = float(lines[iline].split()[1].replace('<',""))
        elif '>' in lines[iline].split()[1]:
            curie_T = float(lines[iline].split()[1].replace('>',""))
        else:
            curie_T = float(lines[iline].split()[1])
        
        if len(lines[iline].split()) !=1:
            additional_info.append(lines[iline].split()[3:])
            reference_numbers.append(lines[iline].split()[2])
          
        curie_dict.update({'id' + str(j) : {'composition': compound, 
                                            'curie_temperature': curie_T, 
                                            'curie_temperature_uncertaintity':  curie_uncertain,
                                            'reference_numbers': reference_numbers,
                                            'line_in_curie_file': line_numbers,
                                            'additional_info':additional_info
                                                    }})
        j+=1
        lines_taken_care_of.append(iline)
        
    ###Catches Hyphen Cases
    if iline + 1 != len(lines)  and lines[iline+1][0] == "-" and lines[iline][0] != '-':
        i=1
        curie_uncertain = []
        line_numbers = []
        reference_numbers = []
        empty_list.append(lines[iline])
        additional_info =[]
        compound = lines[iline].split()[0]
        avgCounter = 0
 
        curie_uncertain.append(lines[iline].split()[1])
        line_numbers.append(iline)
        avgCounter += 1
        if '-' in lines[iline].split()[1]:
            curie_T = (float(lines[iline].split()[1].split('-')[0]) + float(lines[iline].split()[1].split('-')[1]))/2
        elif '±' in lines[iline].split()[1]:
            curie_T = float(lines[iline].split()[1].split('±')[0])
        elif '<' in lines[iline].split()[1]:
            curie_T = float(lines[iline].split()[1].replace('<',""))
        elif '>' in lines[iline].split()[1]:
            curie_T = float(lines[iline].split()[1].replace('>',""))
        else:
            curie_T = float(lines[iline].split()[1])
        
        
        if len(lines[iline].split()) !=1:
            additional_info.append(lines[iline].split()[3:])
            reference_numbers.append(lines[iline].split()[2])
        #curie_T = float(lines[iline].split()[1])
        
        lines_taken_care_of.append(iline)
        
        # Deals with the dash cases
        while iline +i != len(lines) and "-" == lines[iline+i][0]:
            avgCounter += 1
            
            if '-' in lines[iline+i].split()[1]:
                curie_T += (float(lines[iline+i].split()[1].split('-')[0]) + float(lines[iline+i].split()[1].split('-')[1]))/2
            elif '±' in lines[iline+i].split()[1]:
                curie_T += float(lines[iline+i].split()[1].split('±')[0])
            elif '<' in lines[iline+i].split()[1]:
                curie_T += float(lines[iline+i].split()[1].replace('<',""))
            elif '>' in lines[iline+i].split()[1]:
                curie_T += float(lines[iline+i].split()[1].replace('>',""))
            else:
                curie_T += float(lines[iline+i].split()[1])
            # curie_T += float(lines[iline+i].split()[1])
            curie_uncertain.append(lines[iline+i].split()[1])
            empty_list.append(lines[iline+i])
            reference_numbers.append(lines[iline+i].split()[2])
            line_numbers.append(iline+i)
            lines_taken_care_of.append(iline+i)
            
            if len(lines[iline+i].split())>=2:
                additional_info.append(lines[iline+i].split()[3:])
            i+=1
           
        
        curie_T = float(curie_T)/avgCounter
        # curie_temps2.append(curie_T)
        
        curie_dict.update({'id' + str(j) : {'composition': compound, 
                                                    'curie_temperature': curie_T, 
                                                    'curie_temperature_uncertaintity':  curie_uncertain,
                                                    'reference_numbers': reference_numbers,
                                                    'line_in_curie_file': line_numbers,
                                                    'additional_info':additional_info
                                                    }})
        j+=1


  
    ###Catches doping cases with x 
    if 'x' in lines[iline].split()[0]:
        compound = lines[iline].split()[0]
        i = 1
        lines_with_x.append(iline)
        char = lines[iline + i].split()[0]
        
        
        
        
        
        
        lines_taken_care_of.append(iline)
        while char == '&':
            lines_taken_care_of.append(iline+i)
            # Catches Unique doping listings
            try: 
                if 'M' in lines[iline + i].split()[1]:
                    m = lines[iline + i].split()[2] 
                    compound = compound.replace("M" , m)
                    i+=1
                    continue
                
                if '<' in lines[iline + i].split()[2]:
                      x = str((float(lines[iline + i].split()[1]) + float(lines[iline + i].split()[5]))/2)
                      curie_T = lines[iline + i].split()[6]
                      reference_numbers = lines[iline + i].split()[7]
                    
                elif 'y' in lines[iline + i].split()[4]:
                    x = lines[iline + i].split()[3]
                    y = lines[iline + i].split()[6]
                    compound = compound.replace("y" , y)
                    curie_T = lines[iline + i].split()[7]
                    reference_numbers = lines[iline + i].split()[8]
                    
                else:
                      x = lines[iline + i].split()[3]
                      curie_T = lines[iline + i].split()[4]
                      reference_numbers = lines[iline + i].split()[5]
                     
            except: 
                reference_numbers = lines[iline].split()[-1]
                if 'M' in lines[iline + i].split()[1]:
                    m = lines[iline + i].split()[2] 
                    compound = compound.replace("M" , m)
                    i+=1
                    continue
                
                if '<' in lines[iline + i].split()[2]:
                      x = str((float(lines[iline + i].split()[1]) + float(lines[iline + i].split()[5]))/2)
                      curie_T = lines[iline + i].split()[6]
                    
                elif 'y' in lines[iline + i].split()[4]:
                    x = lines[iline + i].split()[3]
                    y = lines[iline + i].split()[6]
                    compound = compound.replace("y" , y)
                    curie_T = lines[iline + i].split()[7]

                else:
                      x = lines[iline + i].split()[3]
                      curie_T = lines[iline + i].split()[4]
            
            
            additional_info = lines[iline + i].split()[-1]

            curie_T_uncertainty  = copy.copy(curie_T)
            # Catches unique 2nd column cases
            if '±' in curie_T :
                #curie_T_uncertainty = '±' + curie_T.split('±')[1]
                curie_T  = curie_T.split('±')[0]
               
            elif '>=' in curie_T:
                
                curie_T = curie_T.replace('>=', "")
                #curie_T_uncertainty = '>=' + curie_T
            elif '<' in curie_T:
                
                curie_T = curie_T.replace('<', "")
                #curie_T_uncertainty = '<' + curie_T
                # curie_T_uncertainty = '<'
            elif '>' in curie_T:
         
                curie_T = curie_T.replace('>', "")
                #curie_T_uncertainty = '>' + curie_T
                # curie_T_uncertainty = '>'
            elif '-' in curie_T:               
                #curie_T_uncertainty = curie_T.split('-')[0] + '-' + curie_T.split('-')[1]
                curie_T = str((float(curie_T.split('-')[0]) + float(curie_T.split('-')[1])) /2)
            else:
                curie_T_uncertainty  = '=' + curie_T_uncertainty
            # print(reference_numbers)
            #print(additional_info)
            # print(curie_T_uncertainty)
            # print(reference_numbers) 
            # if curie_T == "":
            #     print(iline)
            # print(curie_T)
            curie_temps.append(curie_T)
            new_compounds.append(compound.replace("x" , x))
                
            
            char = lines[iline + i + 1].split()[0]
            
            curie_dict.update({'id' + str(j) : {'composition' : compound.replace("x" , x), 
                                                        'curie_temperature': curie_T, 
                                                        'curie_temperature_uncertaintity':  curie_T_uncertainty,
                                                        'reference_numbers': reference_numbers,
                                                        'line_in_curie_file' : str(iline + i + 1),
                                                        'additional_info':additional_info
                                                        }})
            lines_with_x.append(iline+i)
            i+=1
            j+=1


with open('curie_data.json', 'w') as fp:
    json.dump(curie_dict, fp,indent = 4)

lines2 = lines.copy()


def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)
delete_multiple_element(lines2,lines_taken_care_of)



with open('left_over_curie_data.txt', 'a') as the_file:
    for line in lines2:
        the_file.write(line)
# for iline in range(len(lines2)):
    
    # if lines[iline+1].split()[0][0] == '-':
        
    #     compound = lines[iline].split()[0]
    #     print(compound)