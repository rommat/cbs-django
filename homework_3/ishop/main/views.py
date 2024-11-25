from django.shortcuts import render
from django.http import HttpRequest


# Клас для категорії товарів
class Category:
    # all_products = []  # Змінна класу для зберігання всіх товарів у категорії

    def __init__(self, name, description=None):
        self.name = name  # Назва категорії
        self.description = description  # Опис категорії (не обов'язковий)
        self.products = []  # Список товарів цієї категорії
        # Category.all_products.append(self)  # Додаємо категорію до загального списку

    def add_product(self, product):
        """Метод для додавання товару до категорії"""
        self.products.append(product)

    @property
    def all_products(self):
        """Властивість для отримання всіх товарів категорії"""
        return self.products

    def __repr__(self):
        return f"Category(name={self.name}, description={self.description})"


# Клас для властивості товару
class ProductProperty:
    def __init__(self, name, value):
        self.name = name  # Назва властивості
        self.value = value  # Значення властивості

    def __repr__(self):
        return f"ProductProperty(name={self.name}, value={self.value})"


# Клас для товару
class Product:
    def __init__(self, name, category, price, quantity, properties=None):
        self.name = name  # Назва товару
        self.category = category  # Категорія товару
        self.price = price  # Ціна товару
        self.quantity = quantity  # Кількість товару на складі
        self.properties = properties if properties else []  # Список властивостей товару
        category.add_product(self)  # Додаємо товар до відповідної категорії

    def add_property(self, property):
        self.properties.append(property)  # Додавання нової властивості

    def __repr__(self):
        return (f"Product(name={self.name}, category={self.category.name}, price={self.price}, "
                f"quantity={self.quantity}, properties={self.properties})")


# Створимо категорії товарів

# Категорія 1: Електроніка (5 товарів)
electronics = Category("Електроніка", "Товари, пов'язані з технологіями та електронікою")

phone = Product("Телефон", electronics, 2000, 50)
phone.add_property(ProductProperty("Колір", "Чорний"))
phone.add_property(ProductProperty("Екран", "6.5 дюймів"))
phone.add_property(ProductProperty("Процесор", "Snapdragon 888"))
phone.add_property(ProductProperty("Камера", "48 МП"))
phone.add_property(ProductProperty("Оперативна пам'ять", "8 ГБ"))
phone.add_property(ProductProperty("Зображення", "https://example.com/phone.jpg"))
phone.add_property(ProductProperty("Операційна система", "Android"))

laptop = Product("Ноутбук", electronics, 5000, 30)
laptop.add_property(ProductProperty("Колір", "Сірий"))
laptop.add_property(ProductProperty("Екран", "15.6 дюймів"))
laptop.add_property(ProductProperty("Процесор", "Intel Core i7"))
laptop.add_property(ProductProperty("Пам'ять", "512 ГБ SSD"))
laptop.add_property(ProductProperty("Оперативна пам'ять", "16 ГБ"))
laptop.add_property(ProductProperty("Зображення", "https://example.com/laptop.jpg"))
laptop.add_property(ProductProperty("Операційна система", "Windows 10"))

tablet = Product("Планшет", electronics, 3000, 70)
tablet.add_property(ProductProperty("Колір", "Чорний"))
tablet.add_property(ProductProperty("Екран", "10 дюймів"))
tablet.add_property(ProductProperty("Процесор", "Apple A14 Bionic"))
tablet.add_property(ProductProperty("Пам'ять", "128 ГБ"))
tablet.add_property(ProductProperty("Оперативна пам'ять", "4 ГБ"))
tablet.add_property(ProductProperty("Зображення", "https://example.com/tablet.jpg"))
tablet.add_property(ProductProperty("Операційна система", "iOS"))

smartwatch = Product("Смарт-годинник", electronics, 1500, 100)
smartwatch.add_property(ProductProperty("Колір", "Чорний"))
smartwatch.add_property(ProductProperty("Екран", "1.4 дюйма"))
smartwatch.add_property(ProductProperty("Процесор", "MediaTek MTK2502"))
smartwatch.add_property(ProductProperty("Пам'ять", "16 ГБ"))
smartwatch.add_property(ProductProperty("Батарея", "200 мАг"))
smartwatch.add_property(ProductProperty("Зображення", "https://example.com/smartwatch.jpg"))
smartwatch.add_property(ProductProperty("Операційна система", "Wear OS"))

