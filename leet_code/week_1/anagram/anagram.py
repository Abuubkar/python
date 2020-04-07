"""
Authors
----------
Primary: Abubakar Khawaja

Short Description:
----------
This file contains function that will group anagrams together from given array of strings. 
"""

from collections import defaultdict


def groupAnagrams(strs: [str]):
    """
    This function take array of string and adding new words by using key 
    made by their individual character in sorted order in form of tuple 
    """
    # it will contain Tuple as key and List of String as value
    sets = defaultdict(list)

    # Traversing each Word in String list given
    for word in strs:
        # Making Tuple to use as key and to use it for ease of saving its other anagrams

        # Saving it in dictionary in list where key is characters of word
        sets[tuple(sorted(word))].append(word)
        # could also use sets[''.join(sorted(word))].append(word) its better
        # ''.join(list) != str(list)

    # Extract List of anagrams from dictionary
    print(sets.values())
    return (sets.values())


groupAnagrams(["hos", "boo", "nay", "deb", "wow", "bop", "bob", "brr", "hey", "rye", "eve", "elf", "pup", "bum", "iva", "lyx", "yap", "ugh", "hem", "rod", "aha", "nam", "gap",
               "yea", "doc", "pen", "job", "dis", "max", "oho", "jed", "lye", "ram", "pup", "qua", "ugh", "mir", "nap", "deb", "hog", "let", "gym", "bye", "lon", "aft", "eel", "sol", "jab"])
