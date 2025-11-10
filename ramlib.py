"""
randomlib.py
------------

Uma biblioteca simples e independente para gerar números pseudoaleatórios
baseados no tempo atual do sistema (milissegundo, microsegundo, nanosegundo e timestamp).

Autor: [Sam Jamsh]
Licença: Apache License 2.0
Versão: 1.0
"""

import time
import datetime
from random import randrange


class genrandom():
   

    def __init__(self, a, b, s=31):
        self.a = a
        self.b = b
        self.s = s

        self.all = self.generate_random_number(a, b, s)

        self.new, self.random_number, self.last, self.original = self.all
   

    def generate(self, a, b, s=31):
        time.sleep(0.009)   # higher it is, better it becomes
        self.all = self.generate_random_number(a, b, s)
        self.new, self.random_number, self.last, self.original = self.all
        return self.new


    def abs_custom(self, value):
        if value < 0:
            return value * -1
        else:
            return value



    def get_time(self):
        now = datetime.datetime.now()           # captura data e hora atuais
        hora = now.hour                         # extrai a hora
        minuto = now.minute                     # extrai o minuto
        segundo = now.second                    # extrai o segundo
        micro_segundo = now.microsecond         # extrai o microsegundo
        mili_segundo = micro_segundo // 1000    # converte micro → mili
        nano_segundo = int(time.time_ns() % 1e9)# captura os nanossegundos (resto de 1 segundo)
        timestamp = time.time_ns()              # timestamp total em nanossegundos (desde 1970)
        nnano = int(time.time_ns() % 1000000)   # uma versao do nano
        return hora, minuto, segundo, mili_segundo, micro_segundo, nano_segundo, timestamp, nnano




    def generate_random_number(self, a, b, x=31):
        if b < a:
            raise ValueError("O valor máximo 'b' deve ser maior ou igual ao mínimo 'a'.")

          # Captura todos os tempos necessários
        hora, minuto, segundo, mili, micro, nano, timestamp, nnano = self.get_time()

        x = mili

        # Cria o seed combinando os tempos e o parâmetro x
        seed = self.abs_custom(((nano * x + mili + nano) ^ nano) ^ timestamp)


        # Gera número pseudoaleatório no intervalo [a, b]
        random_number = ((seed * (nnano + nano + mili)) % (b - a + 1)) + a

        calc1 = (seed * (nnano + mili + nano) * nano + mili) 

        calc2 = ((b - a + 1) + a) - 1

        new = seed % calc2 + 1

        last = ((seed * calc1) % calc2) + 1

        original = randrange(1, 11)

        return new, random_number, last, original
    


    def getall(self):
        return self.all
    
    def getnew(self):
        return self.new
    
    def getrandom_number(self):
        return self.random_number
    
    def getlast(self):
        return self.last
    
    def getoriginal(self):
        return self.original


if __name__ == "__main__":
    randvalue = genrandom(1, 10).getnew()
    print("Random Value:", randvalue)
