max = float(input())
conta = input().split(" ")
resultado_conta = 0
if (conta[1] == "+"):
    resultado_conta = int(conta[0]) + int(conta[2])
else:
    resultado_conta = int(conta[0]) * int(conta[2])

if (resultado_conta > max):
    print("OVERFLOW")
else:
    print("OK")
