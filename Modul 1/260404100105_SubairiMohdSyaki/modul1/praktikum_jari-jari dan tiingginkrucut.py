import math

jari_jari = float(input("Masukkan jari-jari alas kerucut (cm): "))
tinggi = float(input("Masukkan tinggi kerucut (cm): "))

volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi

print(f"Volume kerucut = {volume:.2f} cm3")