#You'll now write a program to encrypt plaintext into ciphertext using the Caesar cipher.
import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dic = {}
    count1 = 0
    count2 = 0
    
    for i in string.ascii_uppercase:
        dic[i] = string.ascii_uppercase[(shift+count1)%26]
        count1 = count1 + 1
        
    for i in string.ascii_lowercase:
        dic[i] = string.ascii_lowercase[(shift+count2)%26]
        count2 = count2 + 1
    return dic     

#Next, define the function applyCoder, which applies a coder to a string of text.

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    ans = ''
    for i in text:
        if i in string.ascii_lowercase:
            ans = ans + coder[i]
        elif i in string.ascii_uppercase:
            ans = ans + coder[i]
        else:
            ans = ans + i
    return ans

#Once you have written buildCoder and applyCoder, you should be able to use them to encode strings.

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
   
    return applyCoder(text,buildCoder(shift))

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    maxi = 0
    ans= 0
    for i in range(0,26):
        split1 = applyShift(text, i)
     
        count = 0
        split1 = split1.split(' ')
        for j in split1:
            if isWord(wordList, j):
                count = count + 1
        if count>maxi:
                maxi = count
                ans = i
                
    return ans
            

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    wordList = loadWords()
    s = getStoryString()
    bestshift = findBestShift(wordList, s)
    return applyShift(s, bestshift)