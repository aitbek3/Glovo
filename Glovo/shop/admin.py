from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(UserProfile)
admin.site.register(Courier)
admin.site.register(Category)
# admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Rating)
admin.site.register(Review)


@admin.register(Food)
class ProductAdmin(TranslationAdmin):
    list_display = ("resto_name", "description")

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




