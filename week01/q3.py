num=[3, 1, 4, 1, 5, 9, 2, 6]
num.sort()
print(num)
mid=len(num)//2
if len(num)%2==1:
    median=num[mid]
else:
    median=(num[mid]+num[mid+1])/2
print(median)