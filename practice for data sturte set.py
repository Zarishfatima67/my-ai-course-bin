book={12,'computer','lily',23.4}
print(book)
print(type(book))
print(len(book))

for x in book:
    print(x)

book.add('west')
print('book',book)
remove=book.discard('west')
print('remove:',book)