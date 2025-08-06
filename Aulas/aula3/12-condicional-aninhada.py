idade = int(input("Qual sua idade?: "))

vrfcnh = (input("Você tem cnh?: ").lower())
temcnh = False

if vrfcnh == "sim":
    temcnh = True
else:
    temcnh = False

if idade >= 18 and temcnh == True:
    print("voce pode digirir")

else:
    print("voce nao pode dirigir :( ")