result = int(input())

for i in range(result):
    sen = input()
    for i in range(len(sen)-1):
        if sen[i] != sen[i+1] and sen[i] in sen[i+1:]:
            result -= 1
            break
    
print(result)