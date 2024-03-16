from modeltranslation.translator import translator, TranslationOptions
from .models import Home, Standard, About, Contact, Product


class HomeTranslationOptions(TranslationOptions):
    fields = ('tittle', 'description', 'about', 'attributes', 'production', 'address')


translator.register(Home, HomeTranslationOptions)


class StandardTranslationOptions(TranslationOptions):
    fields = ('tittle',)


translator.register(Standard, StandardTranslationOptions)


class AboutTranslationOptions(TranslationOptions):
    fields = ('tittle_application', 'application', 'tittle_process', 'process', 'tittle_manager', 'manager', 'tittle_business', 'business')


translator.register(About, AboutTranslationOptions)


class ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'message')


translator.register(Contact, ContactTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(Product, ProductTranslationOptions)
