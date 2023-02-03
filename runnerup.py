'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up n score. You are given scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.'''




n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)
second = 0

for num in arr:
    if num == mx:
        pass
    elif second == 0:
        second = num
    elif num > second:
        second = num

print(second)