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

## Python list의 `__lt__` 구현: 
* lexicographical: https://stackoverflow.com/questions/37287340/what-is-the-lt-actually-doing-for-lists

## collections.Counter
```
>>> from collections import Counter
>>> c1 = Counter("abc")
>>> c2 = Counter("bcd")
>>> c1
Counter({'a': 1, 'b': 1, 'c': 1})
>>> c2
Counter({'b': 1, 'c': 1, 'd': 1})
>>> c1 - c2
Counter({'a': 1})
```

## random
* https://wikidocs.net/79
```
>>> random.randrange(1,7)

>>> abc = ['a', 'b', 'c', 'd', 'e']
>>> random.shuffle(abc)
>>> abc
['a', 'd', 'e', 'b', 'c']

>>> random.choice(abc)
'a'
>>> random.choice(abc)
'd'
```


# Topics to Study
* 0-1 Knapsack Problem: A limit 안에서 구할 수 있는 B의 ... (최댓값, 가능 여부..)
* Bisect & Binary Search
* Monotone Stack

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
* [Jump Game IV](https://github.com/jyeoniii/algorithm/blob/master/20201227/jump_game4.py)
* [Shortest Path in a Grid with Obstacles Elimination](https://github.com/jyeoniii/algorithm/blob/master/20201228/shortest_path_in_a_grid_with_obstacles_elimination.py)
* [Longest Substring Without Repeating Characters](https://github.com/jyeoniii/algorithm/blob/master/20201229/longest_substring_without_repeating_characters.py)
* [Largest Rectangle in Histogram](https://github.com/jyeoniii/algorithm/blob/master/20201231/largest_rectangle_in_histogram.py)
* [Sum of SuaArray Minimums](https://github.com/jyeoniii/algorithm/blob/master/20210101/sum_of_subarray_minimums.py)
* [Unique Binary Search Trees2](https://github.com/jyeoniii/algorithm/blob/master/20210108/unique_binary_search_trees2.py)
* [Longest Consecutive Sequence](https://github.com/jyeoniii/algorithm/blob/master/20210112/longest_consecutive_sequence.py)
* [Redundant Connection](https://github.com/jyeoniii/algorithm/blob/master/20210112/redundant_connection.py)
* [Minimum Operations To Reduce X to Zero](https://github.com/jyeoniii/algorithm/blob/master/20210114/minimum_operations_to_reduce_x_to_zero.py)
* [Remove Zero Sum Consecutive Node from Linked List](https://github.com/jyeoniii/algorithm/blob/master/20210115/remove_zero_sum_consecutive_nodes_from_linked_list.py)
* [Sort List](https://github.com/jyeoniii/algorithm/blob/master/20210116/sort_list.py)
* [Find the Most Competitive Subsequence](https://github.com/jyeoniii/algorithm/blob/master/20210121/find_the_most_competitive_subsequence.py)
* [Sort K Sorted Array](https://github.com/jyeoniii/algorithm/blob/master/20210121/sort_k_sorted_array.py)
* [Path With Minimum Effort](https://github.com/jyeoniii/algorithm/blob/master/20210126/path_with_minimum_effort.py)
* [Min Rewards](https://github.com/jyeoniii/algorithm/blob/master/20210126/min_rewards.py)
* [Evaluate Divison](https://github.com/jyeoniii/algorithm/blob/master/20210127/evaluate_division.py)
* [Different Ways to Add Parenthesis](https://github.com/jyeoniii/algorithm/blob/master/20210211/different_ways_to_add_parenthesis.py)
* [Search a 2D Matrix II](https://github.com/jyeoniii/algorithm/blob/master/20210213/search_a_2d_matrix2.py)
* [Levenshtein Distance](https://github.com/jyeoniii/algorithm/blob/master/20210223/levenshtein_distance.py)
* [Score of Parentheses](https://github.com/jyeoniii/algorithm/blob/master/20210224/score_of_parentheses.py)
* [Longest String Chain](https://github.com/jyeoniii/algorithm/blob/master/20210308/longest_string_chain.py)
* [Sliding Window Median](https://github.com/jyeoniii/algorithm/blob/master/20210312/sliding_window_median.py)
* [Combination Sum](https://github.com/jyeoniii/algorithm/blob/master/20210422/combination_sum.py), [Combination Sum2](https://github.com/jyeoniii/algorithm/blob/master/20210422/combination_sum2.py), [Combination Sum4](https://github.com/jyeoniii/algorithm/blob/master/20210422/combination_sum4.py)