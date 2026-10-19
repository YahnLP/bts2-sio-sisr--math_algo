def parse_ligne(ligne):
    ip, statut = ligne.split(";")
    return (ip.strip(), statut.strip())


def echecs_par_ip(lignes):
    d = {}
    for l in lignes:
        ip, statut = parse_ligne(l)
        if statut == "ECHEC":
            d[ip] = d.get(ip, 0) + 1
    return d


def suspectes(lignes, seuil):
    """Adresses (triees) avec au moins seuil echecs."""
    ...
