def isPalindrome(word):
    if not word:
        return True
    elif word[0].lower() == word[len(word)-1].lower():
        return isPalindrome(word[1:len(word)-1])
    else:
        return False