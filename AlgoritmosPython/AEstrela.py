from VetorOrdenadoAdjacente import VetorOrdenadoAdjacente

class AEsrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False

    def buscar(self, atual):
        print('\nAtual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)

            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                AEsrela.buscar(self, self.fronteira.getPrimeiro())

from Mapa import Mapa

mapa = Mapa()
aestrenal  = AEsrela(mapa.curitiba)
aestrenal.buscar(mapa.portoUniao)
