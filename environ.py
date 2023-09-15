import os
import dis

for i in os.environ:
    print(i)

os.environ['PYTHONADAPTIVE'] = '1'
os.environ['HAECHAN'] = '1'
print('--------------------------')

for i in os.environ:
    print(i)

print("아이고 의미없다")