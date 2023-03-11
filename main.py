with open ('list of dishes\list_dish.txt', 'rt', encoding= 'utf-8' ) as file:
    cook_book = {}
    for line in file:
       cook_book1 = line.strip()
       quantity = int(file.readline())
       dish = []
       for i in range(quantity):
           name_dish, quant_dish, unit = file.readline().strip().split(' | ')
           dish.append({
           'name_dish' : name_dish,
           'quant_dish' : quant_dish,
           'unit' : unit
               })
       file.readline()
       cook_book[cook_book1] = dish


def UPPER (dishes):
    dishes_upper = []
    for i in dishes:
       i_str = str(i)
       i_str1 = str.capitalize(i_str)
       dishes_upper.append(i_str1)
    return dishes_upper
       
def get_shop_list_by_dishes(dishes, person_count):
    dishes1 = UPPER(dishes)
    dishes_set = set(dishes1)
    all_keys = cook_book.keys()
    all_keys_set = set(all_keys)
    res = list((dishes_set) & (all_keys_set))
    print('Вам потребуется:')
    for d in res:
        dis1 = cook_book.get(d)
        dis1_list = list(dis1)
        for ing in dis1_list:
            val = ing.values()
            val_list = list(val)
            a, b, c = val_list
            print (f'{a} {int(b)*int(person_count)} {c}')
 
 
def get_shop_list_by_dishes_hw(dishes, person_count):
    dishes1 = UPPER(dishes)
    dishes_set = set(dishes1)
    all_keys = cook_book.keys()
    all_keys_set = set(all_keys)
    res = list((dishes_set) & (all_keys_set))
    for d in res:
        
        dis1 = cook_book.get(d)
        dis1_list = list(dis1)
        
        result = {}
        for ing in dis1_list:
            val_dict={}
            val = ing.values()
            a, b, c = list(val)
            val_q1 = (int(b)*int(person_count))
            val_dict['unit']= c
            val_dict['quant_dish']= val_q1
            result[a]=val_dict
        print(result)  
  
  
input_dishes = []  
input_count = []    

def main (dishe, coun):
     
    while True:
        command = input ('Введите команду i или Ш для подсчета необходимых продуктов для праздничного меню:')
        if command == "i" or command == "ш" :
            input_dishes1 = input('Введите блюда которые бы Вы хотели приготовить в формате : "Блюдо1, блюдо2, и тд.')
            input_dishes2 = input_dishes1.split(', ')
            input_count = input('Введите колличество персон:')
            
            get_shop_list_by_dishes (input_dishes2, input_count)
            get_shop_list_by_dishes_hw (input_dishes2, input_count)
    
        
        elif command == "q":
           print("Выход")
           return
            

print(main(input_dishes, input_count))