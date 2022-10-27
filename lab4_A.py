# A program that writes to a file the numbers 1 to 100, their squares and square roots.
# Ensure this python file is saved in the same location as the file you want to write into

def write_numbers():
    file_name = input("What is the name of the file you want to write into? ")
    print("Starting the process") #prints on the IDLE
    infile = open(file_name, 'w')
    print("Number\tSquared\tSq.root",file = infile)
    print("------\t-------\t-------",file=infile)

    for i in range(1,101):
        import math
        print(i ,file = infile,end='') #print first range of numbers into column 1
        print("\t",i*i,file = infile,end='') #calculates square and writes into the file in column 2
        print("\t",round(math.sqrt(i),3),file=infile) #calculates the squareroot and writes into the file in column 3

    infile.close()
    print("Finished writing the file")


write_numbers()


def read_numbers():
    infile = open("1to100.txt", 'r')
    #allstr = infile.read()
    #print(allstr)

    
    for i in range(10): #prints first ten lines
        s = infile.readline()
        print(s[:-1]) #prints the lines without spaces in between the lines
    

    infile.close()


read_numbers()


def read_numbers2():
    infile = open("1to100.txt","r")
    #lines = infile.readlines()
    #print(lines)

    #for s in lines:
    for s in infile:
        print(s[:-1])

    infile.close()
    

read_numbers2()
    
