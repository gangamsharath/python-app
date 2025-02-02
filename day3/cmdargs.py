import sys

if len(sys.argv)>1:
    print("you have passed")
    for index, argval in enumerate(sys.argv):
        print(f"arg {index}: {argval}")
        print(f"your argument value is {argval}")
else:
    print("you have not passed any argument")