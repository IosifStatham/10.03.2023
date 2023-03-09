with open ('list of dishes\list_dish.txt', 'rt', encoding= 'utf-8' ) as file:
    cook_book = {}
    for line in file:
       cook_book1 = line.strip()
       quantity = int(file.readline())
       dish = []
       for i in range(quantity):
           name_dish, quant_dish, unit = file.readline().split(' | ')
           dish.append({
           'name_dish' : name_dish,
           'quant_dish' : quant_dish,
           'unit' : unit
               })
       file.readline()
       cook_book[cook_book1] = dish