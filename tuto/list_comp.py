prizes = [5, 10, 50]

double_prizes = []
for prize in prizes:
    double_prizes.append(prize*2)
print(double_prizes)

#list comprehension method
double_prizes_comp = [ prize*2 for prize in prizes ]
print(double_prizes_comp)

#squaring numbers
nums = [1,2,3,4,5,6,7,8,9,10]
sqred = []
for num in nums:
    if (num **2) % 2 == 0:
        sqred.append(num**2)
print(sqred)

sqred_comp = [ num**2 for num in nums if (num**2) %2 == 0 ]
print(sqred_comp)

#(o que eu quero // for item in itens // condition se existir)