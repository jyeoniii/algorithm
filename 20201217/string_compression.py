# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for chunk_size in range(1, len(s)+1):
        chunks = [s[i:i+chunk_size] for i in range(0, chunk_size * (len(s) // chunk_size), chunk_size)]
        result, prev, cnt = '', '', 0
        for chunk in chunks + ['']:
            if chunk == prev:
                cnt += 1
            else:
                if cnt == 1: result += prev
                elif cnt > 1: result += str(cnt) + prev

                cnt = 1
                prev = chunk

        answer = min(answer, len(result) + len(s) % chunk_size)

    return answer
