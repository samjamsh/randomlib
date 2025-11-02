# RandomLib
A simple random library with prototype in python and main version in C language where you can use in your projects for simple random taks

# 🧬 randomlib — Biblioteca Pseudoaleatória Baseada em Tempo

**Autor:** Sam Jamsh  
**Licença:** Apache License 2.0  
**Versão:** 1.0  

---

## 📘 Visão Geral

`randomlib` (módulo: `ramlib`) é uma biblioteca **simples, independente e determinística** para gerar números **pseudoaleatórios** baseados em tempo.  
Ela utiliza múltiplas camadas de granularidade temporal (milissegundos, microssegundos, nanossegundos e timestamp) combinadas com operações bitwise e multiplicadores dinâmicos.

Ideal para experimentos de pseudoaleatoriedade, simulações, geração de seeds e ambientes sem dependências externas complexas.

---

## 🚀 Instalação

A biblioteca é autônoma — não depende de pacotes externos além da biblioteca padrão do Python.

Basta copiar o arquivo `randomlib.py` para o seu projeto.

---

## 🧩 Importação e Uso

```python
from ramlib import genrandom

# Get & Print a random value
start = 1
end = 10

random_value = genrandom(start, end)
print("\nRandom Value:", random_value.getnew())      # get a random value once
print()

for i in range(5):
    newrandom = random_value.generate(start, end)    # get a random value multiple times
    print("New Random:", newrandom)
print()

