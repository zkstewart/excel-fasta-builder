#! python3
# Excel_fasta_build
# A simple python program which allows the user to extract data in an Excel environment and convert this into a .fasta file
# This script is designed to rely solely on internal python processes (i.e., no importing of external packages) to make sure it is accessible to everyone without needing
# to figure out how to install packages with Python.

import os, time

# Instruct user on basic use
print('This script works by reading in two text files with corresponding transcript IDs and nucleotide/protein sequences.')
print('')

# Global value
outputText = ''

# Begin process with user inputs
print('Enter the name of the .txt file containing the transcript IDs here. Do not write the file extension here.')
while True:
        try:
                fileName = input()
                if os.path.isfile(fileName + '.txt') == False:
                        raise Exception
                print('First .txt file located successfully')
                break
        except:
                print('First .txt file failed to load. If you misspelt the name, try again. If this script isn\'t in the same directory as the .txt file, move it there then try again.')
                continue
print('')
print('Enter the name of the .txt file containing the nucleotide/protein transcripts here. Do not write the file extension here.')
while True:
        try:
                fileName2 = input()
                if os.path.isfile(fileName2 + '.txt') == False:
                        raise Exception
                print('Second .txt file located successfully')
                break
        except:
                print('Second .txt file failed to load. If you misspelt the name, try again. If this script isn\'t in the same directory as the .txt file, move it there then try again.')
                continue     
print('')
print('Enter the desired output .fasta file name. Do not write the file extension here.')
while True:
        try:
                outputFile = input()
                if os.path.isfile(outputFile + '.fasta') == True:
                        raise Exception
                break
        except:
                print('A file with this name already exists in this directory. Using this name will overwrite this file. Use a new name here, or move/delete/rename the previous file.')
                continue     

# Read in files
file1 = open(fileName + '.txt', 'r')
file1 = file1.read().split(sep='\n')
if file1[-1] == '':
        del file1[-1]

file2 = open(fileName2 + '.txt', 'r')
file2 = file2.read().split(sep='\n')
if file2[-1] == '':
        del file2[-1]

# Check that the user supplied properly formatted files
if len(file1) > len(file2):
        print('There are more lines in ' + fileName + '.txt than in ' + fileName2 + '.txt')
        print('This may be due to empty lines at the end of the file (in which case, remove them). Otherwise, fix this problem before running this script again. This window will automatically close in 20 seconds.')
        time.sleep(20)
        quit()

elif len(file2) > len(file1):
        print('There are more lines in ' + fileName2 + '.txt than in ' + fileName + '.txt')
        print('This may be due to empty lines at the end of the file (in which case, remove them). Otherwise, fix this problem before running this script again. This window will automatically close in 20 seconds.')
        time.sleep(20)
        quit()

# Join files in .fasta format
for i in range(len(file1)):
        outputText += '>' + file1[i] + '\n' + file2[i] + '\n'
outputText = outputText[:-1]

# Write to file
output = open(outputFile + '.fasta', 'w')
output.write(outputText)
output.close()
