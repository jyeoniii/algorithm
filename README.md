# Python for algorithm
## Heap
- https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate
  - MinHeap만 지원
  - custom comparator를 지정하고 싶다면, `__lt__`을 오버라이드
  ```
  def __lt__(self, other):
      return self.val < other.val
  ----------------------------------------------------------------------
  setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
  ```
  
## DefaultDict
인자로 주어진 객체의 기본값을 딕셔너리의 초기값으로 지정 가능
```
from collections import defaultdict

word_d = defaultdict(list)
    for word in wordDict:
        word_d[word[0]].append(word)
```

