# A program that reads how many lines, words and characters a text file has.

def main():
    file_name = input("Which text file do you want to access? ")
    infile = open(file_name, 'r')
    number_of_lines = 0
    number_of_characters = 0
    number_of_words = 0

    for lines in infile:
            #print(lines[:-1])  # will print the lines in the text file without space in between the lines
            number_of_lines = number_of_lines + 1  #calculates number of lines

            for words in lines:
                words = len(lines.split())  #a single line will be split into its various words and the number of words counted using len.
            number_of_words = number_of_words + words #will calculate all words in all lines
    

            for characters in lines:
                number_of_characters = number_of_characters + 1  #each character in each line is added to find total
            

   
    print("The text file has",number_of_lines,"lines",end=',')
    print(number_of_words,"words",end=' and ')
    print(number_of_characters,"characters")

        
   


main()
