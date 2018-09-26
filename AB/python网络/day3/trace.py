import traceback
a = 10
try:
    b = a / '1'
except TypeError:
    # print(e)
    traceback.print_exc()

print("==================")