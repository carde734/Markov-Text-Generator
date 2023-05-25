from datetime import datetime
start_time = datetime.now()


import sys
import os 
import os.path





if len(sys.argv)==3:
    OutputFile=sys.argv[2]

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
    


    fileName = sys.argv[1]

    
   
    def Reads_Converts_FileTo_List(fileName,typeConv):
        
        #Reads the file with N lines and converts each line into an array with N elements
        
        fileObj = open(fileName, "r",encoding='utf-8') #opens the file in read mode
        words_out = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()

        if typeConv=="words":
            word_vec=[]
            for word in words_out:
                word_vec.append(word.split())

        elif typeConv=="letters":
            #first separates data into words so it can be separated to letters after
            word_vec=[]
            for line in words_out:
                for word in line:
                    word_vec.append(word)


        element_list = []
        # iterates over the vector of vectors of lines to convert it in a single vector with separate words
        for item in word_vec:
            # appending elements to the flat_list
            element_list += item

        # printing the resultant flat_list
        return(element_list)
               


    def Clean_Data(word_vec):
        #Cleans data in general, standardizes everything to lowcase, removes weird characters and return only alphabetic words
        #Data cleaning
        list_to_replace=[",","[","]","(",")","_",'"',"'","..","...","....",";",":","?","!","*","“","‘","”"]
        cleaned_words=[]    
        
        for i in range(0,len(word_vec)):
            #Converts every word to lower case
            word_vec[i]=word_vec[i].lower()

            for rep in list_to_replace:
                word_vec[i]=word_vec[i].replace(rep,"")

            if(len(word_vec[i])>1 and word_vec[i][-1]=="."):
                word_vec[i]=word_vec[i].replace(".","")

            if(len(word_vec[i])>1 and word_vec[i][-1]=="-"):
                word_vec[i]=word_vec[i].replace("-","")

            if(len(word_vec[i])>1 and word_vec[i][0]=="’"):
                word_vec[i]=word_vec[i].replace("’","")

            if(len(word_vec[i])>1 and word_vec[i][-1]=="’"):
                word_vec[i]=word_vec[i].replace("’","")
                
            if(word_vec[i].isalpha()==True):
                cleaned_words.append(word_vec[i])

        return cleaned_words
        

    def Makes_Dict_SortedCount(cleaned_words): 
        #Makes a dictionary that returns the frequency of words/letters sorted from the most common to the least common
        distinct_words = set(cleaned_words)
        dict_word_counts={}
        
        for dist_word in distinct_words:
            dict_word_counts[dist_word]=0
    
        for word in cleaned_words:
            dict_word_counts[word]=dict_word_counts[word] + 1
        
        sorted_dict_words = dict(sorted(dict_word_counts.items(), key=lambda x: x[1], reverse=True))
        return sorted_dict_words


    def Makes_Dict_Sucessors(ListofWords):
    
        #Makes a dictionary that contains the Successors and number of sucessors of the given ListofWords (for each word)
        DictAllWordSucessors={}
        
        for key in ListofWords:
            DictAllWordSucessors[key]=[]
    
        n=len(ListofWords)

        for word_index in range(0,n):
            if(word_index!=n-1):
                key_word=ListofWords[word_index]
                key_successor=ListofWords[word_index+1]
                DictAllWordSucessors[key_word].append(key_successor)


        DictWordSucessors={}
        

        for i in DictAllWordSucessors :
            DictWordSucessors[i]=Makes_Dict_SortedCount(DictAllWordSucessors[i])

        return DictWordSucessors

    
    
    def prints_results():
    
        #Function called when results needed to be printed

        #To print alphabetic letters
        print("\nAlphabetic letters sorted from most to least common:\n")
        for letter, count in sorted_dict_letters.items():
            print(letter,"-", count, "occurrences")

        print("\n\n")   
          

        #To print number of words
        print("There's a total of", number_of_words, "words")

        print("\n\n")

            
        #To print unique words
        print("There's a total of", len(unique_dict_words), "unique words")

        print("\n\n") 

        #To print top 5 common words and top 3 successors:
            
        print("\nTop 5 common words and top 3 successors :\n")    
        for key_id in topNwords:
            print(key_id,'(',sorted_dict_words[key_id], 'occurrences )'  )
            for sucessors_info, counts in DictWordSucessors[key_id].items():
                print('--',sucessors_info, ',',counts )
            print('\n')
            
        print('\n')
                
        

    def writes_output_file(OutputFile):
    
        #Function that writes the the results (same content of print_results()) inside a provided file by the user
    
        f= open(file=OutputFile, mode="w")
        
        
        f.write("Alphabetic letters sorted from most to least common:\n\n")
        for letter, count in sorted_dict_letters.items():
            f.write(letter+" - "+ str(count)+" occurrences\n")
      
        f.write("\n\nThere's a total of "+ str(number_of_words)+" words\n\n\n")
        
        f.write("There's a total of "+ str(len(unique_dict_words))+" unique words\n\n\n")
        
        f.write("Top 5 most common words and top 3 Successors are:\n\n")

        for key_id in topNwords:
            
            f.write(str(key_id) + '(' + str(sorted_dict_words[key_id]) + ' occurrences )\n' )

            for sucessors_info, counts in DictWordSucessors[key_id].items():
                f.write('--'+ str(sucessors_info) + ',' +  str(counts)+"\n")
            f.write("\n")
     
        f.close()
    



word_vec=Reads_Converts_FileTo_List(fileName, typeConv="words")

cleaned_WordsLetters = Clean_Data(word_vec)

#Dictionary with word count

#In order to make dictionary with word count, first we need to exclude the "lonely" letters
#  #Excludes "lonely" letters, since they are not considered words

OnlyWords=[]
for word in cleaned_WordsLetters:
    if(len(word)>1):
        OnlyWords.append(word)
        
        

sorted_dict_words=Makes_Dict_SortedCount(OnlyWords)
TopN = 5
topNwords= {count: sorted_dict_words[count] for count in list(sorted_dict_words)[:TopN]}


number_of_words=len(OnlyWords)


#Dictionary with letter count

letter_vec=Reads_Converts_FileTo_List(fileName, typeConv="letters")
cleaned_letters=Clean_Data(letter_vec)
sorted_dict_letters=Makes_Dict_SortedCount(cleaned_letters)


#Dictionary with unique words (word count =1)
unique_dict_words = dict(filter(lambda word: word[1] == 1, sorted_dict_words.items()))


#Dictionary with top X (5 for this task) word count and top N (3 for this task) sucessors
DictWordSucessors=Makes_Dict_Sucessors(OnlyWords)

for i in DictWordSucessors :
    DictSucess=DictWordSucessors[i]
    Top3Sucess= {count: DictSucess[count] for count in list(DictSucess)[:3]}
    DictWordSucessors[i]=Top3Sucess



#PRINTING RESULTS 


def main_results():
    #output file provided
    if len(sys.argv)==3:
        writes_output_file(OutputFile)
        print("\nAnalysis is written inside file",OutputFile)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
    else:
        print("\n")
        prints_results()
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))


if __name__ == "__main__":
   # It runs this only when not called via 'import'
    main_results()



   

