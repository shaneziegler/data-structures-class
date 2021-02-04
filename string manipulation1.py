def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    
    #Udacity solution
    word_list = our_string.split(" ")

    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)
    
    #My solution
    # words = our_string.split(' ')
    # new_words = ["" for x in range(len(words))]

    # for count, word in enumerate(words):
    #     new_word = ""
    #     for i in range(len(word)):
    #         new_word += word[len(word)-i-1]
    #     new_words[count] = new_word
    # return " ".join(new_words)


# print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
# print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")




def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    # TODO: Write your solution here
    if len(str1) != len(str2):
        return None
    distance = 0
    for x in range(len(str1)):
        if str1[x] != str2[x]:
            distance += 1
    return distance

print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")