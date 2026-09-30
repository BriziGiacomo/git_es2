class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro: Libro):
        """Aggiunge un libro alla biblioteca."""
        self.libri.append(libro)

    def conta_libri(self) -> int:
        """Restituisce il numero totale di libri presenti."""
        return len(self.libri)

    def cerca_per_titolo(self, titolo: str) -> list:
        """Cerca i libri che contengono la stringa specificata nel titolo."""
        return [l for l in self.libri if titolo.lower() in l.titolo.lower()]

    def cerca_per_autore(self, autore: str) -> list:
        """Cerca i libri scritti da un determinato autore."""
        return [l for l in self.libri if autore.lower() in l.autore.lower()]