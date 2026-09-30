# Importa le classi (se separate in file diversi, es: from libro import Libro)

if __name__ == "__main__":
    # Inizializzazione della biblioteca
    biblioteca_scolastica = Biblioteca()

    # Inserimento di alcuni libri di prova
    libro1 = Libro("Italo Calvino", "Il visconte dimezzato", 1952, "Einaudi", 118)
    libro2 = Libro("George Orwell", "1984", 1949, "Mondadori", 328)
    libro3 = Libro("Dante Alighieri", "Divina Commedia", 1320, "Garzanti", 500)

    biblioteca_scolastica.aggiungi_libro(libro1)
    biblioteca_scolastica.aggiungi_libro(libro2)
    biblioteca_scolastica.aggiungi_libro(libro3)

    # Test del conteggio
    print(f"--- TEST CONTEGGIO ---")
    print(f"Numero totale di libri: {biblioteca_scolastica.conta_libri()}\n")

    # Test del metodo readingTime
    print(f"--- TEST READING TIME ---")
    print(f"Tempo di lettura per '{libro1.titolo}': {libro1.reading_time()} minuti\n")

    # Test di ricerca per autore
    print(f"--- TEST RICERCA PER AUTORE ('Orwell') ---")
    risultati_autore = biblioteca_scolastica.cerca_per_autore("Orwell")
    for l in risultati_autore:
        print(l)
    print()

    # Test di ricerca per titolo
    print(f"--- TEST RICERCA PER TITOLO ('Commedia') ---")
    risultati_titolo = biblioteca_scolastica.cerca_per_titolo("Commedia")
    for l in risultati_titolo:
        print(l)