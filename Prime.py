j = 0;
n = int(input('digit the number: '))
count, result =1,1;
prime = [2,3,5,7,11,13,17,19,23,29,31,37,41]
for j in prime:
    result*=j;
    if(result <= n):
        count+=1;
    print(result)
print(count)
              
