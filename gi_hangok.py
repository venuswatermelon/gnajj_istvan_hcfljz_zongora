class GI_Hangok:
    def __init__(self):
        self.hangok = {
            'C': 262, 'C#': 277, 'D': 294, 'D#': 311,
            'E': 330, 'F': 349, 'F#': 370, 'G': 392,
            'G#': 415, 'A': 440, 'A#': 466, 'B': 494
        }

    def gi_frekvencia(self, hang):
        return self.hangok.get(hang, 440)

    def gi_osszes_hang(self):
        return list(self.hangok.keys())