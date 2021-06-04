# CODE FOR CACHE SIMULATOR 
# This code can only simulate the working of a direct cache
# The set associtive functon is commented out, due to its wrong results to see its orking just un-comment the Setassociativefunction()

#funtions for each tag size 

def split(word): 
    return [char for char in word]


def tag1(j):
    tag_bit[j][0]=temp[6] #if tag size =1 then the value of tag_bit = temp[6] temp has address values stored from each line

def tag2(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]


def tag3(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]

def tag4(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]
    tag_bit[j][3]=temp[9]

def tag5(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]
    tag_bit[j][3]=temp[9]
    tag_bit[j][4]=temp[10]

def tag6(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]
    tag_bit[j][3]=temp[9]
    tag_bit[j][4]=temp[10]
    tag_bit[j][5]=temp[11]
def tag7(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]
    tag_bit[j][3]=temp[9]
    tag_bit[j][4]=temp[10]
    tag_bit[j][5]=temp[11]
    tag_bit[j][6]=temp[12]
def tag8(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]
    tag_bit[j][3]=temp[9]
    tag_bit[j][4]=temp[10]
    tag_bit[j][5]=temp[11]
    tag_bit[j][6]=temp[12]
    tag_bit[j][7]=temp[13]

def tag9(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]
    tag_bit[j][3]=temp[9]
    tag_bit[j][4]=temp[10]
    tag_bit[j][5]=temp[11]
    tag_bit[j][6]=temp[12]
    tag_bit[j][7]=temp[13]
    tag_bit[j][8]=temp[14]

def tag10(j):
    tag_bit[j][0]=temp[6]
    tag_bit[j][1]=temp[7]
    tag_bit[j][2]=temp[8]
    tag_bit[j][3]=temp[9]
    tag_bit[j][4]=temp[10]
    tag_bit[j][5]=temp[11]
    tag_bit[j][6]=temp[12]
    tag_bit[j][7]=temp[13]
    tag_bit[j][8]=temp[14]
    tag_bit[j][9] =temp[15]





#a_file = open(r"C:\Users\AALIYA AHMAD\Desktop\Results\Traces\adpcm.trace", "r")      # Use this line of code if you are running it in command prompt
a_file = open(r"Traces/adpcm.trace", "r")                                              # This line is to be used while opening file with WSL terminal 
address = 13      #after removing first 5 bits of the lines we are left with address size 13

block_size= int(input("block size")) # note that the size entered here is of the power of 2, so if the entered value of block_size is 4 it means block size is 2^4 = 16 Bytes
c = int(input("cache size'"))#10
set_size = c - block_size # c = cache_size
tag_size = address-block_size - set_size 
print("tag size",tag_size) 

i=0
rows= c
cols = tag_size
count = 0
hit =0
#frequency[address[i]]=[count+1]
cold_miss=0
actual_miss=0
History=[]
tag_bit = [[0 for i in range(cols)] for j in range(rows)] # declaring tag bit 
#print(tag_bit)
for line in a_file:
    temp = []
    word = line.strip()
    temp = split(line)
    address = line[6:len(line)-1] # saves values from bit 6 of a line till end of line-1....endofline-1 cause a line alays ends with \n and we don't need it in address
   # tag_try = line[6:6+tag_size]
   # set[i][0]= [tag_try , address]
   # i=i+1
    #print(set)
    #print(address)
    if(count<c):   # running it seperatly for first c size of cache to calculate cold misses 
        for j in range (0,c):
            if(tag_size == 1):
                tag1(j)

            if(tag_size == 2):
                tag2(j)

            if(tag_size==3):
                tag3(j)

            if(tag_bit == 4):
                tag4(j)

            if(tag_bit == 5):
                tag5(j)
                
            if(tag_bit == 6):
                tag6(j)

            if(tag_bit == 7):
                tag7(j)

            if(tag_bit == 8):
                tag8(j)

            if(tag_bit == 9):
                tag9(j)

            

           # print(tag_bit)
    count = count+1
    cold_miss = c*1
  

    valid=[0]*c #valid bit size is equal to cache size 
    for i in range(0,c):
        if (tag_bit[i]!= [0,0,0]):
            valid[i]=1



    if count>c:  #after first 10 bits 
        set_bit = temp[6:6+tag_size]
      #  print(set_bit)
        if (set_bit in tag_bit): # we have already saved set bits or new tag values using a temperory array, now we compare if the set_bit (tag values) matches with the tag_bit which is already there in cache, if they match and valid =1 print hit otherwise miss
            set = tag_bit.index(set_bit)
            if(valid[set]==1):
                hit= hit +1
            else:
                cold_miss = cold_miss +1

        else:
            actual_miss = actual_miss + 1
            for j in range (0,c):
                if(tag_size == 2):
                    tag1(j)

                if(tag_size == 3):
                   tag2(j)

                if(tag_size==3):
                    tag3(j)

                if(tag_bit == 4):
                    tag4(j)

                if(tag_bit == 5):
                    tag5(j)

                if(tag_bit == 6):
                    tag6(j)
                    
                if(tag_bit == 7):
                    tag7(j)

                if(tag_bit == 8):
                    tag8(j)

                if(tag_bit == 9):
                    tag9(j)
                
              #  print(tag_bit)

    if(tag_bit[0] not in History): #History bit is to store new tag values nd compare them later to find conflict misses
        History.append(tag_bit[0])
      #  print(History)
