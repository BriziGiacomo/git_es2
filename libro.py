class Libro:
    def __init__(self, autore: str, titolo: str, anno: int, editore: str, pagine: int):
        self.autore = autore
        self.titolo = titolo
        self.anno = anno
        self.editore = editore
        self.pagine = pagine

    def reading_time(self) -> int:
        """Restituisce il tempo di lettura stimato in minuti (es. 2 minuti a pagina)."""
        return self.pagine * 2

    def __str__(self):
        return f"'{self.titolo}' di {self.autore} ({self.anno}) - {self.editore}, {self.pagine} pag."