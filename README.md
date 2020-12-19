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

## [functools.lru_cache](https://docs.python.org/ko/3/library/functools.html)
* Sample: https://leetcode.com/problems/ones-and-zeroes/discuss/561642/Python-5-liner-top-down-dp

# Topics to Study
* 0-1 Knapsack Problem: A limit 안에서 구할 수 있는 B의 ... (최댓값, 가능 여부..)
* Bisect & Binary Search

# Impressive Problems :)
* [Maximum Product Subarray](https://github.com/jyeoniii/algorithm/blob/master/20201122/maximum_product_subarray.py)
* [Min Stack](https://github.com/jyeoniii/algorithm/blob/master/20201124/min_stack.py)
* [Subsets2](https://github.com/jyeoniii/algorithm/blob/master/20201203/subsets2.py)
* [Maximum Profit in Job Scheduling](https://github.com/jyeoniii/algorithm/blob/master/20201204/maximum_profit_in_job_scheduling.py)
* [Capacity to Ship Packages Within D Days](https://github.com/jyeoniii/algorithm/blob/master/20201205/capacity_to_ship_packages_within_d_days.py)
* [Ones and Zeros](https://github.com/jyeoniii/algorithm/blob/master/20201206/ones_and_zeros.py)
* [Partition Equal Subset Sum](https://github.com/jyeoniii/algorithm/blob/master/20201207/partition_equal_subset_sum.py)
* [Longest Substring With At Least K Repeating Characters](https://github.com/jyeoniii/algorithm/blob/master/20201209/longest_substring_with_at_least_k_repeating_characters.py)
* [Longest Increasing Subsequence](https://github.com/jyeoniii/algorithm/blob/master/20201212/longest_increasing_subsequence.py)
* [Burst Balloons](https://github.com/jyeoniii/algorithm/blob/master/20201213/burst_balloons.py)
* [Validate Binary Search Tree](https://github.com/jyeoniii/algorithm/blob/master/20201216/validate_binary_search_tree.py)
* [Three Sum](https://github.com/jyeoniii/algorithm/blob/master/20201219/three_sum.py)
* [Cherry Pickup II](https://github.com/jyeoniii/algorithm/blob/master/20201219/cherry_pickup2.py)