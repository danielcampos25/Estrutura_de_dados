class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome  = nome
        self.altura = altura
        self.idade = idade
   
    def falar(self):
        print('Olá')

    def imprimeInfo(self):
        print(self.nome,self.altura,self.idade,self.profissao,self.usuario)
    pass

