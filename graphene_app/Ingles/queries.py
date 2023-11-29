import graphene
from graphene_django.types import DjangoObjectType

from Ingles.models import *


class Title_ENType(DjangoObjectType):
    class Meta:
        model = Title_EN
        fields = '__all__'


class Menu_ENType(DjangoObjectType):
    class Meta:
        model = Menu_EN
        fields = '__all__'


class Cover_ENType(DjangoObjectType):
    class Meta:
        model = Cover_EN
        fields = '__all__'


class OWR_Services_ENType(DjangoObjectType):
    class Meta:
        model = OWR_Services_EN
        fields = '__all__'


class Services_ENType(DjangoObjectType):
    class Meta:
        model = Services_EN
        fields = '__all__'


class Presentation_ENType(DjangoObjectType):
    class Meta:
        model = Presentation_EN
        fields = '__all__'


class Our_Work_ENType(DjangoObjectType):
    class Meta:
        model = Our_Work_EN
        fields = '__all__'


class Category_ENType(DjangoObjectType):
    class Meta:
        model = Category_EN
        fields = '__all__'


class See_More_ENType(DjangoObjectType):
    class Meta:
        model = See_More_EN
        fields = '__all__'


class Features_ENType(DjangoObjectType):
    class Meta:
        model = Features_EN
        fields = '__all__'


class Item_Features_ENType(DjangoObjectType):
    class Meta:
        model = Item_Features_EN
        fields = '__all__'


class Team_ENType(DjangoObjectType):
    class Meta:
        model = Team_EN
        fields = '__all__'


class Worker_ENType(DjangoObjectType):
    class Meta:
        model = Worker_EN
        fields = '__all__'


class Scoreboard_ENType(DjangoObjectType):
    class Meta:
        model = Scoreboard_EN
        fields = '__all__'


class Prices_ENType(DjangoObjectType):
    class Meta:
        model = Prices_EN
        fields = '__all__'


class Services_Prices_ENType(DjangoObjectType):
    class Meta:
        model = Services_Prices_EN
        fields = '__all__'


class services_list_ENType(DjangoObjectType):
    class Meta:
        model = services_list_EN
        fields = '__all__'


class Testimonials_ENType(DjangoObjectType):
    class Meta:
        model = Testimonials_EN
        fields = '__all__'


class Lastest_Post_ENType(DjangoObjectType):
    class Meta:
        model = Lastest_Post_EN
        fields = '__all__'


class Posts_ENType(DjangoObjectType):
    class Meta:
        model = Posts_EN
        fields = '__all__'


class Suscribe_ENType(DjangoObjectType):
    class Meta:
        model = Suscribe_EN
        fields = '__all__'


class Contact_Form_ENType(DjangoObjectType):
    class Meta:
        model = Contact_Form_EN
        fields = '__all__'


class Social_links_ENType(DjangoObjectType):
    class Meta:
        model = Social_links_EN
        fields = '__all__'


class Query(object):
    query_Title_EN = graphene.List(Title_ENType)
    query_Menu_EN = graphene.List(Menu_ENType)
    query_Cover_EN = graphene.List(Cover_ENType)
    query_OWR_Services_EN = graphene.List(OWR_Services_ENType)
    query_Services_EN = graphene.List(Services_ENType)
    query_Presentation_EN = graphene.List(Presentation_ENType)
    query_Our_Work_EN = graphene.List(Our_Work_ENType)
    query_Category_EN = graphene.List(Category_ENType)
    query_See_More_EN = graphene.List(See_More_ENType)
    query_Features_EN = graphene.List(Features_ENType)
    query_Item_Features_EN = graphene.List(Item_Features_ENType)
    query_Team_EN = graphene.List(Team_ENType)
    query_Worker_EN = graphene.List(Worker_ENType)
    query_Scoreboard_EN = graphene.List(Scoreboard_ENType)
    query_Prices_EN = graphene.List(Prices_ENType)
    query_Services_Prices_EN = graphene.List(Services_Prices_ENType)
    query_services_list_EN = graphene.List(services_list_ENType)
    query_Testimonials_EN = graphene.List(Testimonials_ENType)
    query_Lastest_Post_EN = graphene.List(Lastest_Post_ENType)
    query_Posts_EN = graphene.List(Posts_ENType)
    query_Suscribe_EN = graphene.List(Suscribe_ENType)
    query_Contact_Form_EN = graphene.List(Contact_Form_ENType)
    query_Social_links_EN = graphene.List(Social_links_ENType)

    def resolve_query_Title_EN(self, info):
        return Title_EN.objects.all()

    def resolve_query_Menu_EN(self, info):
        return Menu_EN.objects.all()

    def resolve_query_Cover_EN(self, info):
        return Cover_EN.objects.all()

    def resolve_query_OWR_Services_EN(self, info):
        return OWR_Services_EN.objects.all()

    def resolve_query_Services_EN(self, info):
        return Services_EN.objects.all()

    def resolve_query_Presentation_EN(self, info):
        return Presentation_EN.objects.all()

    def resolve_query_Our_Work_EN(self, info):
        return Our_Work_EN.objects.all()

    def resolve_query_Category_EN(self, info):
        return Category_EN.objects.all()

    def resolve_query_See_More_EN(self, info):
        return See_More_EN.objects.all()

    def resolve_query_Features_EN(self, info):
        return Features_EN.objects.all()

    def resolve_query_Item_Features_EN(self, info):
        return Item_Features_EN.objects.all()

    def resolve_query_Team_EN(self, info):
        return Team_EN.objects.all()

    def resolve_query_Worker_EN(self, info):
        return Worker_EN.objects.all()

    def resolve_query_Scoreboard_EN(self, info):
        return Scoreboard_EN.objects.all()

    def resolve_query_Prices_EN(self, info):
        return Prices_EN.objects.all()

    def resolve_query_Services_Prices_EN(self, info):
        return Services_Prices_EN.objects.all()

    def resolve_query_services_list_EN(self, info):
        return services_list_EN.objects.all()

    def resolve_query_Testimonials_EN(self, info):
        return Testimonials_EN.objects.all()

    def resolve_query_Lastest_Post_EN(self, info):
        return Lastest_Post_EN.objects.all()

    def resolve_query_Posts_EN(self, info):
        return Posts_EN.objects.all()

    def resolve_query_Suscribe_EN(self, info):
        return Suscribe_EN.objects.all()

    def resolve_query_Contact_Form_EN(self, info):
        return Contact_Form_EN.objects.all()

    def resolve_query_Social_links_EN(self, info):
        return Social_links_EN.objects.all()
