def dfs(g, sommet, visites=None):
    if visites is None:
        visites = []
    visites.append(sommet)
    for voisin in g[sommet]:
        if voisin not in visites:
            dfs(g, voisin, visites)
    return visites

def atteignables(g, depart):
    """Liste triee des sommets atteignables depuis depart."""
    ...
