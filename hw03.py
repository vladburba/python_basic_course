fruits = ["яблоко", "банан", "киви", "арбузjsdf"]
# Без key=len будет переводить в ASCII
max_elem = max(fruits, key=len)
print(max_elem)
right_offset = len(max_elem) + 15
# print(right_offset)
# https://lancelote.gitbooks.io/intermediate-python/content/book/enumerate.html
for index, item in enumerate(fruits, start=1):
    # print('{}. {:>{}}'.format(index, item, right_offset)) # второй способ
    print('{}. {}'.format(index, item.rjust(right_offset)))
