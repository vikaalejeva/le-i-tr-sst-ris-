#Izveidot funkciju, kas pārbauda, vai skaitlis atrodas lietotāja noteiktā diapozonā vai nē.
def noteiktDiapozonu(d1,d2,sk):
  rezultats = "Sakitlis nav diapazonā!"
  if d1>=sk<=d2:
    rezultats = "Skaitlis ir diapazonā!"
  return rezultats

d1 = int(input("Ievadi diapozona sākumu: "))
d2 = int(input("Ievadi diapozona beigas: "))
sk = int(input("Ievadi skaitli: "))
rez = noteiktDiapozonu(d1,d2,sk)
print(rez)