# Question

class Soru:
    def __init__(self, metin, secenekler, cevap):
        self.metin = metin
        self.secenekler = secenekler
        self.cevap = cevap

    def cevapKontrolu(self, cevap):
        return self.cevap == cevap
# Quiz


class Quiz:
    def __init__(self, sorular):
        self.sorular = sorular
        self.puan = 0
        self.soruNumarasi = 0

    def soruGetir(self):
        return self.sorular[self.soruNumarasi]

    def soruGoster(self):
        soru = self.soruGetir()
        self.soruNumarasii = self.soruNumarasi + 1
        print(f'Soru {self.soruNumarasii }: {soru.metin}')

        for q in soru.secenekler:
            print(f"- {q}")

        cevap = input('cevap : ')
        self.tahmin(cevap)
        self.soruYukle()

    def tahmin(self, cevap):
        soru = self.soruGetir()

        if soru.cevapKontrolu(cevap):
            self.puan += 1
        self.soruNumarasi += 1

    def soruYukle(self):
        if len(self.sorular) == self.soruNumarasi:
            self.puanGoster()
        else:
            self.ilerlemeGoster()
            self.soruGoster()

    def puanGoster(self):
        print('Puan : ', self.puan)

    def ilerlemeGoster(self):
        toplamSorular = len(self.sorular)
        soruNumara = self.soruNumarasi + 1

        if soruNumara > toplamSorular:
            print("Quiz bitti")
        else:
            print(f"Soru {soruNumara} of {toplamSorular}".center(100, '*'))


q1 = Soru('En iyi programlama dili hangisidir ?', [
          'C#', 'Python', 'Javascript', 'java'], 'python')
q2 = Soru('En populer programlama dili hangisidir ?', [
          'C#', 'Javascript', 'Python', 'java'], 'python')
q3 = Soru('En cok programlama dili hangisidir ?', [
          'Python', 'C#', 'Javascript', 'java'], 'python')
sorular = [q1, q2, q3]

quiz = Quiz(sorular)

quiz.soruYukle()
