# https://www.algoexpert.io/questions/Reverse%20Words%20In%20String


def reverseWordsInString(string):
    l, r = len(string) - 1, len(string) - 1
    words = []
    while l >= 0:
        if string[l] == ' ':
            words.append(string[l + 1:r + 1])
            while l >= 0 and string[l] == ' ':
                words.append(' ')
                l -= 1
            r = l
        l -= 1

    words.append(string[:r + 1])
    return ''.join(words)