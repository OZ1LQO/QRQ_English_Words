#A routine that loads the 5000 most common words in english
#prepares a text file for ebook2cw.exe to be made into an mp3 file
#for morse code word practice.
#ebook2cw can be called diretly from the routine, producing an mp3 to bring around
#OZ1LQO 2014.04.28

import random
import os
import datetime
import time

def welcome():
    print("""\nWelcome to word generator 1.0 by OZ1LQO\n
This script will load the most common 5000 english words and
give you the opportunity to create files with selected words from
a certain range (always starting at the first word), or you can generate
a file with randomly selected words from a given range.
Note that the loaded words are sorted in order as to how common they
are, ie. word #23 is more common than word #123. And so forth.
You can also choose to generate an mp3 from the text file stored using
basic parameters: WPM, effective WPM and extra word spacing.
\nHave fun and best 73 DR OM!\n""")
          

def loadwords():
    """Import the words from the file.
    Format them and return the formatted list"""
    file = open("e5000_sorted.txt", "r")
    words = file.readlines()
    file.close()

    #Initialize the final, formatted, list of words
    wordlist = []

    #For each word, remove the \n 
    for word in words:
        word=word[:len(word)-1]
        #put them in the word list
        wordlist.append(word)

    print("\n..imported and formatted the words")
    
    
    return wordlist


def writefile(wordlist,wpm,effwpm,filename,call,wordspace):
    """Saves the generated word file on the hard drive"""
    #Get the current date
    year=datetime.date.today().strftime("%Y")
    month=datetime.datetime.now().strftime("%m")
    day=datetime.date.today().strftime("%d")
       
    #Initialize and build the output array
    output_init='vvvv '+call+' '+year+'-'+month+'-'+day+'  wpm '+wpm+'  effwpm '+effwpm+'  wsp '+wordspace+'   4 3 2 1  vvvv\n'
    output=[output_init]
    #Add a space to each word
    for word in wordlist:
        word+=(' ')
        output.append(word)
    #add a <AR><SK> to the end
    output.append('\n<AR><SK>\n')
    #write the file, adding the .txt type
    filename+='.txt'
    outputfile = open(filename, "w")
    outputfile.writelines(output)
    outputfile.close()
    print("\nWrote the file as ",filename)
    
    

def makemp3(wpm, effwpm, filename,wordspace):
    """Calls eebok2cw externally and makes an mp3-file from the generated text file"""
    #setup the correct command line
    #command=('ebook2cw ')
    command='ebook2cw '+filename+'.txt'+' -w '+wpm+' -e '+effwpm+' -o '+filename+' -W '+wordspace
    #call ebook2cw to generate the mp3
    print("\n..Called ebook2cw routine\n")
    os.system(command)
    input("\nPress ENTER to continue..")
    

    
def randwords_once(wordlist,wpm,effwpm,filename,call,wordspace):
    """Handles the generation of a file from randomized words up to a certain range
(each word gets presented only once)"""
    os.system('cls')
    print("""\nYou selected a file generation from randomized
words up to a certain range (each word gets presented only once)""")
    rnge=int(input("\nEnter the max range (max 5000):"))
    output=[]
    for i in range(0,rnge-1,1):
        output.append(wordlist[i])

    random.shuffle(output)
    print("\n..List generated")
    writefile(output,wpm,effwpm,filename,call,wordspace)
    input("\nPress ENTER to continue..")
    

def randwords_multiple(wordlist,wpm,effwpm,filename,call,wordspace):
    """Handles the generation of a file from randomized words up to a certain range
(words may be repeated)"""
    os.system('cls')
    print("""\nYou selected a file generation from randomized
words up to a certain range (words may be repeated)""")
    rnge=int(input("\nEnter the max range (max 5000):"))
    amount=int(input("\nHow many words do you want in the file? "))
    words=wordlist[:rnge-1]
    output=[]
    for i in range(0,amount-1,1):
        output.append(random.choice(words))

    print("\n..List generated")
    writefile(output,wpm,effwpm,filename,call,wordspace)
    input("\nPress ENTER to continue..")
    

