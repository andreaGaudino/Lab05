
import dataclasses

@dataclasses.dataclass
class Corso:
    codins: str
    crediti:int
    nome:str
    pd:int

    def __str__(self):
        return f"{self.nome} ({self.codins})"