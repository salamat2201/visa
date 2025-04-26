from django.db import models
from django.utils.translation import gettext_lazy as _


class Manager(models.Model):
    """Модель для менеджеров компании"""
    name = models.CharField(_("Имя"), max_length=100)
    position = models.CharField(_("Должность"), max_length=100)
    description = models.TextField(_("Описание"), blank=True)
    photo = models.ImageField(_("Фотография"), upload_to="managers/", blank=True)
    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Телефон"), max_length=20, blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    
    class Meta:
        verbose_name = _("Менеджер")
        verbose_name_plural = _("Менеджеры")
        ordering = ["order", "name"]
    
    def __str__(self):
        return self.name


class VisaDirection(models.Model):
    """Модель для направлений виз"""
    country_name = models.CharField(_("Название страны"), max_length=100)
    flag = models.ImageField(_("Флаг"), upload_to="flags/", blank=True)
    description = models.TextField(_("Описание"))
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    
    class Meta:
        verbose_name = _("Направление визы")
        verbose_name_plural = _("Направления виз")
        ordering = ["order", "country_name"]
    
    def __str__(self):
        return self.country_name


class Testimonial(models.Model):
    """Модель для отзывов клиентов"""
    client_name = models.CharField(_("Имя клиента"), max_length=100)
    client_photo = models.ImageField(_("Фотография клиента"), upload_to="testimonials/", blank=True)
    text = models.TextField(_("Текст отзыва"))
    rating = models.PositiveSmallIntegerField(_("Оценка"), choices=[(i, i) for i in range(1, 6)], default=5)
    date_added = models.DateField(_("Дата добавления"), auto_now_add=True)
    is_active = models.BooleanField(_("Активен"), default=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    
    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")
        ordering = ["order", "-date_added"]
    
    def __str__(self):
        return f"{self.client_name} - {self.rating}/5"


class ContactMessage(models.Model):
    """Модель для сообщений из формы обратной связи"""
    name = models.CharField(_("Имя"), max_length=100)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Телефон"), max_length=20, blank=True)
    message = models.TextField(_("Сообщение"))
    date_sent = models.DateTimeField(_("Дата отправки"), auto_now_add=True)
    is_processed = models.BooleanField(_("Обработано"), default=False)
    
    class Meta:
        verbose_name = _("Сообщение")
        verbose_name_plural = _("Сообщения")
        ordering = ["-date_sent"]
    
    def __str__(self):
        return f"{self.name} - {self.date_sent.strftime('%d.%m.%Y %H:%M')}"


class SiteConfiguration(models.Model):
    """Модель для конфигурации сайта"""
    site_name = models.CharField(_("Название сайта"), max_length=100, default="EuroWork2020")
    site_slogan = models.CharField(_("Слоган"), max_length=200, blank=True)
    about_text = models.TextField(_("О нас"), blank=True)
    address = models.TextField(_("Адрес"), blank=True)
    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Телефон"), max_length=100, blank=True)
    whatsapp = models.CharField(_("WhatsApp"), max_length=100, blank=True)
    telegram = models.CharField(_("Telegram"), max_length=100, blank=True)
    instagram = models.CharField(_("Instagram"), max_length=100, blank=True)
    
    class Meta:
        verbose_name = _("Конфигурация сайта")
        verbose_name_plural = _("Конфигурация сайта")
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        # Всегда должна быть только одна запись конфигурации
        if not self.pk and SiteConfiguration.objects.exists():
            return
        return super().save(*args, **kwargs)