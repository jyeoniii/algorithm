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