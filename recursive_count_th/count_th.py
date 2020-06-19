'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #takes in a string = ""
    # set the int counter to 0
    counter = 0
    #make sure theres more than 1 letter in the word
    if len(word) >= 2:
        #if there is, check to see letter at pos 0 is t and pos 1 is h
        if word[0] == 't' and word[1] == 'h':
            #add that word to the counter
            counter += 1
            #return the counter # starting 
            return counter + count_th(word[1:])
            #print it to see if its working
            print(word, "Counter is:", counter)
        else:
            return count_th(word[1:])
    else:
        return counter

count_th("thhoweuwoeuthwoefnwoethnowe")
count_th("hwkjfhkwejhkwjehcwjeth")
count_th("ththththtththththththth")

#passing :) 