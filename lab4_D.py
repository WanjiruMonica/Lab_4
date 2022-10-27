#A program that finds sum and average of three different columns

def main():
    file_name = input("What is the name of the file? ")
    infile = open(file_name,"r")  #will open text file in write mode
    sum_of_numbers = 0
    sum_of_squares = 0
    sum_of_roots = 0

    
    lines = infile.readlines()
    lines2 = lines[2:]  #will read and return from line 3 i.e index 2 till the end of the file

    for i in lines2:
        b = str(i).split()  #since readlines() returns string split the string in order to access individual columns
        numbers = int(b[0])  #will access column 1 of every line then converts it to integer
        #print(numbers,end='')   #will print column 1
        sum_of_numbers = sum_of_numbers + numbers #calculate the values in that column
        average_of_numbers = (sum_of_numbers/100)

        squares = int(b[1])  #will access column 2 and convert to integer
        sum_of_squares = sum_of_squares + squares
        average_of_squares = (sum_of_squares/100)
        #print("\t",squares,end='') # will print column 2
    
        roots = float(b[2]) #will access column 3 and convert to integer
        #print("\t",roots) # will print column 3
        sum_of_roots = sum_of_roots + roots
        average_of_roots = (sum_of_roots/100)
    
    print("Each column has 100 numbers")
    print("Column: Number\tSquares \tRoots")
    print("Total: ",sum_of_numbers,"\t",sum_of_squares,"\t",sum_of_roots)
    print("Average: ",average_of_numbers,"\t",average_of_squares,"\t",round(average_of_roots,3))

    
main()
