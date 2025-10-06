hafta_kunlari = [
    "Yakshanba", 
    "Dushanba", 
    "Seshanba", 
    "Chorshanba", 
    "Payshanba", 
    "Juma", 
    "Shanba"
]
K = int(input("K kunini kiriting (1-365 oralig'ida): "))

kun_index = (1 + (K - 1)) % 7

print(f"{K}-kun haftaning {hafta_kunlari[kun_index]} kuniga to‘g‘ri keladi.")