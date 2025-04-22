def quadrato_magico(n):
    rimamenti = []
    for i in range(n*n):
        rimamenti.append(i)
    ricorsione([], rimamenti, n)


def ricorsione(parziale, rimanenti, n):
    if len(parziale) == n*n:
        print(parziale)
    else:
        for i in range(len(rimanenti)):
            numero = rimanenti[i]
            parziale.append(numero)
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]
            ricorsione(parziale,nuovi_rimanenti, n)
            parziale.pop()

if __name__ == "__main__":
    quadrato_magico(3)