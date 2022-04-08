men = int(input())
women = int(input())
free_tables = int(input())

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        if free_tables == 0:
            break
        free_tables -= 1
        print(f"({man} <-> {woman}) ", end="")