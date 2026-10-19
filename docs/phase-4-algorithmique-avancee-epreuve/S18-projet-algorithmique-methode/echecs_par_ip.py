def parse_ligne(ligne):
    ip, statut = ligne.split(";")
    return (ip.strip(), statut.strip())


def echecs_par_ip(lignes):
    """Dictionnaire adresse -> nombre d'echecs (>= 1)."""
    ...
