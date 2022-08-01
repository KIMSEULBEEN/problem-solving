"""
BOJ 10815 숫자 카드
"""
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

numbers = dict()
for card in cards:
    numbers[card] = 1

M = int(input())
cards_test = list(map(int, input().split()))

answer = ""
for card in cards_test:
    print("1", end=" ") if card in numbers else print("0", end= " ")
print()