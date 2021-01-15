# https://www.algoexpert.io/questions/Valid%20IP%20Addresses


def validIPAddresses(digits):
    answer = []

    def helper(string, li):
        if not string:
            if len(li) == 4: answer.append('.'.join(li))
            return
        elif len(li) >= 4:
            return

        for i in range(3):
            if i + 1 <= len(string):
                s = string[:i + 1]
                if not is_valid(s): continue
                li.append(s)
                helper(string[i + 1:], li)
                li.pop()

    helper(digits, [])
    return answer


def is_valid(string):
    num = int(string)
    if str(num) != string: return False
    return 0 <= num < 256