print("count",count)
print("hits",hit)
print("hit rate ",hit/count*100)
print("actual miss",actual_miss)
print("actual miss rate",actual_miss/count*100)
print("cold misses",cold_miss)
print("total misses",actual_miss+cold_miss)    
print("Total miss rate",(((actual_miss+cold_miss)/count)*100))


"""

# plotting hit vs miss rate using matplotlib, the plot doesn't show results hence excel was used to plot values
import matplotlib.pyplot as plt
x=hit
y = actual_miss
plt.plot(x,y)
plt.show()  """


#  N way set associative cache 
# The N-way set associative cache does not show correct results and hence is commented out, to see its working just un comment the function 
from collections import deque
addresses =[]
number_of_rows = c
address= addresses
ways = int(input ("enter value of n ")) 

"""
def simulateSetAssociative():
    tags = [[-1 for i in range(0, ways)] for i in range(0, number_of_rows)]  #declaring the tag, valid and LRU bits
    valid = [[0 for i in range(0, ways)] for i in range(0, number_of_rows)]
    LRU = [deque() for i in range(0,number_of_rows)]

    miss_count = 0
    total_instructions = 0

    for i in range(0, tag_size):
        for addr in addresses:
            offset = addr % block_size
            row = (addr // block_size) % number_of_rows
            tag = addr // (block_size * number_of_rows)
            print("Address: " + str(addr) + ", tag: " + str(tag) + ", row: " + str(row) + ", offset: " + str(offset), end="\t")
            flag = False
            if (tag in tags[row]) and (valid[row][tags[row].index(tag)]): # checking if our tag is in our row and its valid
                print("Hit")
                if i > 0:
                    total_instructions += 1
                continue # go to the next address, we found this one

            for j in range(0,ways): # if we couldn't find it, see if there is an open spot
                if valid[row][j] == 0:
                    tags[row][j] = tag
                    if j in LRU[row]:
                        LRU[row].remove(j)
                    LRU[row].append(j)
                    valid[row][j] = 1
                    flag = True
                    print("added value to the cache for the first time")
                    break
            if flag == False: # The tag did not match or was ncorrect
                leastUsedWay = LRU[row].popleft()
                tags[row][leastUsedWay] = tag
                if i > 0:
                    miss_count += 1
                LRU[row].append(leastUsedWay)
                print(" Miss - updating entry")

            if i > 0:
                total_instructions += 1
        print("END OF CYCLE: " + str(i))
        print("")

    print("row\tvalid\ttag\t|\tvalid\ttag")
    for j in range(0, number_of_rows):
        print(str(j) + "\t\t", end="")
        for k in range(0, ways):
            print(str(valid[j][k]) + "\t" + str(tags[j][k]) + "\t|\t",end="")
        print("")


    print("END")


simulateSetAssociative()

"""
# We tried writting the replacement policy but could not get it to work, mentioned below is the code for the same

# REPLACEMENT POLICY
#clock_counter = 0

#option = input("Enter the option for the replacement policy from 0 -> LRU; 1 ->> ;FU; 2 -> CLOCK PRO; 3 -> RANDOM: ")

#def rep_pol(option, new_address)
#	if (option == 0):			#LRU
#		cache_address.pop()		#pop the 0th address
#		for i in 1 to csize:
#			cache_address[i - 1] = cache_address[i]
#		cache_adress[count] = new_address
#
#	if (option == 1):			#LFU
#		temp_freq = frequency[0]
#		for itr in 1 to csize:		#to find the address with the lowest frequency
#			if frequency[itr] < temp_freq:
#				temp_freq = frequency[itr]
#				lfu_line = itr
#		cache_address[lfu_line] = new_address
#
#	if (option == 2):			#CLOCK
#		if (clock_counter == csize + 1):
#			clock_counter = 0
#		cache_adress[clock_counter] = new_address
#		clock_counter += 1;	
#
#	if (option == 3):			#RANDOM
#		line = random.randint(0,csize)
#		cache_address[count] = new_address