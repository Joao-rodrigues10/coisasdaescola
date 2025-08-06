nota1 = float(input("Digite sua primeira nota aqui => :"))

nota2 = float(input("Digite sua segunda nota aqui => :"))

nota3 = float(input("Digite sua terceira nota aqui => :"))

media = (nota1 + nota2 + nota3) / 3

if media >= 10: 
    print(f" Sua media foi {round(media, 2)}, Parabens APROVADO")

elif media >= 7:
    print(f"Sua media foi {round(media, 2)} Muito bom!")

elif media >= 5:
    print(f"Sua media foi {round(media, 2)} Recuperção")

elif media >= 4:
    print(f"Sua media foi {round(media, 2)}")

