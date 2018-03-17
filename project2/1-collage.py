# Author: John Gauthier
# Description: Given a "magazine" of words, checks if a "collage" can be made for a given set of words. Words can only be used once.

import sys

def check_collage(num_mag, num_note, d_mag, l_note):
    
    if num_note > num_mag: #Print no if there are more words in the note than the magazine
        print("NO")
        return

    for word in l_note:
        if (word in d_mag.keys() and d_mag[word] > 0): #if the word is in the magazine and its value isnt 0 decrease its value by 1
            d_mag[word] -= 1
        else:
            print("NO")
            return
    print("YES")


def driver():

    with open(sys.argv[1]) as f:

        line1 = f.readline().split() #read numbers from first line

        num_mag = int(line1[0])
        num_note = int(line1[1])

        line2 = f.readline().split() 

        d_mag = {x: line2.count(x) for x in line2} #make dictionary from second line. Keys are word, values are number of times that word appears

        line3  = f.readline().split()

        check_collage(num_mag, num_note, d_mag, line3)



if __name__ == "__main__":
    driver()
