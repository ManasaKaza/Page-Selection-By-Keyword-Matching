import sys

page_dict = {}
query_dict = {}

#function for sorting the dictionary based on query strength
def sorting_of_pages(strength_dict):
    sorted_dict = dict(sorted(strength_dict.items(), key=lambda x: x[1], reverse=True))
    sorted_dict = {x: y for x, y in sorted_dict.items() if y != 0}
    result = ""
    for item in sorted_dict.keys():
        result += item + " "
        if len(result.strip().split(" ")) >= 5:
            break
    return result.strip()

#function for searching for the pages based on query keywords
def search(lst):
    strength_dict = {}
    for key in page_dict.keys():
        strength = 0
        list2 = page_dict[key]
        for i in range(len(lst)):
            if lst[i] in list2:
                strength += (8 - i) * (8 - list2.index(lst[i]))
        strength_dict[key] = strength
    return sorting_of_pages(strength_dict)

#function for parsing and adding the pages to the page dictionary
def add_page(string, page_id):
    words = string.lower()
    words = words.split(',')
    page_dict["P" + str(page_id)] = words

#function for parsing and adding the queries to the query dictionary
def add_query(string, query_id):
    words = string.lower()
    words = words.split(',')
    query_dict["Q" + str(query_id)] = words

#main function
def page_selection():
    page_id = 0
    query_id = 0
    for i in range(1,len(sys.argv),2):
        string = sys.argv[i].lower()
        if string == "":
            print("Blank input not accepted")
        elif string == "p":
            page_id += 1
            add_page(sys.argv[i+1],page_id)
            
        elif string == "q":
            query_id += 1
            add_query(sys.argv[i+1],query_id)
            
        elif string == "e":
            break


page_selection()

print("Query Pages")
for key in query_dict.keys():
    print(key + ": " + search(query_dict[key]))