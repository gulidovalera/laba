from Bio import SeqIO
import os

def calculate_gc_content(sequence):
    """Вычисляет GC-состав последовательности."""
    sequence = sequence.upper()  # Преобразуем в верхний регистр
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence)

def process_genbank_file(filename):
    """
    Читает GenBank файл, вычисляет GC-состав каждой последовательности и
    выводит последовательности в порядке возрастания GC-составов.
    """
    sequences_with_gc = []
    for record in SeqIO.parse(filename, "genbank"):
        gc_content = calculate_gc_content(record.seq)
        sequences_with_gc.append((record.id, record.description, gc_content, str(record.seq)))

    # Сортируем последовательности по GC-составу (возрастание)
    sorted_sequences = sorted(sequences_with_gc, key=lambda x: x[2])

    for record_id, description, gc_content, seq in sorted_sequences:
        print(f"{record_id}: {description}, GC = {gc_content}")

file_path = r"C:\Users\ASUS\OneDrive\Рабочий стол\python\labi\в3_файлы.gb" 
process_genbank_file(file_path)
