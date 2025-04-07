#лаба4_В3 биопитон с окном для файла
import tkinter as tk
from tkinter import scrolledtext, ttk, filedialog
from Bio import SeqIO
import os

def calculate_gc_content(sequence):
    """Вычисляет GC-состав последовательности."""
    sequence = sequence.upper()  # Преобразуем в верхний регистр
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence)

def process_genbank_file(filename, text_area):
    """
    Читает GenBank файл, вычисляет GC-состав каждой последовательности и
    выводит результаты в текстовую область.
    """
    sequences_with_gc = []
    try:
        for record in SeqIO.parse(filename, "genbank"):
            gc_content = calculate_gc_content(record.seq)
            sequences_with_gc.append((record.id, record.description, gc_content, str(record.seq)))

        # Сортируем последовательности по GC-составу (возрастание)
        sorted_sequences = sorted(sequences_with_gc, key=lambda x: x[2])

        # Вывод результатов в текстовое поле
        for record_id, description, gc_content, seq in sorted_sequences:
            output_text = f"{record_id}: {description}, GC = {gc_content}\n"
            text_area.insert(tk.END, output_text)
            text_area.see(tk.END)  # Автоматическая прокрутка к концу

    except FileNotFoundError:
        text_area.insert(tk.END, f"Ошибка: Файл '{filename}' не найден.\n")
    except Exception as e:
        text_area.insert(tk.END, f"Произошла ошибка: {e}\n")

def browse_files():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title="Select a GenBank file",
                                           filetypes=(("GenBank files", "*.gb *.gbk"), ("all files", "*.*")))
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, filename)


def run_analysis():
    """Запускает анализ GenBank файла и выводит результаты в текстовое поле."""
    file_path = file_path_entry.get()  # Получаем путь к файлу из текстового поля
    results_text.delete("1.0", tk.END)  # Очищаем текстовое поле перед новым анализом
    process_genbank_file(file_path, results_text)


# Создаем главное окно
root = tk.Tk()
root.title("GC Content Analyzer")

# Use ttk for a modern look and feel
style = ttk.Style(root)
style.theme_use('clam')  # Or 'alt', 'default', 'classic', 'vista'

# Элементы интерфейса
frame = ttk.Frame(root, padding=(10, 10, 10, 10))
frame.pack(fill="both", expand=True)

file_path_label = ttk.Label(frame, text="Файл GenBank:")
file_path_label.grid(column=0, row=0, sticky=tk.W)

file_path_entry = ttk.Entry(frame, width=50)
file_path_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
file_path_entry.insert(0, r"C:\Users\ASUS\OneDrive\Рабочий стол\python\ncbi_лаба4\в3_файлы.gb") # default file

browse_button = ttk.Button(frame, text="Обзор", command=browse_files)
browse_button.grid(column=2, row=0, sticky=tk.W)

analyze_button = ttk.Button(frame, text="Анализировать", command=run_analysis)
analyze_button.grid(column=0, row=1, columnspan=3, pady=10) # span over 3 columns

results_text = scrolledtext.ScrolledText(frame, width=80, height=20)
results_text.grid(column=0, row=2, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

# Adjust weights to make things expandable
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)  # Allow the entry field to expand
frame.rowconfigure(2, weight=1)  # Allow the text field to expand

# Запускаем главный цикл обработки событий
root.mainloop()
