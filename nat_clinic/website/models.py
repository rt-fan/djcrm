from django.db import models
from django.urls import reverse


class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Clients(models.Model):
    first_name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=True, verbose_name='Фамилия')
    photo_passport = models.ImageField(upload_to="passport/%Y/%m/%d/", null=True, verbose_name='Фото паспорта')
    phone = models.CharField(max_length=50, null=True, verbose_name='Номер телефона')
    age = models.IntegerField(null=True, verbose_name='Год рождения')
    rating = models.FloatField(default=10, null=True, verbose_name='Рейтинг')
    comments = models.TextField(default='---', null=True, verbose_name='Комментарии')
    history = models.TextField(null=True, verbose_name='История посещений')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.pk} {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']


class Tasks(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='ФИО')
    clients = models.ManyToManyField(Clients, verbose_name='Клиент', related_name='taski')
    phone = models.CharField(max_length=50, null=True, verbose_name='Номер телефона')
    potok = models.CharField(max_length=50, null=True, verbose_name='Дата начала недели')
    room = models.CharField(max_length=50, null=True, verbose_name='Комната')
    status = models.CharField(max_length=50, null=True, verbose_name='Статус')
    money = models.CharField(max_length=50, null=True, verbose_name='Оплачено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.pk} {self.clients} {self.potok} {self.room} {self.status} {self.money} {self.created_at}"

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


class TestTable(models.Model):
    name = models.ForeignKey(Clients, null=True, on_delete=models.PROTECT)
    task = models.ForeignKey(Tasks, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.pk} {self.name} {self.task}"


class Divisions(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Наименование')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Подразделения'
        verbose_name_plural = 'Подразделения'
        ordering = ['id']


class Staff(models.Model):
    first_name = models.CharField(max_length=50, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=True, verbose_name='Фамилия')
    photo_passport = models.ImageField(upload_to="passport/%Y/%m/%d/", null=True, verbose_name='Фото паспорта')
    phone = models.CharField(max_length=50, null=True, verbose_name='Номер телефона')
    age = models.CharField(max_length=50, null=True, verbose_name='Дата рождения')
    rating = models.FloatField(default=10, null=True, verbose_name='Рейтинг')
    division = models.ForeignKey(Divisions, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.pk} {self.first_name} {self.last_name} {self.phone} {self.division} {self.photo_passport}"

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'
        ordering = ['-created_at']

