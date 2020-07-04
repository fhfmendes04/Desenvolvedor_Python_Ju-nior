from collections import deque
minha_fila = deque(["joao", "Pedro", "Augusto"])
print(minha_fila)

# remover elemento
minha_fila.popleft()
print(minha_fila)

# Inserir elemento
minha_fila.append("Maria")
print(minha_fila)

