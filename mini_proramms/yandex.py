alice = list(input())
zeliboba = list(input())

answer = [i for i in range(len(alice))]
for i in answer:
    if zeliboba[i] == alice[i]:
        answer[i] = 'P'
        alice[i] = '0'
for i in range(len(alice)):
    if zeliboba[i] in alice and answer[i] != 'P':
        answer[i] = 'S'
        alice[alice.index(f'{zeliboba[i]}')] = '0'
    elif answer[i] != 'P':
        answer[i] = 'I'
print(''.join(answer))
