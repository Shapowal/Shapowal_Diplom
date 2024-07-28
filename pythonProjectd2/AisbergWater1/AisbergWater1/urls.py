from django.contrib import admin
from django.urls import path, include
from sklad1 import views as sklad1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', sklad1_views.register, name='register'),
    path('login/', sklad1_views.login_view, name='login'),
    path('production/', sklad1_views.production_view, name='production'),
    path('warehouse/', sklad1_views.warehouse_view, name='warehouse'),
    path('finished_goods_warehouse/', sklad1_views.finished_goods_warehouse_view, name='finished_goods_warehouse'),
    path('', sklad1_views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('production_main/', sklad1_views.production_main, name='production_main'),
    path('create_line/', sklad1_views.create_line, name='create_line'),
    path('add_product_to_line/', sklad1_views.add_product_to_line, name='add_product_to_line'),
    path('create_batch/', sklad1_views.create_batch, name='create_batch'),
    path('view_stock/', sklad1_views.view_stock, name='view_stock'),
    path('receive_materials/', sklad1_views.receive_materials, name='receive_materials'),
    path('write_off_stock/', sklad1_views.write_off_stock, name='write_off_stock'),
    path('check_expenses/', sklad1_views.check_expenses, name='check_expenses'),
    path('view_finished_goods_stock/', sklad1_views.view_finished_goods_stock, name='view_finished_goods_stock'),
    path('receive_finished_goods/', sklad1_views.receive_finished_goods, name='receive_finished_goods'),
    path('ship_finished_goods/', sklad1_views.ship_finished_goods, name='ship_finished_goods'),
]