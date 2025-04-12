from typing import List

def average(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

lista_liczb = [1.0, 2.0, 3.0]
wynik = average(lista_liczb)
print(f"Średnia: {wynik}")