earphones = Product("Навушники Bluetooth", electronics, 800, 200)
earphones.add_property(ProductProperty("Колір", "Чорний"))
earphones.add_property(ProductProperty("Тип", "Бездротові"))
earphones.add_property(ProductProperty("Час роботи", "8 годин"))
earphones.add_property(ProductProperty("Тип підключення", "Bluetooth 5.0"))
earphones.add_property(ProductProperty("Зображення", "https://example.com/earphones.jpg"))
earphones.add_property(ProductProperty("Кнопки", "Тактильні"))

# Категорія 2: Одяг (4 товарів)
clothing = Category("Одяг", "Одяг для повсякденного носіння та святкових подій")

tshirt = Product("Футболка", clothing, 300, 100)
tshirt.add_property(ProductProperty("Колір", "Білий"))
tshirt.add_property(ProductProperty("Розмір", "L"))
tshirt.add_property(ProductProperty("Матеріал", "Бавовна"))
tshirt.add_property(ProductProperty("Стиль", "Класичний"))
tshirt.add_property(ProductProperty("Призначення", "Повсякденний"))
tshirt.add_property(ProductProperty("Зображення", "https://example.com/tshirt.jpg"))

jeans = Product("Джинси", clothing, 1200, 50)
jeans.add_property(ProductProperty("Колір", "Сині"))
jeans.add_property(ProductProperty("Розмір", "M"))
jeans.add_property(ProductProperty("Матеріал", "Денім"))
jeans.add_property(ProductProperty("Стиль", "Slim fit"))
jeans.add_property(ProductProperty("Призначення", "Повсякденний"))
jeans.add_property(ProductProperty("Зображення", "https://example.com/jeans.jpg"))
jeans.add_property(ProductProperty("Довжина", "Стандартна"))

jacket = Product("Куртка", clothing, 2500, 20)
jacket.add_property(ProductProperty("Колір", "Чорний"))
jacket.add_property(ProductProperty("Розмір", "XL"))
jacket.add_property(ProductProperty("Матеріал", "Шкіра"))
jacket.add_property(ProductProperty("Стиль", "Класичний"))
jacket.add_property(ProductProperty("Призначення", "Зимовий"))
jacket.add_property(ProductProperty("Зображення", "https://example.com/jacket.jpg"))
jacket.add_property(ProductProperty("Теплоту", "Тепла"))

scarf = Product("Шарф", clothing, 500, 150)
scarf.add_property(ProductProperty("Колір", "Червоний"))
scarf.add_property(ProductProperty("Матеріал", "Шерсть"))
scarf.add_property(ProductProperty("Довжина", "150 см"))
scarf.add_property(ProductProperty("Ширина", "30 см"))
scarf.add_property(ProductProperty("Призначення", "Теплий"))
scarf.add_property(ProductProperty("Зображення", "https://example.com/scarf.jpg"))

# Категорія 3: Продукти харчування (3 товару)
food = Category("Продукти харчування", "Все для вашого харчування та здоров'я")

apple = Product("Яблука", food, 50, 200)
apple.add_property(ProductProperty("Вага", "1 кг"))
apple.add_property(ProductProperty("Сорт", "Грета"))
apple.add_property(ProductProperty("Смак", "Солодкий"))
apple.add_property(ProductProperty("Фермер", "Фермер №1"))
apple.add_property(ProductProperty("Строк зберігання", "2 тижні"))
apple.add_property(ProductProperty("Зображення", "https://example.com/apple.jpg"))

bread = Product("Хліб", food, 20, 150)
bread.add_property(ProductProperty("Тип", "Житній"))
bread.add_property(ProductProperty("Вага", "500 г"))
bread.add_property(ProductProperty("Термін зберігання", "3 дні"))
bread.add_property(ProductProperty("Країна виробник", "Україна"))
bread.add_property(ProductProperty("Призначення", "Повсякденне"))
bread.add_property(ProductProperty("Зображення", "https://example.com/bread.jpg"))

milk = Product("Молоко", food, 30, 100)
milk.add_property(ProductProperty("Об'єм", "1 л"))
milk.add_property(ProductProperty("Жирність", "3.2%"))
milk.add_property(ProductProperty("Виробник", "Молочний завод"))
milk.add_property(ProductProperty("Дата виробництва", "22.11.2024"))
milk.add_property(ProductProperty("Термін зберігання", "7 днів"))
milk.add_property(ProductProperty("Зображення", "https://example.com/milk.jpg"))

# Категорія 4: Спортивні товари (4 товарів)
sports = Category("Спортивні товари", "Для активного відпочинку та спорту")

