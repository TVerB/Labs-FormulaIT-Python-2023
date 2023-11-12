memory = 1.44           # мегабайты
number_of_pages = 100
number_of_strings = 50
number_of_chars = 25
memory_for_char = 4     # байты

memory *= 1024**2
memory_for_book = number_of_pages * number_of_strings * number_of_chars * memory_for_char

print("Количество книг, помещающихся на дискету:", int(memory / memory_for_book))
