def fusion(A, B):
    resultat = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            resultat.append(A[i])
            i = i + 1
        else:
            resultat.append(B[j])
            j = j + 1
    return resultat + A[i:] + B[j:]

def tri_fusion(L):
    """Liste triee (nouvelle liste), par tri fusion."""
    ...
