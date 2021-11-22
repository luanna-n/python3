nums = [1,2,3,4,5,6]

#regular way
def square(n):
    return n*n
print(list(map(square, nums)))

#lambdas - inline anonymous function
print(list(map(lambda n: n*n, nums)))
#lambda args: return expression