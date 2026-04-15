# x = lambda **kwargs: sum(kwargs.values())
# print(x(a=2,b=3,c=5))
def function(a: int, b: int):
    return (a<b and "b is bigger than a") or (a>b and "a is bigger than a") or "a and b are equal"
    # return (("a is bigger","a is equal to b")[a==b], "b is bigger")[a<b]

print(function(a=5,b=4))