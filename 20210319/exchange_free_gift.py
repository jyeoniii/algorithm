# https://devth-preview.goorm.io/exam/53763/%EC%A3%BC-%EA%B5%AC%EB%A5%B4%EB%AF%B8-%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B3%B5%EA%B0%9C%EC%B1%84%EC%9A%A9-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/quiz/3


T = int(input())
for _ in range(T):
    N, M = map(int, input().split(" "))
    cnt = min(N//5, M//7)
    N -= cnt * 5
    M -= cnt * 7

    if N >= 5 and M > 0 and M + N >= 12:
        N -= 12 - M
        cnt += 1

    if N >= 12:
        cnt += N // 12

    print(cnt)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split(" "))
    answer = min(N//5, (N+M)//12)
    print(answer)