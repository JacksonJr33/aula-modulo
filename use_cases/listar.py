from repositorio import banco

def listarProdutos():
    print('_____ LIST ADE PRODUTOS _____')
    for produto in banco:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")
        print('_'*100)

if __name__ == '__main__':
    adicionarProduto('Mouse', 'Perfericos', 135.00)
    adicionarProduto('Monitor Philco', 'Monitores', 750.00)
    listarProdutos()