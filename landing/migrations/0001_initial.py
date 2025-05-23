# Generated by Django 4.2.7 on 2025-04-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Обработано')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['-date_sent'],
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('position_ru', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('position_uz', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('position_tg', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('position_ky', models.CharField(max_length=100, null=True, verbose_name='Должность')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_tg', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='managers/', verbose_name='Фотография')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='EuroWork2020', max_length=100, verbose_name='Название сайта')),
                ('site_slogan', models.CharField(blank=True, max_length=200, verbose_name='Слоган')),
                ('site_slogan_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='Слоган')),
                ('site_slogan_uz', models.CharField(blank=True, max_length=200, null=True, verbose_name='Слоган')),
                ('site_slogan_tg', models.CharField(blank=True, max_length=200, null=True, verbose_name='Слоган')),
                ('site_slogan_ky', models.CharField(blank=True, max_length=200, null=True, verbose_name='Слоган')),
                ('about_text', models.TextField(blank=True, verbose_name='О нас')),
                ('about_text_ru', models.TextField(blank=True, null=True, verbose_name='О нас')),
                ('about_text_uz', models.TextField(blank=True, null=True, verbose_name='О нас')),
                ('about_text_tg', models.TextField(blank=True, null=True, verbose_name='О нас')),
                ('about_text_ky', models.TextField(blank=True, null=True, verbose_name='О нас')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('address_ru', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('address_uz', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('address_tg', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('address_ky', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='Телефон')),
                ('whatsapp', models.CharField(blank=True, max_length=100, verbose_name='WhatsApp')),
                ('telegram', models.CharField(blank=True, max_length=100, verbose_name='Telegram')),
                ('instagram', models.CharField(blank=True, max_length=100, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Конфигурация сайта',
                'verbose_name_plural': 'Конфигурация сайта',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Имя клиента')),
                ('client_photo', models.ImageField(blank=True, upload_to='testimonials/', verbose_name='Фотография клиента')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('text_ru', models.TextField(null=True, verbose_name='Текст отзыва')),
                ('text_uz', models.TextField(null=True, verbose_name='Текст отзыва')),
                ('text_tg', models.TextField(null=True, verbose_name='Текст отзыва')),
                ('text_ky', models.TextField(null=True, verbose_name='Текст отзыва')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, verbose_name='Оценка')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['order', '-date_added'],
            },
        ),
        migrations.CreateModel(
            name='VisaDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100, verbose_name='Название страны')),
                ('country_name_ru', models.CharField(max_length=100, null=True, verbose_name='Название страны')),
                ('country_name_uz', models.CharField(max_length=100, null=True, verbose_name='Название страны')),
                ('country_name_tg', models.CharField(max_length=100, null=True, verbose_name='Название страны')),
                ('country_name_ky', models.CharField(max_length=100, null=True, verbose_name='Название страны')),
                ('flag', models.ImageField(blank=True, upload_to='flags/', verbose_name='Флаг')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_uz', models.TextField(null=True, verbose_name='Описание')),
                ('description_tg', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Направление визы',
                'verbose_name_plural': 'Направления виз',
                'ordering': ['order', 'country_name'],
            },
        ),
    ]
