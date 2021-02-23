# https://www.algoexpert.io/questions/Kadane's%20Algorithm


def kadanesAlgorithm(array):
	curr_sum = answer = float("-inf")
	for num in array:
		curr_sum = max(curr_sum + num, num)
		answer = max(answer, curr_sum)
	return answer
