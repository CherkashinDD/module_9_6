def all_variants(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


a = all_variants("abc")
for i in a:
    print(i)

'''
Вариант в котором порядок вывода как в примере
def all_variants(text):

    for i in range(len(text)):
        yield text[i]

    for start in range(len(text)):
        for end in range(start + 2, len(text) + 1):
            yield text[start:end]
            start += 1
            break

    for i in range(len(text)):
        yield text
        break


a = all_variants("abc")
for i in a:
    print(i)
'''