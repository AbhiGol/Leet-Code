from collections import defaultdict

def max_k_sum_pairs(nums, K):
    count = defaultdict(int)
    pair_count = 0

    for num in nums:
        complement = K - num

        if count[complement] > 0:
            pair_count += count[complement]
            count[complement] -= 1

        count[num] += 1

    return pair_count

array = [1, 2, 3, 4, 5]
K = 6
result = max_k_sum_pairs(array, K)
print(result) 