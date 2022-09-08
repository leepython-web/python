inputFile = open('input.txt', 'r', encoding='utf-8')
a = inputFile.read()
nums = a.split()
answer = int(nums[0]) + int(nums[1])
inputFile.close

outputFile = open('output.txt', 'w', encoding='utf-8')
outputFile.write(answer)
outputFile.close