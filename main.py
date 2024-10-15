class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - {self.preco:.2f}"

    def __eq__(self, outro):
        return self.preco == outro.preco and self.nome.lower() == outro.nome.lower()



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.first_node = None

    def __str__(self):
        valores = []
        current = self.first_node
        while current:
            valores.append(str(current.value))
            current = current.next
        return " -> ".join(valores)

    def add(self, value):
        new_node = Node(value)

        try:
            if isinstance(value, Product):
                if self.first_node is None:
                    self.first_node = (
                    new_node  # Se a lista estiver vazia, o novo nó é o primeiro
                )
                else:
                    current = self.first_node
                    while current.next:  # Percorre até o final
                        if value.nome > current.value.nome and value.nome < current.next.value.nome: #revisar, usar os __gt__, __lt__ p refinar
                            current.next = new_node# Adiciona o novo nó no final
                        current = current.next
                    
        except Exception: #ideal seria fazer uma exception customizada p lidar com este erro!
                print('Só instâncias de Produto são aceitas.')

    def remove(self, value):
        current = self.first_node
        anterior = None
        while current:
            if current.value == value:
                if anterior is None:  # Remover o primeiro nó
                    self.first_node = current.next
                else:
                    anterior.next = current.next  # Pular o nó removido
                return  # Termina após a remoção
            anterior = current
            current = current.next
        print(f"Valor {value} não encontrado na lista.")

    def position(self, value):
        current = self.first_node
        result = 0
        while current:
            if current.value == value:
                return result
            current = current.next
            result += 1
        return -1  # Indica que o value não foi encontrado


# Criando uma lista encadeada
lista = LinkedList()

# Adicionando elementos
lista.add(10)
lista.add(20)
lista.add(5)
lista.add(30)

print("Lista:", lista)  # Deve exibir: 10 -> 20 -> 30

# Removendo um elemento
lista.remove(20)
print("Lista após remove 20:", lista)  # Deve exibir: 10 -> 30

# Buscando a posição de um elemento
position = lista.position(30)
print(f"Posição de 30: {position}")  # Deve exibir: Posição de 30: 1


