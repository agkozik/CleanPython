my_list = [1, 2, 4, 7, 3]
my_list.sort()
# ---------------------------------------------------------------
for i in my_list:
    print(i)
# ---------------------------------------------------------------

for index, item in enumerate(my_list):
    print(f'{index}: {item}')
# 0: 1
# 1: 2
# 2: 3
# 3: 4
# 4: 7
# ----------------------------------------------------------------

emails = {
    'user1': '1@gmail.com',
    'user2': '2@gmail.com',
}

for name, email in emails.items():
    print(f'{name} = {email}')
# ------------------------------------------------------------------
# JAVA
# for (int i = a, i<n; i = i +s){
# sout(i)
# }

# Python
# for i in range(a, n, s):
#     print(i)