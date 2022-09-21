from numpy.random import randint

a = bin(100)  # binary of 100 = 0b1100100 len: 9
for i in range(0, len(a)):
    if a[i] == '1':
        # printing 1
        print('yes')

a_back = int(a, 2)
print(a_back)

# spyder
# code format: Ctrl + Alt + i


# r=range(100)

rand_var = [randint(0, 2, 90) for _ in range(100)]
rand_var_list = [randint(0, 2, 90).tolist() for _ in range(100)]
rand_list = randint(0, 2, 90).tolist()

assert stores_df.shape[1]==factory_df.shape[1]
