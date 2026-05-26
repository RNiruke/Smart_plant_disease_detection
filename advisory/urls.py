from django.urls import path
from . import views

app_name = 'advisory'

urlpatterns = [
    path('', views.advisory_list_view, name='list'),
    path('<str:disease_key>/',
         views.advisory_detail_view,
         name='detail'),

    # ── Admin CRUD Panel (staff only) ─────────────────────────────────────
    path('admin-panel/advisory/', views.advisory_admin_table, name='admin_table'),
    path('admin-panel/advisory/add/', views.advisory_admin_add, name='admin_add'),
    path('admin-panel/advisory/edit/<int:pk>/', views.advisory_admin_edit, name='admin_edit'),
    path('admin-panel/advisory/delete/<int:pk>/', views.advisory_admin_delete, name='admin_delete'),
]
