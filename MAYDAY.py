string = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"



string_sliced = string.split(" ")
#print(string_sliced)

numbers = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7
           , "Eight" : 8, "Nine" : 9, "Zero" : 0, "Dash" : "-"}

for w in string_sliced:
    if w in numbers:
        print(numbers[w], end="")
    else:
        print(w[0], end="")