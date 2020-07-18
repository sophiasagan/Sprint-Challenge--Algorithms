'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC? - The Base Case?
    if len(word) <= 1:
        return 0
    # elif word[:2] == 'th':
    #     return count_th(word[1:]) + 1
    if word[0] == "t" and word[1] == "h":
        return count_th(word[2:]) + 1
    else:
        return count_th(word[1:])



print(count_th('bath'))
print(count_th('thatch'))
print(count_th('https'))
print(count_th('teach'))
print(count_th('thousandth'))

# 0
# 1
# 0
# 0
# 1
# something's wrong only counts at beginning of word


# passing