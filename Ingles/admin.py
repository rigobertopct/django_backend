from django.contrib import admin

# Register your models here.
from Ingles.models import *


@admin.register(Menu_EN)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['item']


@admin.register(Title_EN)
class TitleAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Cover_EN)
class CoverAdmin(admin.ModelAdmin):
    list_display = ['text_h3', 'text_h1', 'image', 'boton_text']


@admin.register(OWR_Services_EN)
class OWR_ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']


@admin.register(Services_EN)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['icono', 'name', 'text']


@admin.register(Presentation_EN)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['title', 'subitle', 'video_link']


@admin.register(Our_Work_EN)
class Our_WorkAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category_EN)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image']


@admin.register(See_More_EN)
class See_MoreAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'button_text']


@admin.register(Features_EN)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image']


@admin.register(Item_Features_EN)
class Item_FeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'icon']


@admin.register(Team_EN)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Worker_EN)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'ocupation', 'short_phrase', 'long_phrase']


@admin.register(Scoreboard_EN)
class ScoreboardAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'icon']


@admin.register(Prices_EN)
class PricesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Services_Prices_EN)
class Services_PricesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'price']


@admin.register(services_list_EN)
class services_listAdmin(admin.ModelAdmin):
    list_display = ['service', 'name']


@admin.register(Testimonials_EN)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['testimonial', 'author', 'ocupation']


@admin.register(Lastest_Post_EN)
class Lastest_PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Posts_EN)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['image', 'author', 'date', 'comentarios', 'content', 'button_text']


@admin.register(Suscribe_EN)
class SuscribeAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'input_placeholder', 'button_text']


@admin.register(Contact_Form_EN)
class Contact_FormAdmin(admin.ModelAdmin):
    list_display = ['title', 'name_placeholder', 'email_placeholder', 'message_placeholder', 'button_text']


@admin.register(Social_links_EN)
class Social_linksAdmin(admin.ModelAdmin):
    list_display = ['facebook', 'twiter', 'skype', 'linkedin']
