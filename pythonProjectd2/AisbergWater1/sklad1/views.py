from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from .models import *


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('production')  # Перенаправление на страницу производства
    else:
        form = CustomUserCreationForm()
    # Передача списка ролей в контекст
    role_choices = CustomUser.ROLE_CHOICES
    return render(request, 'register.html', {'form': form, 'role_choices': role_choices})
"""функция регистрации"""


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('production')  # Перенаправление на страницу производства
        else:
            error = 'Неправильное имя пользователя или пароль'
    return render(request, 'login.html', {'error': error})
"""функция входа"""


def home(request):
    return render(request, 'home.html')
"""домашняя страница"""


def warehouse_view(request):
    return render(request, 'warehouse.html')
"""страница склада материалов"""


def production_view(request):
    return render(request, 'production.html')
"""страница производства"""


def finished_goods_warehouse_view(request):
    return render(request, 'finished_goods_warehouse.html')
"""страница склада готовой продукции"""


def production_main(request):
    return render(request, 'production_main.html')
"""страница производства"""


def create_line(request):
    return render(request, 'stub.html', {'message': 'Create Line Page'})
"""функция создания линии"""


def add_product_to_line(request):
    return render(request, 'stub.html', {'message': 'Add Product to Line Page'})
"""добавление продукта на линию"""


def create_batch(request):
    return render(request, 'stub.html', {'message': 'Create Batch Page'})
"""функция создания партии"""


def warehouse(request):
    return render(request, 'warehouse.html')
"""страница склада"""


def view_stock(request):
    return render(request, 'stub.html', {'message': 'Просмотр остатков'})
"""функция просмотра остатков материала"""


def receive_materials(request):
    return render(request, 'stub.html', {'message': 'Прием материалов на склад'})
"""функция приемки материалов"""


def write_off_stock(request):
    return render(request, 'stub.html', {'message': 'Списание остатков'})
"""списываем излишки"""


def check_expenses(request):
    return render(request, 'stub.html', {'message': 'Проверка расхода за период'})
"""проверка расходов выбранный день или период"""


def view_finished_goods_stock(request):
    return render(request, 'stub.html', {'message': 'Просмотр остатков готовой продукции'})
"""просмотр остатков готовых позицый"""


def receive_finished_goods(request):
    return render(request, 'stub.html', {'message': 'Поступление готовой продукции за период'})
"""функция поступления из производства"""



def ship_finished_goods(request):
    return render(request, 'stub.html', {'message': 'Отгрузка готовой продукции'})
"""функция отгрузки товара и списания с остатка"""