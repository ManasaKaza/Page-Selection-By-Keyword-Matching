import operator

def sorting_of_pages(dict1)->str:                                                      # Sorting_of_Pages()
    string1 = ''                                                                       # Function for sorting the Dictionary based on
    sorted_d = dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)) # Query Weight
    sorted_d ={x:y for x,y in sorted_d.items() if y!=0}
    maxpage_limit = 1
    for item in sorted_d.keys():
        if maxpage_limit > 5:
            break
        string1 = string1 + item + ' '
        maxpage_limit +=1
    return(string1.strip())

def search(lst):                                                                       # Search()
    dict1={}                                                                           # Function for Searching the Pages based on Query
    for key in page_dict.keys():                                                       # Keywords
        weight = 0
        list2 = page_dict[key]
        for i in range(len(lst)):
            if lst[i] in list2:
                weight += (9-i)*(9-list2.index(lst[i]))
        dict1[key] = weight
    return(sorting_of_pages(dict1))

def page(string:str,counter:int):                                                     # Page()
    string = string[2:]                                                               # Function for Adding the Page Keywords into
    string = string.lower()                                                           # Page_Dict{} Dictionary
    list1  = string.split()
    page_dict['P' + str(counter)] = list1

def query(string:str,counter:int):                                                    # Query()
    string = string[2:]                                                               # Function for Adding the Query Keywords into
    string = string.lower()                                                           # Query_Dict{} Dictionary
    list1  = string.split()
    query_dict['Q' + str(counter)] = list1

page_dict={}
query_dict={}

def page_selection():                                                                 # Main function : Page_selection()
    count_of_pages = 1                                                                # Reads the Input from the Text File and
    count_of_queries = 1                                                              # Passes each line into Page() and Query()
    File = open('input.txt','r')                                                      # Based on First character
    for line in File:
        if line[0] == "P" or line[0] == "p":
            page(line,count_of_pages)
            count_of_pages += 1

        if line[0] == "Q" or line[0] == "q":
            query(line,count_of_queries)
            count_of_queries += 1

        if line[0] == "E" or line[0] == "e":
            break
page_selection()
print("QUERY PAGES")
for key in query_dict.keys():
    print(key + ": "+ search(query_dict[key]))
