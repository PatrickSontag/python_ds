def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return (len(str(num1)) == len(str(num2)))

    #  # you need to identify the number and the frequency
    # def freq_counter(passed):
    #     '''Return the frequency of passed in arguement'''

    #     counts = {}

    #     for num in passed:
    #         counts[num] = counts.get(num,0) +1
    #         # print(counts)
    #         # this is assigning the key value based on index

    #     return counts
    # print("str(num1) ", str(num1))
    # print("str(num2) ", str(num2))
    # print("freq_counter(str(num1))", freq_counter(str(num1)))
    # print("freq_counter(str(num2))", freq_counter(str(num2)))

    # set1 = {1,2,3}
    # set2 = {2,1,3}
    # print("set1 = set2?", set1 == set2)

    
    # return freq_counter(str(num1)) == freq_counter(str(num2))
    # # returns true/ false after stringifying the result of freq_counter w/ num1/ num2 passed in