def parameters(wpm,effwpm,filename,call,wordspace):
    """Allows the user to edit current parameters"""
   
    choice='1'
    while choice!='0':
        os.system('cls')
        print("\nCurrent Parameters are:")
        print("\n1) WPM: ",wpm)
        print("\n2) Effective WPM: ",effwpm)
        print("\n3) Filename: ",filename)
        print("\n4) Call: ",call)
        print("\n5) Extra wordspacing is:",wordspace,"seconds")
        choice=input("\nWhat do you want to change (0 exits with current parameters): ")
        if choice=='1':
            wpm=input("\nEnter new WPM: ")
        elif choice=='2':
            effwpm=input("\nEnter new effective WPM: ")
        elif choice=='3':
            filename=input("\nEnter new filename (extension defaults to .TXT): ")
        elif choice=='4':
            effwpm=input("\nEnter new Call Sign: ")
        elif choice=='5':
            wordspace=input("\nEnter new wordspacing in decimal seconds (eg. 0.5 or 1.5): ")

    return wpm,effwpm,filename,call,wordspace     
        
def printcurrent(filename):
    """Prints the current file (or any other if 'filename.txt' can be found in the folder"""
    os.system('cls')
    filename+='.txt'
    text_file=open(filename, "r")
    lines=text_file.readlines()
    print("\nCurrent file:\n")
    for line in lines:
        print(line)
    print("\n-done-\n")
    text_file.close()
    input("\nPress ENTER to continue..")


def showdir():
    """Listing current directory, sorting for extensions"""
    os.system('cls')
    print("\nText files in the directory:")
    for file in os.listdir():
        if file.endswith('.txt'):
            print(file)

    print("\nmp3 files in the directory:")
    for file in os.listdir():
        if file.endswith('.mp3'):
            print(file)
    print("\n\n")
    input("\nPress ENTER to continue..")

def main():
    """Main routine, imports the file and presents the options"""

    #set basic ebook2cw parameters
    wpm='20'
    effwpm='15'
    filename="output"
    call='OZ1LQO'
    wordspace='0'

    welcome()
    wordlist=loadwords()
    input("\nPress ENTER to continue..")

    

    select='1'
    while select!='0':
        os.system('cls')
        print("\nCurrent Parameters are:")
        print("\n1) WPM: ",wpm)
        print("\n2) Effective WPM: ",effwpm)
        print("\n3) Filename: ",filename)
        print("\n4) Call: ",call)
        print("\n5) Extra wordspacing is:",wordspace,"seconds")
        print("""\n\nWhat do you want to do:\n
1) Create a file from randomized words up to a certain range
(each word gets presented only once)\n
2) Create a file from randomly selected words up to a certain range
(words may be repeated)\n
3) Edit WPM, Effective WPM, Filename, Your Call or extra Wordspacing\n
4) Generate an mp3 sound file from the current file and parameters\n
5) Print the current file (be aware of it's length!)\n
6) List current text and mp3 files in the directory\n""")
        select=input("Select 1,2,3,4,5 or 6 (0 exits):")

        if select=='1':
            randwords_once(wordlist,wpm,effwpm,filename,call,wordspace)
        elif select=='2':
            randwords_multiple(wordlist,wpm,effwpm,filename,call,wordspace)
        elif select=='3':
            wpm,effwpm,filename,call,wordspace=parameters(wpm,effwpm,filename,call,wordspace)
        elif select=='4':
            makemp3(wpm, effwpm, filename,wordspace)
        elif select=='5':
            printcurrent(filename)
        elif select=='6':
            showdir()    

    print("\n73 DR OM ",call," BEST QRQ CW")
    input("\npress ENTER to exit")    
           
 

main()

    
