import time

print("Processando sua operação", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(1.5)  # ⏸️ Pausa de 1 segundo entre cada ponto
print("\nResultado: 15")