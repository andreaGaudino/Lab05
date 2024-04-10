import dataclasses

from model import corso, studente



class Iscrizione:
    def __init__(self, corso, studente):
        self.corso = corso
        self.studente = studente
