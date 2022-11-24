numbers = int(input())
def minimum(num):
    answer = list
    if num < 10:
        pass
    else:
        num = num // 10
        print(num)
        return minimum(num)

minimum(numbers)
