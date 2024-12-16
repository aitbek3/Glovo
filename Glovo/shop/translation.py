from .models import Food
from modeltranslation.translator import TranslationOptions, register


@register(Food)
class ProductTranslationOptions(TranslationOptions):
    fields = ('resto_name', 'description')

