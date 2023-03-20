"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - hra Bulls and Cows
author: Jaroslav Dvořák
email: dvorak-jaroslav@email.cz
discord: Jaroslav D
"""

import random


def gen_tajneho_cisla() -> list:
    """Generuje náhodné 4 čísla
    v rozmezí 0 až 9.
    Čísla jsou uložena do seznamu.
    >>>gen_tajne_cisla()
    např. [5, 8, 0, 6]
    """
    cislice = list(range(10))
    random.shuffle(cislice)
    l_tajna_cisla = cislice[:4]
    """kontrola jestli není nula na začátku"""
    temp = ""
    if l_tajna_cisla[0] == 0:
        temp = l_tajna_cisla[0]
        l_tajna_cisla[0] = l_tajna_cisla[1]
        l_tajna_cisla[1] = temp
    return l_tajna_cisla

def zadaní_kontrola_cisel() -> str:
    """Funkce požádá uživatele, aby zadal 4místné číslo. Potom kontroluje
    a upozorňuje, jestli zadaná čísla uživatelem jsou opravdu zadána, 
    jestli neobsahují nečíselné znaky, jestli není zadáno více nebo měně 
    než 4 čísla, jestli nezačínají nulou a jestli nebsahují duplicitu.
    >>>zadani_kontrola_cisel()
    např. "8421"
    """
    while True:
        oddělení = "-" * 40
        zadana_cisla = input("Zadej 4 čísla:  ")
        if zadana_cisla == "":
            print("Nezadal jsi žádná čísla.")
            print(oddělení)
            continue
        elif not zadana_cisla.isdigit():
            print("Zadané hodnoty musí obsahovat poze čísla.")
            print(oddělení)
            continue
        elif len(zadana_cisla) > 4:
            print("Zadal jsi více než 4 čísla.")
            print(oddělení)
            continue
        elif len(zadana_cisla) < 4:
            print("Zadal jsi méné než 4 čísla")
            print(oddělení)
            continue
        elif zadana_cisla[0] == "0":
            print("Zadane číslo nesmí začínat nulou.")
            print(oddělení)
            continue
        elif len(set(zadana_cisla)) != len(zadana_cisla):
            print("Tvé zadání obsahuje duplicitní čísla.")
            print(oddělení)
            continue
        else:
            break
    return zadana_cisla

def pocet_byku_krav(seznam_pocitac: list, seznam_uzivatel: list) -> int:
    """Funkce počítá "býky a krávy".
    Funkce má na vstupu dva seznami se 4 různými čísly.
    Pokud je v seznamu_uzivatel o proti seznamu_pocitac správné
    číslo i umístění - připočítá se býk, pokud je správné jen
    číslo (a špatné umístění) - připočítá se kráva.
    >>>pocet_byku_krav([1, 2, 5, 6], [1, 2, 6, 8])
    2, 1
    """
    byk = 0
    krava = 0
    for index, cislo in enumerate(seznam_uzivatel):
        if cislo == seznam_pocitac[index]:
            byk = byk + 1
        elif cislo in seznam_pocitac:
            krava = krava + 1
    return byk, krava


def prevod(a: str) -> list:
    """Funkce převede string jehož znaky jsou
    číslice na list, který obsahuje int.
    >>>prevod("1234")
    [1, 2, 3, 4]
    """
    x_list = []
    for cislice in a:
        x_list.append(int(cislice))
    return x_list

def vypis_byci_kravy(cislo_byk: int, cislo_krava: int) -> print:
    """Funkce má na vstupu počet býků a krav
    a výstupem je příkaz print se správné 
    skloňonovanými slovy býk a kráva.
    >>>vypis_byci_krava(2, 5)
    např. 2 býci, 5 krav  
    """
    if cislo_byk == 1:
        slovo_byk = str(cislo_byk) + " býk"
    elif cislo_byk in [2, 3, 4]:
        slovo_byk = str(cislo_byk) + " býci"
    else:
        slovo_byk = str(cislo_byk) + " býků"

    if cislo_krava == 1:
        slovo_krava = str(cislo_krava) + " kráva"
    elif cislo_krava in [2, 3, 4]:
        slovo_krava = str(cislo_krava) + " krávy"
    else:
        slovo_krava = str(cislo_krava) + " krav"
    print(slovo_byk, slovo_krava,sep=", ")

def hraj():
    """Funkce spouští a řídí celou hru."""
    oddělení = "-" * 40
    pocet_pokusu = 0
    print("Ahoj")
    print(oddělení)
    print("Vygeneroval jsem pro tebe 4místné číslo: ")
    print("Pojdme si zahrát hru býci a krávy.")
    print(oddělení)

    pocitac_cisla = gen_tajneho_cisla()
    #print(pocitac_cisla)  #jen abych viděl správné řešení

    while True:
        uzivatel_tip = zadaní_kontrola_cisel()
        uzivatel_cisla = prevod(uzivatel_tip)
        pocet_pokusu = pocet_pokusu + 1
        pocet_byk, pocet_krav = pocet_byku_krav(pocitac_cisla, uzivatel_cisla)
        vypis_byci_kravy(pocet_byk, pocet_krav)
        print(oddělení)
        if pocet_byk == 4:
            break
    if pocet_pokusu == 1:
        print(f"Máš všechny čísla správně na {pocet_pokusu} pokus.")
    elif pocet_pokusu in [2, 3, 4]:
        print(f"Máš všechny čísla správně na {pocet_pokusu} pokusy.")
    else:
        print(f"Máš všechny čísla správně na {pocet_pokusu} pokusů.")
    print(oddělení)
    if pocet_pokusu < 10:
        print("Je to úžasný výsledek, dobrá práce.")
    elif pocet_pokusu < 20:
        print("Je to průměrný výsledek.")
    else:
        print("Je to podprůměrný výsledek, přiště se více snaž.")

if __name__ == "__main__":
    hraj()


