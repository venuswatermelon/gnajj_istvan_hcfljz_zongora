class GI_Akkordok:
    def __init__(self):
        self.akkordok = {
            'C': ['C', 'E', 'G'],
            'Dm': ['D', 'F', 'A'],
            'Em': ['E', 'G', 'B'],
            'F': ['F', 'A', 'C'],
            'G': ['G', 'B', 'D'],
            'Am': ['A', 'C', 'E']
        }

    def gi_akkord_hangok(self, akkord):
        return self.akkordok.get(akkord, ['C', 'E', 'G'])

    def gi_uj_akkord(self, nev, hangok):
        self.akkordok[nev] = hangok

    def gi_sajat_fuggveny(self, szam1, szam2):
        return f"Zongora billentyűk: {szam1} fehér, {szam2} fekete"