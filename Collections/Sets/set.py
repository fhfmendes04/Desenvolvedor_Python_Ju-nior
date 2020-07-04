# Declaraçao de um set

meu_set = {1,2,3,4,1}
print(meu_set)

meu_set2 = set([1,2,8,9,10])
print(meu_set2)

meu_set3 = set([])
print(type(meu_set3))

# Adição
meu_set.add(5)
print(meu_set)

# update()
meu_set.update([3,4,5,6])
print(meu_set)

#discard()
meu_set.discard(2)
print(meu_set)

# União
print(meu_set | meu_set2)
print(meu_set.union(meu_set2))

# Interseção
print(meu_set & meu_set2)
print(meu_set.intersection(meu_set2))

# Diferença
print(meu_set - meu_set2)
print(meu_set2.difference(meu_set))

# Diferença simétrica
print(meu_set ^ meu_set2)
print(meu_set2.symmetric_difference(meu_set))





