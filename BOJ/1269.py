"""
BOJ 1269 대칭 차집합
"""
import sys
input = sys.stdin.readline

len_nums1, len_nums2 = list(map(int, input().split()))
nums1 = set(list(map(int, input().split())))
nums2 = set(list(map(int, input().split())))

print(len_nums1 + len_nums2 - len(nums1 & nums2) * 2)