#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lab03

Avnika Manaktala 

This file reads a text file with comma separated data, converts the columns 
into a dictionary and stores each column in a list. Various computations are 
made from this data including mean and average distance of the raccoon. 
A new file is then created using the computed data. 

"""
import math

#Part 1- Opening and reading the contents of the data file

raccoon_data= open("2008Male00006.txt", "r")
header=raccoon_data.readline()
print(header) #Displaying header for each column
lines = raccoon_data.readlines()
raccoon_data.close()

#Part 2- Storing data into a Dictionary

Data = [0]*len(lines) #Creating empty list equivalent to file size

#Part 3- Assigning number type to column 

for lidx in range(len(lines)-1): 
    Data[lidx]=lines[lidx].split(",") #Split lines based on separation flag
    Data[lidx][3]=int(Data[lidx][3]) 
    Data[lidx][8:15]=map(float,Data[lidx][8:15]) 
    Data[lidx][4:6]=map(float,Data[lidx][4:6])

dictionary_raccoon=dict() #Creating empty dictionary

header=header.split(",") #Converting columns into list 


lst=[[0]*14]*15 #Creating blank list of lists 
for lidx in range(15):
    lst[lidx]=[]

for lidx in range(15): #Adding values from the file into the list
    for lidy in range(14):
        lst[lidx].append(Data[lidy][lidx])
       
for lidx in range(15): #Creating required dictionary
    dictionary_raccoon[header[lidx]]=lst[lidx]       
    

#Part 4- Computing key statistics such as mean, sum and distance

def avg(x): #Defining mean function
    print(sum(x)/len(x))

avg_MSL= avg(dictionary_raccoon['MSL']) #Mean of list
   
def total(x): #Defining sum function
    print(sum(x))
total(dictionary_raccoon['MVL']) #Sum of List

def distance(lat,long): #Defining distance function
    dist=[]
    for x in range(len(lat)-1):
        dist.append(((math.sqrt(((lat[x]-lat[x+1])**2.0)+((long[x]-long[x+1])**2.0)))))
    return dist

#Part 5- Adding George's movement to data dictionary

dictionary_raccoon["Distance"]=[0] #Adding 0 to the begining of the distance list
dictionary_raccoon["Distance"].extend(distance(dictionary_raccoon[' X'],dictionary_raccoon[' Y']))

distance(dictionary_raccoon[' X'],dictionary_raccoon[' Y']) #Computing distance

avg(dictionary_raccoon['Energy Level']) #Computing average energy level

avg(dictionary_raccoon[' X']) #Computing average distance in X
avg(dictionary_raccoon[' Y']) #Computing average distance in Y

total(dictionary_raccoon['Distance']) #Total distance travelled

#Part 6- Creating new file
new_file=open("amanakta_Georges_life.txt", "w")


L=['Raccoon name: George \n','Average Location: 591189.03,4504604.08 \n',
   'Distance Travelled: 593.9 \n','Average Energy level: 563.6 \n',
   'Raccoon End State: DEAD \n'] #Header for georges_life.txt file
new_file.writelines(L)
new_file.flush()


new_file.write('\n') #Writing column names for data
CN=['Date','Time','X','Y','Asleep Flag','Behavior Mode','Distance Travelled']
new_file.write("\t".join(CN))
new_file.flush()


  
for lidx in range(14): #Converting floats to strings
    dictionary_raccoon[' X'][lidx]=str(dictionary_raccoon[' X'][lidx])
    dictionary_raccoon[' Y'][lidx]=str(dictionary_raccoon[' Y'][lidx])
    dictionary_raccoon['Distance'][lidx]=str(dictionary_raccoon['Distance'][lidx])
    

#Tab delimited data points
new_file.write('\n')
date=dictionary_raccoon['Day']
new_file.write("\t".join(date))
new_file.flush()

new_file.write('\n')
time=dictionary_raccoon['Time']
new_file.write("\t".join(time))
new_file.flush()

new_file.write('\n')
Xdist=dictionary_raccoon[' X']
new_file.write("\t".join(Xdist))
new_file.flush()

new_file.write('\n')
Ydist=dictionary_raccoon[' Y']
new_file.write("\t".join(Ydist))
new_file.flush()

new_file.write('\n')
Asleep=dictionary_raccoon[' Asleep']
new_file.write("\t".join(Asleep))
new_file.flush()

new_file.write('\n')
Behavior=dictionary_raccoon['Behavior Mode']
new_file.write("\t".join(Behavior))
new_file.flush()

new_file.write('\n')
Dist=dictionary_raccoon['Distance']
new_file.write("\t".join(Dist))
new_file.flush()



