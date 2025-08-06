from datetime import datetime
import locale 
locale.setlocale(locale.LC_ALL,'pt-BR.UTF-8')

opcao = 3

match opcao:
    case 1:
        print("opão 1 selecionada")
    case 2:
        print("opão 2 selecionada")
    case 3:
        print("opão 3 selecionada")
    case _:
        print("opção invalida")

dia = "segunda"


pegardiaatual = datetime.now()
print(pegardiaatual)

print(f"data atual {pegardiaatual.strftime('%d/%m/%Y')}")
print(f"data atual {pegardiaatual.strftime('%d/%m/%y')}")
print(f"Dia da semana {pegardiaatual.strftime('%A')}")
print(f"Dia da semana (abreviado) {pegardiaatual.strftime('%a')}")
print(f"numero do dia do ano {pegardiaatual.strftime('%j')}")
print(f"dia {pegardiaatual.strftime('%d')}")
print(f"mes {pegardiaatual.strftime('%m')}")
print(f"ano abreviado {pegardiaatual.strftime('%y')}")
print(f"ano por extenso {pegardiaatual.strftime('%Y')}")


print(int(pegardiaatual.srtftime("%A")))

match dia:

    case "segunda" :
        print("hoje é segunda")
    case "terça" :
        print("hoje é terça")
    case "quarta" :
        print("hoje é quarta")
    case "quinta" :
        print("hoje é quinta")
    case "sexta" :
        print("hoje é sexta")
    case "sabado" :
        print("hoje é sabado")
    case "domingo" :
        print("hoje é domingo")
    case _:
        print("valor invalido")
        