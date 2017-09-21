from django.db import models
from django.utils import timezone


class Post(models.Model):#Наследуемся из класса Моделс
    author = models.ForeignKey('auth.User') # ForeignKey - это id. Взять данные из другой таблицы+ ее имя. Чтобы все время не логинился
    title = models.CharField(max_length=200, blank=False, null=False)# Это текстовое поле в 1 линию
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save() # ОТдельно, т..к срабатывает после публикации. И тогда записывает не дату создания, а публикации

    def __str__(self):
        return self.title # Для того чтобы видели название базы данных,  ане объект ...
