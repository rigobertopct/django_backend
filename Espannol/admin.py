from django.contrib import admin

# Register your models here.
from Espannol.models import *


@admin.register(Menu_ES)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['item']


@admin.register(Title_ES)
class TitleAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Cover_ES)
class CoverAdmin(admin.ModelAdmin):
    list_display = ['text_h3', 'text_h1', 'image', 'boton_text']


@admin.register(OWR_Services_ES)
class OWR_ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']


@admin.register(Services_ES)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['icono', 'name', 'text']


@admin.register(Presentation_ES)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['title', 'subitle', 'video_link']


@admin.register(Our_Work_ES)
class Our_WorkAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category_ES)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image']


@admin.register(See_More_ES)
class See_MoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'button_text']


@admin.register(Features_ES)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image']


@admin.register(Item_Features_ES)
class Item_FeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'icon']


@admin.register(Team_ES)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Worker_ES)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'ocupation', 'short_phrase', 'long_phrase']


@admin.register(Scoreboard_ES)
class ScoreboardAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'icon']


@admin.register(Prices_ES)
class PricesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Services_Prices_ES)
class Services_PricesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'price']


@admin.register(services_list_ES)
class services_listAdmin(admin.ModelAdmin):
    list_display = ['service', 'name']


@admin.register(Testimonials_ES)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['testimonial', 'author', 'ocupation']


@admin.register(Lastest_Post_ES)
class Lastest_PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Posts_ES)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['image', 'author', 'date', 'comentarios', 'content', 'button_text']


@admin.register(Suscribe_ES)
class SuscribeAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'input_placeholder', 'button_text']


@admin.register(Contact_Form_ES)
class Contact_FormAdmin(admin.ModelAdmin):
    list_display = ['title', 'name_placeholder', 'email_placeholder', 'message_placeholder', 'button_text']


@admin.register(Social_links_ES)
class Social_linksAdmin(admin.ModelAdmin):
    list_display = ['facebook', 'twiter', 'skype', 'linkedin']
