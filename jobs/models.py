from django.contrib.auth import get_user_model
from django.db import models

from users.models import Employer
from .choices import IndustryCh, CategoryCh, SpecialityCh, ExperienceCh

User = get_user_model()

parametersForNull = {
    'null': True,
    'blank': True,
}


class Industry(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название отрасли',
        choices=IndustryCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Название отрасли(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отрасль"
        verbose_name_plural = "Отрасли"


class Category(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название категории',
        choices=CategoryCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Название категории(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Speciality(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название специализации',
        choices=SpecialityCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Название специализации(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Experience(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Уровень опыта',
        choices=ExperienceCh,
        default=None,
        **parametersForNull
    )
    other_title = models.CharField(
        max_length=250,
        verbose_name='Уровень опыта(другое)',
        **parametersForNull
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Уровень опыта"
        verbose_name_plural = "Уровени опыта"


class Vacancy(models.Model):
    industry = models.ManyToManyField(
        Industry,
        verbose_name='Отрасль'
    )
    category = models.ManyToManyField(
        Category,
        verbose_name='Категория'
    )
    specializing = models.ManyToManyField(
        Speciality,
        verbose_name='Специализация'
    )
    experience = models.ManyToManyField(
        Experience,
        verbose_name='Уровень опыта'
    )
    salary = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00,
        verbose_name='Зарплата'
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Локация'
    )
    company = models.ManyToManyField(
        Employer,
        verbose_name='компания'
    )
    published_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Актуально'),
            (2, 'Не актуально')
        ),
        default=2
    )
    contacts = models.CharField(
        max_length=13,
        unique=True,
        verbose_name='Контакты'
    )

    def __str__(self):
        specializations = ', '.join([specialization.title for specialization in self.specializing.all()])
        categories = ', '.join([category.title for category in self.category.all()])
        industries = ', '.join([industry.title for industry in self.industry.all()])
        experiences = ', '.join([experience.title for experience in self.experience.all()])
        return f'{specializations}\n {categories}\n {industries}\n {experiences}'

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Response(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.PROTECT,
        verbose_name='Выберите вакансию'
    )
    cover_letter = models.TextField(
        verbose_name='Сопроводительное письмо'
    )
    created_at = models.DateTimeField(
        auto_now_add=True)
    resume = models.FileField(
        upload_to="media/resume",
        verbose_name='Добавьте свое резюме'
    )

    def __str__(self):
        return f'{self.user.username} откликнулся на вакансию :{self.vacancy}'

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"


class Chosen(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.PROTECT,
        verbose_name='Выберите вакансию'
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} --> {self.vacancy}"

    class Meta:
        verbose_name = "Избранный"
        verbose_name_plural = "Избранные"

