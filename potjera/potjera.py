import os
import string
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

os.getcwd()

score = 0
lovac_score = 0
pitanja = []
usedsecretnum = []
broj_pokusaja = 0
max_pokusaja = 7

# dodaj pitanja
with open("pitanja.txt", encoding='utf-8') as f:
    for x in f:
        pitanja.append(x.strip().split('|'))

def print_p(p):
    print("╔" + "═" * 50 + "╗")
    print("║ {:48} ║".format("PITANJE"))
    print("╠" + "═" * 50 + "╣")
    print("║ {:<48} ║".format(p[0]))
    print("╠" + "═" * 50 + "╣")
    print("║ {:<23} {:<23} ║".format("(a) " + p[1], "(b) " + p[2]))
    print("║ {:<23} {:<23} ║".format("(c) " + p[3], "(d) " + p[4]))
    print("╚" + "═" * 50 + "╝")

def print_score():
    print("\n" + "="*60)
    print("|{:^58}|".format("BODOVI"))
    print("|" + "="*58 + "|")
    print("|{:^28}|{:^28}|".format("IGRAČ", "LOVAC"))
    print("|{:<28}|{:>28}|".format(f"Score: {score}", f"Score: {lovac_score}"))
    print("|{:^58}|".format(f"PITANJE: {broj_pokusaja+1}/{max_pokusaja}"))
    print("="*60 + "\n")

# main game loop
while broj_pokusaja < max_pokusaja:
    clear_screen()
    print_score()
    
    # jedinstveno pitanje
    secretnumber = random.randint(0, len(pitanja) - 1)
    while secretnumber in usedsecretnum:
        secretnumber = random.randint(0, len(pitanja) - 1)
    usedsecretnum.append(secretnumber)
    
    # sanse da ce lovac tocno odgovoriti
    lovac = random.randint(0, 100)
    
    # prikaz pitanja
    odgovor = pitanja[secretnumber][5][0].lower()
    print_p(pitanja[secretnumber])
    
    # input igraca
    user_odg = ""
    while user_odg not in ['a', 'b', 'c', 'd']:
        user_odg = input("\nTvoj odgovor: (a/b/c/d): ").lower().strip()
        if user_odg not in ['a', 'b', 'c', 'd']:
            print("Smiješ samo odabrati a, b, c, or d!")
    
    # provjeri tocnost odgovora
    if user_odg == odgovor:
        score += 1
        print("\n✓ Točno!")
    else:
        print(f"\n✗ Netočno! Tocan odgovor je ({odgovor})")
    
    # score lovca
    if lovac < 80:
        lovac_score += 1
        print("Lovac je točno odgovorio!")
    else:
        print("Lovac je netočno odgovorio!")
    
    if score <= lovac_score and broj_pokusaja < max_pokusaja - 1:
        print("\nLovac te stiže!")
    
    input("\nEnter za slijedeće pitanje...")
    broj_pokusaja += 1

# konacan rezultat
clear_screen()
print("╔" + "═" * 50 + "╗")
print("║{:^50}║".format("KONAČAN REZULTAT"))
print("╠" + "═" * 50 + "╣")
print("║ {:<24} {:>24} ║".format("Tvoj Score:", str(score)))
print("║ {:<24} {:>24} ║".format("lovčev Score:", str(lovac_score)))
print("╠" + "═" * 50 + "╣")

if score > lovac_score:
    print("║{:^50}║".format("YOU WIN!"))
    print("║{:^50}║".format("Pobjedio si lovca!"))
elif score < lovac_score:
    print("║{:^50}║".format("GAME OVER"))
    print("║{:^50}║".format("Lovac je pobjedio!"))
else:
    print("║{:^50}║".format("NERJEŠENO!"))
    print("║{:^50}║".format("Lovac i ti ste imali jednak broj bodova!"))

print("╚" + "═" * 50 + "╝")