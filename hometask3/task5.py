# В базе данных интернет-магазина PizzaTime хранятся сведения о том, кто, что и
# сколько заказывал у них в определённый период. Вам нужно структурировать
# эту информацию и определить, сколько всего пицц купил каждый заказчик.
# На вход в программу подаётся N заказов. Каждый заказ представляет собой
# строку вида «Покупатель — название пиццы — количество заказанных пицц».
# Реализуйте код, который выводит список покупателей и их заказов по алфавиту. Учитывайте, что один человек может заказать одну и ту же пиццу
# несколько раз.


# Ввод количества заказов
orders_count = int(input('Введите количество заказов: '))
# Создаем пустой словарь для хранения данных о заказах
database = dict()

# Обрабатываем каждый заказ
for i_order in range(orders_count):
# Вводим заказ и разбиваем его на части
    customer, pizza_name, count = input('{} заказ: '.format(i_order + 1)).split()
# Преобразуем количество в целое число
    count = int(count)
    if customer not in database:
        database[customer] = {pizza_name: count}
    else:
        if pizza_name in database[customer]:
            database[customer][pizza_name]+=count
        else:
            # Если пицца новая для этого покупателя, добавляем запись
            database[customer][pizza_name] = count

# Сортируем список покупателей в алфавитном порядке и выводим информацию
for customer in sorted(database.keys()):
    print('{}:'.format(customer))
# Сортируем пиццы по алфавиту и выводим информацию
    for pizza_name in sorted(database[customer].keys()):
        print(' {}: {}'.format(pizza_name, database[customer][pizza_name]))
