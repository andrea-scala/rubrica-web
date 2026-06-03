class Persona:
    """
    Classe Persona, ogni persona è definita da:
        - id: intero (id autonumerante, identificativo della persona)
        - nome: stringa
        - cognome: stringa
        - indirizzo: stringa
        - telefono: stringa
        - eta: intero
    """
    def __init__(self, id=None, nome='', cognome='', indirizzo='', telefono='', eta=0):
            self.id = id
            self.nome = nome
            self.cognome = cognome
            self.indirizzo = indirizzo
            self.telefono = telefono
            self.eta = eta

    # def __repr__(self):
    #     return f'<Persona {self.id} - {self.nome} {self.cognome}>'