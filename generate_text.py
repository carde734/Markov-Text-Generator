from datetime import datetime
start_time = datetime.now()


import sys
import os 
import os.path
import random
from text_stats import * 


if len(sys.argv)!=4:
    print("A file, a starting word and a max number of words to be generated should be provided for the text generator program")
    exit()
  


if len(sys.argv)==1:
    print("A file should be provided to be analysed")
    exit()
  
  

elif os.path.splitext(sys.argv[1])[1] != ".txt":
    print("A txt file should be provided")
    exit()
    
elif os.path.exists(sys.argv[1]) == False:
    print("The file does not exist")
    exit()

 
        
else:
    
    file_name = sys.argv[1]
    StartingWord = sys.argv[2]
    MaxNumWords = sys.argv[3]
    

    def text_generator(file_name,StartingWord,MaxNumWords):
    
        #Receives a file name, a starting word and desired number of words as input. It uses the given file to generate sucessors in
        #the text for each word that will be selected randomnly in a weighted way (based on the number of times they succeed the word).
        #The generated file will have "MaxNumWords" words.

        cur_word=StartingWord
        MaxNumWords = int(MaxNumWords)
         
        msg=cur_word
        word_list = msg.split()
        number_of_words = len(word_list)
        
        #Reads the file with N lines and converts each line into an array with N elements
        word_vec=Reads_Converts_FileTo_List(fileName, typeConv="words")
        
        #Cleans data in general, standardizes everything to lowcase, removes weird characters and return only alphabetic words
        cleaned_WordsLetters =Clean_Data(word_vec)

        #Dictionary with word count

        #In order to make dictionary with word count, first we need to exclude the "lonely" letters
        #  #Excludes "lonely" letters, since they are not considered words

        OnlyWords=[]
        for word in cleaned_WordsLetters:
            if(len(word)>1):
                OnlyWords.append(word)
        
        

        #Dictionary with all words and sucessors ordered from the most to the least common
        DictWordSucessors=Makes_Dict_Sucessors(OnlyWords)
        
        ####################################################################################################################
        while number_of_words < MaxNumWords:
       
       
            #Creates list with sucessors and counts (weights) for the selected word
            SucessWords=[]
            SucessCounts=[]
       
            for words, counts in DictWordSucessors[cur_word].items():
                SucessWords.append(words)
                SucessCounts.append(counts)
                
            try:
                cur_word=random.choices(SucessWords, weights=SucessCounts, k=1) 
            except IndexError:
                print("Message: Word",cur_word,"is a terminal node")
                return(msg)
              
                
            cur_word="".join(map(str,cur_word))
       
            msg=msg+" "+cur_word
            word_list = msg.split()
            number_of_words = len(word_list)
       
    
        return(msg)
        
        
    #####RETURN RESULTS
    
    
        
Results=text_generator(file_name,StartingWord,MaxNumWords)
print("\n", Results)
 

       
end_time = datetime.now()
print('\nDuration: {}'.format(end_time - start_time))
