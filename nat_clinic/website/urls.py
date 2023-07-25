from django.conf.urls.static import static
from django.urls import path

from nat_clinic import settings
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.register_user, name='register'),
    path("test/", views.test, name='test'),
    path("record/<int:pk>/", views.record, name='record'),
    path("delete_record/<int:pk>/", views.delete_record, name='delete_record'),
    path("update_record/<int:pk>/", views.update_record, name='update_record'),
    path("add_record/", views.add_record, name='add_record'),

    path("tasks/", views.tasks, name='tasks'),
    path("task/<int:pk>/", views.task, name='task'),
    path("add_task/", views.add_task, name='add_task'),
    path("update_task/<int:pk>/", views.update_task, name='update_task'),
    path("delete_task/<int:pk>/", views.delete_task, name='delete_task'),
    path('task_search/', views.task_search, name='task_search'),

    path("clients/", views.clients, name='clients'),
    path("client/<int:pk>/", views.client, name='client'),
    path("add_client/", views.add_client, name='add_client'),
    path("update_client/<int:pk>/", views.update_client, name='update_client'),
    path("delete_client/<int:pk>/", views.delete_client, name='delete_client'),
    path('client_search/', views.client_search, name='client_search'),

    path("test_template/", views.test_template, name='test_template'),

    path("divisions/", views.divisions, name='divisions'),
    path("staffs/", views.staffs, name='staffs'),
    path("staff/<int:pk>/", views.staff, name='staff'),
    path("add_staff/", views.add_staff, name='add_staff'),
    path("staff_search/", views.staff_search, name='staff_search'),

    path("services/", views.services, name='services'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

