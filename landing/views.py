from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .models import Manager, VisaDirection, Testimonial, SiteConfiguration
from .forms import ContactForm


class HomeView(FormView):
    """Главная страница с формой обратной связи"""
    template_name = 'landing/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('landing:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Получаем настройки сайта (создаем, если не существуют)
        config, created = SiteConfiguration.objects.get_or_create()
        
        context.update({
            'site_config': config,
            'managers': Manager.objects.all(),
            'visa_directions': VisaDirection.objects.all(),
            'testimonials': Testimonial.objects.filter(is_active=True),
        })
        
        return context
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, _('Спасибо! Ваше сообщение отправлено. Мы свяжемся с вами в ближайшее время.'))
        return super().form_valid(form)