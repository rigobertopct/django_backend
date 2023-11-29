from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Title_EN(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Título'


class Menu_EN(models.Model):
    item = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Menu'


class Cover_EN(models.Model):
    text_h3 = models.CharField(max_length=255)
    text_h1 = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banner')
    boton_text = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Cover'


class OWR_Services_EN(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Mis servicios'


class Services_EN(models.Model):
    icono = models.ImageField(upload_to='icono_servicio')
    name = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Servicios'


class Presentation_EN(models.Model):
    title = models.CharField(max_length=255)
    subitle = models.TextField()
    video_link = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Presentaciones'


class Our_Work_EN(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Mis trabajos'


class Category_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name_plural = 'Categorias'


class See_More_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Ver mas'


class Features_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    image = models.ImageField(upload_to='features')

    class Meta:
        verbose_name_plural = 'Features'


class Item_Features_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    icon = models.ImageField(upload_to='features_item')

    class Meta:
        verbose_name_plural = 'Items features'


class Team_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = 'Equipo'


class Worker_EN(models.Model):
    name = models.CharField(max_length=100)
    ocupation = models.CharField(max_length=100)
    short_phrase = models.CharField(max_length=255)
    long_phrase = models.TextField()

    class Meta:
        verbose_name_plural = 'Trabjadores'


class Scoreboard_EN(models.Model):
    icon = models.ImageField(upload_to='scoreboard')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Scoreboard'


class Prices_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = 'Precios'


class Services_Prices_EN(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = 'Precios por servicios'


class services_list_EN(models.Model):
    service = models.ForeignKey(Services_Prices_EN, on_delete=CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Lista de servicios'


class Testimonials_EN(models.Model):
    testimonial = models.TextField()
    author = models.CharField(max_length=100)
    ocupation = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Testimonios'


class Lastest_Post_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = 'Ultimos post'


class Posts_EN(models.Model):
    image = models.ImageField(upload_to='posts')
    author = models.CharField(max_length=100)
    date = models.DateField()
    comentarios = models.IntegerField()
    content = models.TextField()
    button_text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Post'


class Suscribe_EN(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    input_placeholder = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Suscripcion'


class Contact_Form_EN(models.Model):
    title = models.CharField(max_length=255)
    name_placeholder = models.CharField(max_length=100)
    email_placeholder = models.CharField(max_length=100)
    message_placeholder = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Formulario de contacto'


class Social_links_EN(models.Model):
    facebook = models.CharField(max_length=255)
    twiter = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Links sociales'
