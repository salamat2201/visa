from modeltranslation.translator import translator, TranslationOptions
from .models import Manager, VisaDirection, Testimonial, SiteConfiguration


class ManagerTranslationOptions(TranslationOptions):
    fields = ('position', 'description')


class VisaDirectionTranslationOptions(TranslationOptions):
    fields = ('country_name', 'description')


class TestimonialTranslationOptions(TranslationOptions):
    fields = ('text',)


class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('site_slogan', 'about_text', 'address')


# Регистрация моделей для перевода
translator.register(Manager, ManagerTranslationOptions)
translator.register(VisaDirection, VisaDirectionTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(SiteConfiguration, SiteConfigurationTranslationOptions)