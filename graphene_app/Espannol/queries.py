import graphene
from graphene_django.types import DjangoObjectType

from Espannol.models import *


class Title_ESType(DjangoObjectType):
    class Meta:
        model = Title_ES
        fields = '__all__'


class Menu_ESType(DjangoObjectType):
    class Meta:
        model = Menu_ES
        fields = '__all__'


class Cover_ESType(DjangoObjectType):
    class Meta:
        model = Cover_ES
        fields = '__all__'


class OWR_Services_ESType(DjangoObjectType):
    class Meta:
        model = OWR_Services_ES
        fields = '__all__'


class Services_ESType(DjangoObjectType):
    class Meta:
        model = Services_ES
        fields = '__all__'


class Presentation_ESType(DjangoObjectType):
    class Meta:
        model = Presentation_ES
        fields = '__all__'


class Our_Work_ESType(DjangoObjectType):
    class Meta:
        model = Our_Work_ES
        fields = '__all__'


class Category_ESType(DjangoObjectType):
    class Meta:
        model = Category_ES
        fields = '__all__'


class See_More_ESType(DjangoObjectType):
    class Meta:
        model = See_More_ES
        fields = '__all__'


class Features_ESType(DjangoObjectType):
    class Meta:
        model = Features_ES
        fields = '__all__'


class Item_Features_ESType(DjangoObjectType):
    class Meta:
        model = Item_Features_ES
        fields = '__all__'


class Team_ESType(DjangoObjectType):
    class Meta:
        model = Team_ES
        fields = '__all__'


class Worker_ESType(DjangoObjectType):
    class Meta:
        model = Worker_ES
        fields = '__all__'


class Scoreboard_ESType(DjangoObjectType):
    class Meta:
        model = Scoreboard_ES
        fields = '__all__'


class Prices_ESType(DjangoObjectType):
    class Meta:
        model = Prices_ES
        fields = '__all__'


class Services_Prices_ESType(DjangoObjectType):
    class Meta:
        model = Services_Prices_ES
        fields = '__all__'


class services_list_ESType(DjangoObjectType):
    class Meta:
        model = services_list_ES
        fields = '__all__'


class Testimonials_ESType(DjangoObjectType):
    class Meta:
        model = Testimonials_ES
        fields = '__all__'


class Lastest_Post_ESType(DjangoObjectType):
    class Meta:
        model = Lastest_Post_ES
        fields = '__all__'


class Posts_ESType(DjangoObjectType):
    class Meta:
        model = Posts_ES
        fields = '__all__'


class Suscribe_ESType(DjangoObjectType):
    class Meta:
        model = Suscribe_ES
        fields = '__all__'


class Contact_Form_ESType(DjangoObjectType):
    class Meta:
        model = Contact_Form_ES
        fields = '__all__'


class Social_links_ESType(DjangoObjectType):
    class Meta:
        model = Social_links_ES
        fields = '__all__'


class Query(object):
    query_Title_ES = graphene.List(Title_ESType)
    query_Menu_ES = graphene.List(Menu_ESType)
    query_Cover_ES = graphene.List(Cover_ESType)
    query_OWR_Services_ES = graphene.List(OWR_Services_ESType)
    query_Services_ES = graphene.List(Services_ESType)
    query_Presentation_ES = graphene.List(Presentation_ESType)
    query_Our_Work_ES = graphene.List(Our_Work_ESType)
    query_Category_ES = graphene.List(Category_ESType)
    query_See_More_ES = graphene.List(See_More_ESType)
    query_Features_ES = graphene.List(Features_ESType)
    query_Item_Features_ES = graphene.List(Item_Features_ESType)
    query_Team_ES = graphene.List(Team_ESType)
    query_Worker_ES = graphene.List(Worker_ESType)
    query_Scoreboard_ES = graphene.List(Scoreboard_ESType)
    query_Prices_ES = graphene.List(Prices_ESType)
    query_Services_Prices_ES = graphene.List(Services_Prices_ESType)
    query_services_list_ES = graphene.List(services_list_ESType)
    query_Testimonials_ES = graphene.List(Testimonials_ESType)
    query_Lastest_Post_ES = graphene.List(Lastest_Post_ESType)
    query_Posts_ES = graphene.List(Posts_ESType)
    query_Suscribe_ES = graphene.List(Suscribe_ESType)
    query_Contact_Form_ES = graphene.List(Contact_Form_ESType)
    query_Social_links_ES = graphene.List(Social_links_ESType)

    def resolve_query_Title_ES(self, info):
        return Title_ES.objects.all()

    def resolve_query_Menu_ES(self, info):
        return Menu_ES.objects.all()

    def resolve_query_Cover_ES(self, info):
        return Cover_ES.objects.all()

    def resolve_query_OWR_Services_ES(self, info):
        return OWR_Services_ES.objects.all()

    def resolve_query_Services_ES(self, info):
        return Services_ES.objects.all()

    def resolve_query_Presentation_ES(self, info):
        return Presentation_ES.objects.all()

    def resolve_query_Our_Work_ES(self, info):
        return Our_Work_ES.objects.all()

    def resolve_query_Category_ES(self, info):
        return Category_ES.objects.all()

    def resolve_query_See_More_ES(self, info):
        return See_More_ES.objects.all()

    def resolve_query_Features_ES(self, info):
        return Features_ES.objects.all()

    def resolve_query_Item_Features_ES(self, info):
        return Item_Features_ES.objects.all()

    def resolve_query_Team_ES(self, info):
        return Team_ES.objects.all()

    def resolve_query_Worker_ES(self, info):
        return Worker_ES.objects.all()

    def resolve_query_Scoreboard_ES(self, info):
        return Scoreboard_ES.objects.all()

    def resolve_query_Prices_ES(self, info):
        return Prices_ES.objects.all()

    def resolve_query_Services_Prices_ES(self, info):
        return Services_Prices_ES.objects.all()

    def resolve_query_services_list_ES(self, info):
        return services_list_ES.objects.all()

    def resolve_query_Testimonials_ES(self, info):
        return Testimonials_ES.objects.all()

    def resolve_query_Lastest_Post_ES(self, info):
        return Lastest_Post_ES.objects.all()

    def resolve_query_Posts_ES(self, info):
        return Posts_ES.objects.all()

    def resolve_query_Suscribe_ES(self, info):
        return Suscribe_ES.objects.all()

    def resolve_query_Contact_Form_ES(self, info):
        return Contact_Form_ES.objects.all()

    def resolve_query_Social_links_ES(self, info):
        return Social_links_ES.objects.all()
