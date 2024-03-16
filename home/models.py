from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class Home(models.Model):
    tittle = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('subject'))
    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    about = models.TextField(null=True, blank=True, verbose_name=_('about'))
    attributes = models.TextField(null=True, blank=True, verbose_name=_('attributes'))
    production = models.TextField(null=True, blank=True, verbose_name=_('production'))
    phone = models.CharField(max_length=13, null=True, blank=True, verbose_name=_('phone'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('email'))
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('address'))
    image_manager = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('manager image'))
    image_symbol1 = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('icon image 1'))
    image_symbol2 = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('icon image 2'))
    image_symbol3 = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('icon image 3'))
    image_about = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('image about'))
    video = models.FileField(upload_to='video', null=True, blank=True,
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name=_('video'))

    class Meta:
        verbose_name = _('information')
        verbose_name_plural = _('Home')

    def __str__(self):
        return self.tittle


class Standard(models.Model):
    tittle = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('subject'))
    image_standard = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('standard symbol'))

    class Meta:
        verbose_name = _('standard')
        verbose_name_plural = _('standards')

    def __str__(self):
        return self.tittle


class About(models.Model):
    tittle_application = models.CharField(max_length=50, null=True, blank=True,
                                          verbose_name=_('Subject of application'))
    application = models.TextField(null=True, blank=True, verbose_name=_('application'))
    image = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('process image'))
    tittle_process = models.CharField(max_length=50, null=True, blank=True,
                                      verbose_name=_('the subject of the process'))
    process = models.TextField(null=True, blank=True, verbose_name=_('process'))
    tittle_manager = models.CharField(max_length=50, null=True, blank=True,
                                      verbose_name=_('the subject of the manager'))
    manager = models.TextField(null=True, blank=True, verbose_name=_('manager'))
    image_manager = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('manager image'))
    tittle_business = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('the subject of business'))
    business = models.TextField(null=True, blank=True, verbose_name=_('business'))

    class Meta:
        verbose_name = _('about us')
        verbose_name_plural = _('about us')

    def __str__(self):
        return self.tittle_application


class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('name'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('email'))
    phone = models.CharField(max_length=13, null=True, blank=True, verbose_name=_('phone'))
    message = models.TextField(null=True, blank=True, verbose_name=_('message'))

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('product name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    image = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('product image'))
    image_packing = models.ImageField(upload_to='image', null=True, blank=True,
                                      verbose_name=_('image of product packaging'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name


class Wallpaper(models.Model):
    wallpaper = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('wallpaper'))

    class Meta:
        verbose_name = _('wallpaper')
        verbose_name_plural = _('wallpapers')

        def __str__(self):
            return self.verbose_name


class Gallery(models.Model):
    image = models.ImageField(upload_to='image', null=True, blank=True, verbose_name=_('image'))

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')

        def __str__(self):
            return self.verbose_name
