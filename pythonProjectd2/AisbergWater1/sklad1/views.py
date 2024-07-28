from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('production')  # Перенаправление на страницу производства
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

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

def home(request):
    return render(request, 'home.html')

def warehouse_view(request):
    return render(request, 'warehouse.html')

def production_view(request):
    return render(request, 'production.html')

def finished_goods_warehouse_view(request):
    return render(request, 'finished_goods_warehouse.html')

def production_main(request):
    return render(request, 'production_main.html')


def production_main(request):
    return render(request, 'production_main.html')

def create_line(request):
    return render(request, 'stub.html', {'message': 'Create Line Page'})

def add_product_to_line(request):
    return render(request, 'stub.html', {'message': 'Add Product to Line Page'})

def create_batch(request):
    return render(request, 'stub.html', {'message': 'Create Batch Page'})

def warehouse(request):
    return render(request, 'warehouse.html')

def view_stock(request):
    return render(request, 'stub.html', {'message': 'Просмотр остатков'})

def receive_materials(request):
    return render(request, 'stub.html', {'message': 'Прием материалов на склад'})

def write_off_stock(request):
    return render(request, 'stub.html', {'message': 'Списание остатков'})

def check_expenses(request):
    return render(request, 'stub.html', {'message': 'Проверка расхода за период'})

def view_finished_goods_stock(request):
    return render(request, 'stub.html', {'message': 'Просмотр остатков готовой продукции'})

def receive_finished_goods(request):
    return render(request, 'stub.html', {'message': 'Поступление готовой продукции за период'})

def ship_finished_goods(request):
    return render(request, 'stub.html', {'message': 'Отгрузка готовой продукции'})