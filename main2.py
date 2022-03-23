
# 4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed

    def ilosc_produktu(self):
        return self.ilosc, self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed



maslo = NaZakupy('masło', 5, 'szt', 4 )

print(maslo.wyswietl_produkt())

print(maslo.ilosc_produktu())

print(maslo.ile_kosztuje(), '\n')


# 5
class CiagiArytmetyczne:
     a = 1
     r = 2
     n = 10

     def wyswietl_dane(self):
         i = 0
         while i < self.n:
             print(self.a)
             i += 1
             self.a += self.r
         return ''



     def pobierz_elementy(self):
         self.a = int(input("Podaj pierwszy wyraz: "))
         self.a2 = int(input("Podaj drugi wyraz: "))
         self.r = self.a2-self.a


     def pobierz_parametry(self):
         self.a = int(input("Podaj pierwszy wyraz: "))
         self.r = int(input("Podaj roznice: "))
         self.n = int(input("Podaj ilosc wyrazow: "))

obiekt = CiagiArytmetyczne()

print(obiekt.wyswietl_dane())

obiekt.pobierz_elementy()

print(obiekt.wyswietl_dane())

obiekt.pobierz_parametry()

print(obiekt.wyswietl_dane())


