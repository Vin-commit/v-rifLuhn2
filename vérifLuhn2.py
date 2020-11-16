#!/usr/bin/python3
# coding: utf-8


# Src : http://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers#Python


print (" Vérification si un nombre (numéro de SIREN, de SIRET, IMEI, de carte bancaire...) suit les conditions fixées par la formule de Luhn.\n Usage :<nombre testé> => <True|False>\n")


def vérifLuhn2(n):
    r = [int(ch) for ch in n][::-1] 
    return (sum(r[::2]) + sum([sum(divmod(d*2, 10)) for d in r[1::2]])) % 10 == 0 


# (([1]) + ((())[2])) % 10 == 0
# [::-1] inverse l’ordre de la liste.
# [::2] sélectionne un élément sur deux.
# [1::2] sélectionne à partir du 2° élément un élément sur deux.
# divmod(x, y) renvoie le tuple (x // y, x % y).
# sum(<list or tuple>) additionne les éléments fournis.


for n in (9, 18, 8763, 325373017, 42407859000025, 353809054912495, 1234567890123452):
    print (str(n)+" =>", vérifLuhn2(str(n)))
