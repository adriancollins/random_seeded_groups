#########################################################
#Algorithm Notes:
#system create blank list of lists based on total number of goups + total size of groups
#
#Algorithm randomly assigns users on a group by group basis
#
#E.G.
#|  Team1  |  Team2  |  Team3  |
#| p1@a.com| p3@a.com| p2@a.com|
#| p5@a.com| p4@a.com| p2@b.com|
#| p1@b.com| p3@b.com| p1@c.com|
#
#ensures even(ish) distribution
#
#Order:
#         Team 1 | random from group 1
#         Team 2 | random from group 1
#         Team 3 | random from group 1
#         Team 1 | random from group 1
#         .....until group 1 is empty
#         then:
#         Team 1 | random from group 2
#         Team 2 | random from group 2
#         .....until all group members have been assigned.

import random
import math
from decimal import *
from sys import getsizeof




in_file = "test_data/email_test_data.txt"
out_file = "test_data/output_group.txt"

grp_size =3 #required output group size


###########################


##########################
##Read file into matrix###
##########################
curr_inc = 0
curr_input_grp = 0
curr_group = 0
GPN = []
CURR_GPN = []
sum_val = 0;
round_count = 0;
loop_count = 0;
f = open(in_file, 'r')
row_val = 0
count = 0
out_str = ""

for line in f:
        a =line.split(',')

        if(int(a[1]) > row_val):
           #row has changed
           row_val =int(a[1])
           count = 0
           GPN.append(CURR_GPN)
           #clear
           CURR_GPN = []

        CURR_GPN.insert(count,a[0])
        count = count+1

#tidy up last row
GPN.append(CURR_GPN)
##########################



##########################
##Generate Random Groups##
##########################

print("Random email group generator v1.0 \n")


err = 0
num_elements = 0
num_grps_init = len(GPN)

for x in range(0,num_grps_init):        #get total number of elements
    num_elements= num_elements+len(GPN[x])



#find the total number of output groups achieveable (round numbers)
num_grps_total = math.ceil(Decimal(num_elements) / Decimal(grp_size))
#print num_grps_total
print("Total number of participants: %d" % num_elements)
print("Total number of expected emails: %d \n" % num_grps_total)
curr_grp = 0
out_groups = [None]*int(num_grps_total)

############################################
##pre allocate the output list of lists
someListOfElements = ['']*int(grp_size) # size of each OP group
x = int(num_grps_total) #number of OP groups
out_list = []
for i in range(x):
    out_list.append([])
    for j in someListOfElements:
        out_list[i].append(j)
############################################
        

############################################
##Generate random groups
###########################################
curr_count = num_elements
while(curr_count > 0):
    curr_ran_mail = ""
    #print curr_group


    if(len(GPN[curr_input_grp]) >0):
        rand_sel = random.randint(0,len(GPN[curr_input_grp])-1)
        curr_ran_mail = GPN[curr_input_grp][rand_sel]
        del GPN[curr_input_grp][rand_sel]
    else:
        #move onto next input group
        curr_input_grp = curr_input_grp+1
        rand_sel = random.randint(0,len(GPN[curr_input_grp])-1)
        curr_ran_mail = GPN[curr_input_grp][rand_sel]
        del GPN[curr_input_grp][rand_sel]
    
    #jump around output groups
    out_groups[curr_group]=curr_count
    print("Out Group: %d  | In Group: %d  | Ran Val: %s  |  Round Count: %d" % (curr_group, curr_input_grp, curr_ran_mail, round_count))
    out_list[curr_group][round_count] = curr_ran_mail

    
    
    curr_group = curr_group+1
    if(curr_group == num_grps_total):
        curr_group = 0    


    #how many times have we gone around the block?
    loop_count = loop_count+1
    if(loop_count == int(num_grps_total)):
       loop_count = 0
       round_count = round_count+1
       
    curr_count = curr_count-1



        
##########################
##Write Results to File
##########################
f = open(out_file,'w')
for inc in range(0, int(num_grps_total)):
        for inc2 in range(0,len(out_list[inc])):
                f.write(out_list[inc][inc2]+';')
        f.write('|Group: %d \n' % (inc))
f.close()

print(out_list)
#Finsihed

print("fin")