ball = Product("Футбольний м'яч", sports, 500, 80)
ball.add_property(ProductProperty("Матеріал", "Штучна шкіра"))
ball.add_property(ProductProperty("Розмір", "5"))
ball.add_property(ProductProperty("Вага", "420 г"))
ball.add_property(ProductProperty("Тип", "Стандартний"))
ball.add_property(ProductProperty("Призначення", "Для гри в футбол"))
ball.add_property(ProductProperty("Зображення", "https://example.com/ball.jpg"))

bicycle = Product("Велосипед", sports, 8000, 25)
bicycle.add_property(ProductProperty("Тип", "Гірський"))
bicycle.add_property(ProductProperty("Колір", "Чорний"))
bicycle.add_property(ProductProperty("Розмір", "26 дюймів"))
bicycle.add_property(ProductProperty("Матеріал", "Алюміній"))
bicycle.add_property(ProductProperty("Призначення", "Для активного відпочинку"))
bicycle.add_property(ProductProperty("Зображення", "https://example.com/bicycle.jpg"))
bicycle.add_property(ProductProperty("Максимальне навантаження", "120 кг"))

dumbbells = Product("Гантелі", sports, 1500, 40)
dumbbells.add_property(ProductProperty("Вага", "10 кг"))
dumbbells.add_property(ProductProperty("Матеріал", "Чавун"))
dumbbells.add_property(ProductProperty("Тип", "Регульовані"))
dumbbells.add_property(ProductProperty("Кількість в комплекті", "2 шт"))
dumbbells.add_property(ProductProperty("Призначення", "Для тренувань"))
dumbbells.add_property(ProductProperty("Зображення", "https://example.com/dumbbells.jpg"))
dumbbells.add_property(ProductProperty("Ручки", "Гумові"))

skates = Product("Ковзани", sports, 1200, 60)
skates.add_property(ProductProperty("Тип", "Фігурні"))
skates.add_property(ProductProperty("Розмір", "36-41"))
skates.add_property(ProductProperty("Матеріал", "Шкіра"))
skates.add_property(ProductProperty("Колір", "Білий"))
skates.add_property(ProductProperty("Призначення", "Для фігурного катання"))
skates.add_property(ProductProperty("Зображення", "https://example.com/skates.jpg"))

# Категорія 5: Іграшки (3 товару)
toys = Category("Іграшки", "Товари для дітей різного віку")

lego = Product("Конструктор LEGO", toys, 1200, 60)
lego.add_property(ProductProperty("Вік", "3+"))
lego.add_property(ProductProperty("Кількість деталей", "500"))
lego.add_property(ProductProperty("Матеріал", "Пластик"))
lego.add_property(ProductProperty("Тип", "Конструктор"))
lego.add_property(ProductProperty("Призначення", "Для розвитку творчих навичок"))
lego.add_property(ProductProperty("Зображення", "https://example.com/lego.jpg"))

doll = Product("Лялька Barbie", toys, 700, 100)
doll.add_property(ProductProperty("Вік", "3+"))
doll.add_property(ProductProperty("Матеріал", "Пластик"))
doll.add_property(ProductProperty("Колір волосся", "Руде"))
doll.add_property(ProductProperty("Одяг", "Сукня"))
doll.add_property(ProductProperty("Тип", "Іграшка"))
doll.add_property(ProductProperty("Зображення", "https://example.com/doll.jpg"))

puzzle = Product("Пазл", toys, 300, 150)
puzzle.add_property(ProductProperty("Вік", "6+"))
puzzle.add_property(ProductProperty("Кількість частин", "1000"))
puzzle.add_property(ProductProperty("Матеріал", "Картон"))
puzzle.add_property(ProductProperty("Тип", "Пазл"))
puzzle.add_property(ProductProperty("Тема", "Природа"))
puzzle.add_property(ProductProperty("Зображення", "https://example.com/puzzle.jpg"))

# Виведемо всі категорії та їх товари
categories = [electronics, clothing, food, sports, toys]

for category in categories:
    print(f"\nКатегорія: {category.name}")
    print(category.all_products)
    print("-" * 30)
    for product in category.all_products\
            :
        print(product)
        print("-" * 30)


# Create your views here.
def main(request: HttpRequest):
    context = {'categories_list': categories}

    return render(request, 'main/main.html', context)


def orders_page(request: HttpRequest):
    return render(request, 'main/orders.html')


def contacts_page(request: HttpRequest):
    return render(request, 'main/contacts.html')
