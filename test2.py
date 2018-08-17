def calc_lettercase(alist):
    upper = 0
    lower = 0
    for letter in alist:
        if letter.isupper():
            upper += 1
        if letter.islower():
            lower += 1
    print("No. of Upper case characters: {}".format(upper))
    print("No. of Lower case characters: {}".format(lower))

samplestring = 'The Quick Brow 9837'
print(calc_lettercase(samplestring))
