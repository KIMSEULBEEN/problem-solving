a = 'abcdcde'
a = a.replace('cd','1')


croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
len_croa = len(croa)

input_arr = input()

for n in range(len_croa):
    input_arr = input_arr.replace(croa[n],'1')


print(len(input_arr))
