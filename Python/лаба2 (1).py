def calculate_gc_content(sequence):
    return (sequence.count('G') + sequence.count('C')) / len(sequence) * 100

print("Введите последовательности в формате FASTA (закончите ввод пустой строкой):")

sequences = {}     #создаем словарь.Ключами словаря будут названия последовательностей (идентификаторы), а значениями сами последовательности.
while True:
    line = input()
    if not line:
        break
    if line.startswith('>'):   #Если строка начинается с >, она считает это названием последовательности (убирая символ >).
        identifier = line[1:]  # Убираем ">"
        sequences[identifier] = ""
    else: #Если строка не начинается с >, она добавляет эту строку как саму последовательность к идентификатору.
        sequences[identifier] += line

# Вывод GC-состава для каждой последовательности
print("\n Результаты GC-состава (в процентах):")
max_gc_identifier = None
max_gc_content = 0
for identifier, sequence in sequences.items():
    gc_content = calculate_gc_content(sequence)
    print(f'{identifier}: {gc_content:.2f}%')
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_identifier = identifier
# Вывод последовательности с максимальным GC-составом
print(f"\n Последовательность с наибольшим GC-составом:")
print(f'{max_gc_identifier}: {max_gc_content:.2f}%')