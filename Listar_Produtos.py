
from produtos import produtos 



for produto in produtos:
    print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: R$ {produto['preço']:.2f}")
