import random
tab = []
for k in range(40):
    tab.append(random.randint(0,100))

def triFusion(tab):
    if len(tab) > 1:
        mid = len(tab)//2
 
        G = tab[:mid] # sous-tableau gauche
        D = tab[mid:] # sous-tableau droit
 
        triFusion(G)
        triFusion(D)
 
        # Fusion                               
        i = j = k = 0
 
        while i < len(G) and j < len(D):
            if G[i] < D[j]:
                tab[k] = G[i]
                i += 1
            else:
                tab[k] = D[j]
                j += 1
            k += 1
 
        while i < len(G):
            tab[k] = G[i]
            i += 1
            k += 1
 
        while j < len(D):
            tab[k] = D[j]
            j += 1
            k += 1
 
 
# A = [64, 25, 12, 22, 11]
triFusion(tab)
print("Voici le tableau trié")
for i in range(len(tab)):
    print("%d" % tab[i]),