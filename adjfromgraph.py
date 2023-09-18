import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def __len__(self):
        return self.size
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val),end='')
            print("\n")
def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    
    #1
    g_antlia = Graph(4)
    g_antlia.add_edge(0,2)
    g_antlia.add_edge(0,3)
    g_antlia.add_edge(1,3)
    g_antlia.add_edge(0,1)
    g_antlia.add_edge(1,2)

    #2
    g_apus = Graph(5)
    g_apus.add_edge(0,1)
    g_apus.add_edge(1,2)
    g_apus.add_edge(2,3)
    g_apus.add_edge(3,4)

    #3
    g_aquila = Graph(10)
    g_aquila.add_edge(0,1)
    g_aquila.add_edge(0,6)
    g_aquila.add_edge(1,4)
    g_aquila.add_edge(4,2)
    g_aquila.add_edge(4,7)
    g_aquila.add_edge(4,5)
    g_aquila.add_edge(2,8)
    g_aquila.add_edge(2,5)
    g_aquila.add_edge(5,9)
    g_aquila.add_edge(9,3)
    g_aquila.add_edge(3,7)
    
    #4
    g_ara = Graph(8)
    g_ara.add_edge(0,1)
    g_ara.add_edge(5,1)
    g_ara.add_edge(1,7)
    g_ara.add_edge(7,2)
    g_ara.add_edge(2,6)
    g_ara.add_edge(6,4)
    g_ara.add_edge(4,3)
    g_ara.add_edge(3,0)

    #5    
    g_aries = Graph(9)
    g_aries.add_edge(0,6)
    g_aries.add_edge(0,1)
    g_aries.add_edge(0,2)
    g_aries.add_edge(0,5)
    g_aries.add_edge(1,3)
    g_aries.add_edge(2,8)
    g_aries.add_edge(5,4)
    g_aries.add_edge(5,7)

    #6    
    g_camelpardalis = Graph(8)
    g_camelpardalis.add_edge(0,7)
    g_camelpardalis.add_edge(0,2)
    g_camelpardalis.add_edge(2,3)
    g_camelpardalis.add_edge(3,4)
    g_camelpardalis.add_edge(4,1)
    g_camelpardalis.add_edge(2,5)
    g_camelpardalis.add_edge(5,6)

    #7   
    g_centaurus = Graph(20)
    g_centaurus.add_edge(0,1)
    g_centaurus.add_edge(1,4)
    g_centaurus.add_edge(4,6)
    g_centaurus.add_edge(4,3)
    g_centaurus.add_edge(6,3)
    g_centaurus.add_edge(6,11)
    g_centaurus.add_edge(11,10)
    g_centaurus.add_edge(10,14)
    g_centaurus.add_edge(14,8)
    g_centaurus.add_edge(8,15)
    g_centaurus.add_edge(10,2)
    g_centaurus.add_edge(0,2)
    g_centaurus.add_edge(2,16)
    g_centaurus.add_edge(16,17)
    g_centaurus.add_edge(17,6)
    g_centaurus.add_edge(17,5)
    g_centaurus.add_edge(5,9)
    g_centaurus.add_edge(3,13)
    g_centaurus.add_edge(13,7)
    g_centaurus.add_edge(7,12)
    g_centaurus.add_edge(13,18)
    g_centaurus.add_edge(18,19)

    #8
    g_chamaeleon = Graph(6)
    g_chamaeleon.add_edge(0,1)
    g_chamaeleon.add_edge(1,2)
    g_chamaeleon.add_edge(2,3)
    g_chamaeleon.add_edge(3,4)
    g_chamaeleon.add_edge(4,5)
    g_chamaeleon.add_edge(5,0)
    
    #9
    g_circinus= Graph(4)
    g_circinus.add_edge(0,1)
    g_circinus.add_edge(2,1)
    g_circinus.add_edge(0,3)

    #10
    g_CoronaAustralis=Graph(6)
    g_CoronaAustralis.add_edge(2,1)
    g_CoronaAustralis.add_edge(0,1)
    g_CoronaAustralis.add_edge(2,3)
    g_CoronaAustralis.add_edge(3,4)
    g_CoronaAustralis.add_edge(4,5)

    #11
    g_CoronaBorealis=Graph(7)
    g_CoronaBorealis.add_edge(2,1)
    g_CoronaBorealis.add_edge(0,1)
    g_CoronaBorealis.add_edge(2,3)
    g_CoronaBorealis.add_edge(3,4)
    g_CoronaBorealis.add_edge(4,5)
    g_CoronaBorealis.add_edge(6,5)

    #12
    g_Corvus=Graph(5)
    g_Corvus.add_edge(0,1)
    g_Corvus.add_edge(1,2)
    g_Corvus.add_edge(2,3)
    g_Corvus.add_edge(3,4)
    g_Corvus.add_edge(3,0)

    #13
    g_crater=Graph(8)
    g_crater.add_edge(2,1)
    g_crater.add_edge(0,1)
    g_crater.add_edge(2,3)
    g_crater.add_edge(3,4)
    g_crater.add_edge(4,5)
    g_crater.add_edge(6,5)
    g_crater.add_edge(6,7)
    g_crater.add_edge(2,5)

    #14   
    g_Delphinus=Graph(5)
    g_Delphinus.add_edge(2,1)
    g_Delphinus.add_edge(0,1)
    g_Delphinus.add_edge(2,3)
    g_Delphinus.add_edge(3,4)
    g_Delphinus.add_edge(1,4)

    #15
    g_Equuleus=Graph(3)
    g_Equuleus.add_edge(2,1)
    g_Equuleus.add_edge(0,1)

    #16
    g_fornax=Graph(4)
    g_fornax.add_edge(3,0)
    g_fornax.add_edge(1,2)
    g_fornax.add_edge(2,3)
    g_fornax.add_edge(0,1)

    #17
    g_horlogium=Graph(7)
    g_horlogium.add_edge(1,0)
    g_horlogium.add_edge(1,2)
    g_horlogium.add_edge(2,3)
    g_horlogium.add_edge(3,4)
    g_horlogium.add_edge(4,5)
    g_horlogium.add_edge(5,6)

    #18
    g_indus=Graph(5)
    g_indus.add_edge(4,0)
    g_indus.add_edge(1,4)
    g_indus.add_edge(2,1)
    g_indus.add_edge(3,2)
    g_indus.add_edge(3,0)

    #19
    g_lacerta=Graph(9)
    g_lacerta.add_edge(1,0)
    g_lacerta.add_edge(1,2)
    g_lacerta.add_edge(2,3)
    g_lacerta.add_edge(3,4)
    g_lacerta.add_edge(4,5)
    g_lacerta.add_edge(5,6)
    g_lacerta.add_edge(6,7)
    g_lacerta.add_edge(7,8)

    #20
    g_leominor=Graph(5)
    g_leominor.add_edge(1,0)
    g_leominor.add_edge(1,2)
    g_leominor.add_edge(2,3)
    g_leominor.add_edge(2,4)
    g_leominor.add_edge(4,0)

    #21
    g_lynx=Graph(8)
    g_lynx.add_edge(1,0)
    g_lynx.add_edge(1,2)
    g_lynx.add_edge(2,3)
    g_lynx.add_edge(3,4)
    g_lynx.add_edge(4,5)
    g_lynx.add_edge(6,7)
    g_lynx.add_edge(6,5)

    #22
    g_Mensa=Graph(4)
    g_Mensa.add_edge(2,1)
    g_Mensa.add_edge(0,1)
    g_Mensa.add_edge(2,3)
    
    #23
    g_microscopium =Graph(6)
    g_microscopium.add_edge(0,1)
    g_microscopium.add_edge(2,1)
    g_microscopium.add_edge(2,4)
    g_microscopium.add_edge(3,0)
    g_microscopium.add_edge(5,3)
    
    #24
    g_musca =Graph(6)
    g_musca.add_edge(0,1)
    g_musca.add_edge(2,1)
    g_musca.add_edge(2,4)
    g_musca.add_edge(0,5)
    g_musca.add_edge(0,4)
    g_musca.add_edge(5,3)

    #25
    g_pavo =Graph(11)
    g_pavo.add_edge(0,2)
    g_pavo.add_edge(2,1)
    g_pavo.add_edge(7,1)
    g_pavo.add_edge(7,0)
    g_pavo.add_edge(2,4)
    g_pavo.add_edge(2,6)
    g_pavo.add_edge(2,9)
    g_pavo.add_edge(2,5)
    g_pavo.add_edge(10,8)
    g_pavo.add_edge(8,9)
    g_pavo.add_edge(10,5)
    g_pavo.add_edge(8,3)

    #26
    g_sculptor =Graph(5)
    g_sculptor.add_edge(0,4)
    g_sculptor.add_edge(4,1)
    g_sculptor.add_edge(1,2)
    g_sculptor.add_edge(2,3)
    g_sculptor.add_edge(0,3)

    #27
    g_sextans =Graph(4)
    g_sextans.add_edge(0,1)
    g_sextans.add_edge(2,1)
    g_sextans.add_edge(2,3)
    g_sextans.add_edge(3,0)

    #28
    g_telescopium=Graph(6)
    g_telescopium.add_edge(0,1)
    g_telescopium.add_edge(2,1)
    g_telescopium.add_edge(2,3)
    g_telescopium.add_edge(3,4)
    g_telescopium.add_edge(4,5)
    g_telescopium.add_edge(5,0)

    #29
    g_ursamajor=Graph(7)
    g_ursamajor.add_edge(0,5)
    g_ursamajor.add_edge(5,3)
    g_ursamajor.add_edge(3,4)
    g_ursamajor.add_edge(4,1)
    g_ursamajor.add_edge(1,2)
    g_ursamajor.add_edge(2,6)
    g_ursamajor.add_edge(6,4)
   
    #30
    g_vela=Graph(8)
    g_vela.add_edge(1,0)
    g_vela.add_edge(1,2)
    g_vela.add_edge(2,3)
    g_vela.add_edge(3,4)
    g_vela.add_edge(4,5)
    g_vela.add_edge(5,6)
    g_vela.add_edge(6,7)
    
    
    #31
    g_volans=Graph(6)
    g_volans.add_edge(4,0)
    g_volans.add_edge(5,0)
    g_volans.add_edge(3,0)
    g_volans.add_edge(1,3)
    g_volans.add_edge(1,2)
    g_volans.add_edge(2,5)
    
    


    
    
    



   
if __name__ == '__main__':
    main()
    
    

