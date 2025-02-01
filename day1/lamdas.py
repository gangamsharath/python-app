'''
def add5(val):
    return val+5

print(add5(100))
'''
'''
#single line function are called lamda functions
add5=val=val+5

print(add5(100))
'''
#or
'''
add5=lambda x:x+5
print(type(add5))
print(add5(100))
'''
sm=lambda x:True if x.startswith('M') else False
print(sm('murthy'))

#'''
# def check(x):
#   '''check fn takes value in stingre...'''
#    if x.startswith('M')
#      return True
#     else:
#       return False
      
# '''

# alist=['leanr','python','step','by','step']
# output=map(lambda x:x.upper(),alist)
# print(type(output))

# alist=['leanr','python','step','by','step']
# output=list(map(lambda x:x.upper(),alist))
# print(type(output))
# print(output)

scores = [66,90,69,58,76,60,88]
# def is_A_student(score):
#     return score > 75

# is_A_student = lambda score: score > 75

# over_75 = list(filter(is_A_student, scores))
# print(over_75)

# #sort
# list=[('eggs',525),('carrots',1.4),('honey',9.5)]
# list.sort(key=lambda x:x[1],reverse=0)
# print(list)

# import numpy as np
# x = np.array([1,2,3,4,5,6])
# squarer = lambda t: t ** 2
# squarers = np.array([squarer(xi) for xi in x])
# print(squarers)
