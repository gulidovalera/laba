import tracemalloc
import time
from Bio import SeqIO

def calculate_gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence)

def process_genbank_file(filename):
    tracemalloc.start()  # Запуск отслеживания памяти
    snapshots = []       # Список для хранения снимков памяти и времени
    start_time = time.time()

    sequences_with_gc = []
    for i, record in enumerate(SeqIO.parse(filename, "genbank"), 1):
        gc_content = calculate_gc_content(record.seq)
        sequences_with_gc.append((record.id, gc_content))
        
        # Фиксируем память и время каждые 10 записей
        if i % 10 == 0:
            snapshot = tracemalloc.take_snapshot()
            current_time = time.time() - start_time
            snapshots.append((current_time, snapshot))

    # Сортировка и вывод
    sorted_sequences = sorted(sequences_with_gc, key=lambda x: x[1])
    for record_id, gc_content in sorted_sequences:
        print(f"{record_id}: GC = {gc_content:.2%}")

    # Анализ потребления памяти
    print("\n--- Потребление памяти по времени ---")
    for time_stamp, snapshot in snapshots:
        stats = snapshot.statistics("lineno")
        total_memory = sum(stat.size for stat in stats) / 1024  # В KiB
        print(f"Время: {time_stamp:.2f} сек. | Память: {total_memory:.1f} KiB")

    # Самый большой блок памяти
    final_stats = tracemalloc.take_snapshot().statistics("traceback")
    if final_stats:
        largest_block = final_stats[0]
        print(f"\nСамый большой блок: {largest_block.size/1024:.1f} KiB")

file_path = r"C:\Users\ASUS\OneDrive\Документы\subjects\python\labi\в3_файлы.gb" 
process_genbank_file(file_path)