from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
# from django import template
# from django.contrib.auth.models import User, Group
from django.contrib import messages
from .forms import *
from .models import *


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "You've been logged in")
            return redirect("home")
        else:
            # messages.warning(request, "A mistake occured, Try one more time")
            return redirect("home")
    else:
        return render(request, "website/home.html")


def logout_user(request):
    logout(request)
    # messages.success(request, "You logged out")
    return redirect("home")


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, "You've been registered in")
            return redirect("home")
        # else:
        #     messages.error(request, "An error occured during registration")

    return render(request, "website/register.html", {"form": form})


def test(request):
    records = Record.objects.all()
    if request.user.is_authenticated:
        return render(request, "website/test.html", {"records": records})
    else:
        return redirect("home")


def test_template(request):
    """
    Тестовая страница, где реализована проверка пользователя на группу
    """
    user = request.user
    if request.user.is_authenticated:
        print(user.groups.filter(name__in=['Несуществующая_группа', 'Персонал']).exists())
        return render(request, "website/test_template.html")
    else:
        return redirect("home")


def record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, "website/record.html", {"record": record})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_record = form.save()
            # messages.success(request, f"Record {add_record.first_name} was added")
            return redirect("test")
        return render(request, "website/add_record.html", {"form": form})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            updated_record = form.save()
            # messages.success(request, f"Record '{updated_record.first_name}' was added")
            return redirect("test")
        return render(request, "website/update_record.html", {"form": form})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        del_record = Record.objects.get(id=pk)
        del_record.delete()
        # messages.success(request, "You deleted the record")
        return redirect("test")
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def task_search(request):
    form = SearchForm(request.POST)
    results = []

    if form.is_valid() and request.POST['query']:
        query = form.cleaned_data['query']
        results = Tasks.objects.filter(phone__icontains=query) | \
                  Tasks.objects.filter(money__icontains=query) | \
                  Tasks.objects.filter(status__icontains=query) | \
                  Tasks.objects.filter(phone__icontains=query).order_by('-pk')

        if not results:

            results = Tasks.objects.filter(clients__first_name__icontains=query) | \
                      Tasks.objects.filter(clients__last_name__icontains=query).order_by('-pk')
    return render(request, 'website/task_search.html', {'form': form, 'results': results})


def tasks(request):
    if request.user.is_authenticated:
        tasks = Tasks.objects.order_by('-pk')
        form = SearchForm(request.POST)
        return render(request, "website/tasks.html", {"tasks": tasks, "clients": clients, 'form': form})
    else:
        return redirect("home")


def task(request, pk):
    if request.user.is_authenticated:
        task = Tasks.objects.get(id=pk)
        return render(request, "website/task.html", {"task": task})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def add_task(request):
    form = AddTaskForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_task = form.save()
            # messages.success(request, f"Record was added")
            return redirect("tasks")
        return render(request, "website/add_task.html", {"form": form})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def update_task(request, pk):
    if request.user.is_authenticated:
        task = Tasks.objects.get(id=pk)
        form = AddTaskForm(request.POST or None, instance=task)
        if form.is_valid():
            updated_task = form.save()
            # messages.success(request, f"Record '{updated_task.name}' was added")
            return redirect("tasks")
        return render(request, "website/update_task.html", {"form": form})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def delete_task(request, pk):
    if request.user.is_authenticated:
        del_task = Tasks.objects.get(id=pk)
        del_task.delete()
        # messages.success(request, "You deleted the record")
        return redirect("tasks")
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def client_search(request):
    form = SearchForm(request.POST)
    results = []

    if form.is_valid() and request.POST['query']:
        query = form.cleaned_data['query']
        results = Clients.objects.filter(first_name__icontains=query) | \
                  Clients.objects.filter(last_name__icontains=query) | \
                  Clients.objects.filter(phone__icontains=query) | \
                  Clients.objects.filter(age__icontains=query) | \
                  Clients.objects.filter(rating__icontains=query) | \
                  Clients.objects.filter(comments__icontains=query) | \
                  Clients.objects.filter(created_at__icontains=query).order_by('-pk')
    return render(request, 'website/client_search.html', {'form': form, 'results': results})


def clients(request):
    if request.user.is_authenticated:
        clients = Clients.objects.order_by('-pk')
        form = SearchForm(request.POST)
        return render(request, "website/clients.html", {"clients": clients, 'form': form})
    else:
        return redirect("home")


def client(request, pk):
    if request.user.is_authenticated:
        client = Clients.objects.get(id=pk)
        return render(request, "website/client.html", {"client": client})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def add_client(request):
    form = AddClientForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            # messages.success(request, f"Record was added")
            return redirect("clients")
        return render(request, "website/add_client.html", {"form": form})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def update_client(request, pk):
    if request.user.is_authenticated:
        client = Clients.objects.get(id=pk)
        form = AddClientForm(request.POST or None, instance=client)
        if form.is_valid():
            form.save()
            # messages.success(request, f"Record was updated")
            return redirect("clients")
        return render(request, "website/update_client.html", {"form": form})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def delete_client(request, pk):
    if request.user.is_authenticated:
        del_client = Clients.objects.get(id=pk)
        del_client.delete()
        # messages.success(request, "You deleted the record")
        return redirect("clients")
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def divisions(request):
    if request.user.is_authenticated:
        divisions = Divisions.objects.order_by('-pk')
        user = request.user
        group_is = user.groups.filter(name__in=['Несуществующая_группа', 'Персонал']).exists()
        return render(request, "website/staffs.html", {"divisions": divisions, "group_is": group_is})
    else:
        return redirect("home")


def staff_search(request):
    form = SearchForm(request.POST)
    results = []

    if form.is_valid() and request.POST['query']:
        query = form.cleaned_data['query']
        results = Staff.objects.filter(first_name__icontains=query) | \
                  Staff.objects.filter(last_name__icontains=query) | \
                  Staff.objects.filter(phone__icontains=query) | \
                  Staff.objects.filter(age__icontains=query) | \
                  Staff.objects.filter(division__name__icontains=query) | \
                  Staff.objects.filter(rating__icontains=query).order_by('-pk')
    return render(request, 'website/staff_search.html', {'form': form, 'results': results})


def staffs(request):
    if request.user.is_authenticated:
        staffs = Staff.objects.order_by('-pk')
        print(staffs)
        form = SearchForm(request.POST)
        return render(request, "website/staffs.html", {'staffs': staffs, 'form': form})
    else:
        return redirect("home")


def staff(request, pk):
    if request.user.is_authenticated:
        staff = Staff.objects.get(id=pk)
        return render(request, "website/staff.html", {"staff": staff})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def add_staff(request):
    form = AddStaffForm(request.POST or None, request.FILES)
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            # messages.success(request, f"Record was added")
            return redirect("staffs")
        return render(request, "website/add_staff.html", {"form": form})
    else:
        # messages.error(request, "You have to login")
        return redirect("home")


def services(request):
    if request.user.is_authenticated:
        return render(request, "website/services.html")
    else:
        return redirect("home")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')