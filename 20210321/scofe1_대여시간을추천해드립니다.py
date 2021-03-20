# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
times = [input().split(" ~ ") for _ in range(N)]
start = max(t[0] for t in times)
end = min(t[1] for t in times)

print(f"{start} ~ {end}" if start < end else -1)
