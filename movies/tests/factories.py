import factory.fuzzy
from django.contrib.auth.models import User

from movies import models


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyChoice([x[0] for x in models.Category.CategoryName.choices])
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)

    class Meta:
        model = models.Category


class ActorFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    birth_place = factory.Faker('country_code')

    class Meta:
        model = models.Actor


class PictureFactory(factory.django.DjangoModelFactory):
    actor = factory.SubFactory(ActorFactory)
    image = factory.django.ImageField()

    class Meta:
        model = models.Picture


class MovieFactory(factory.django.DjangoModelFactory):
    file = factory.django.FileField()
    title = factory.fuzzy.FuzzyText()
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def actors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for actor in extracted:
                self.actors.add(actor)

    class Meta:
        model = models.Movie


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: "user_%d" % n)
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')

    class Meta:
        model = User


class AccessFactory(factory.django.DjangoModelFactory):
    movie = factory.SubFactory(MovieFactory)
    user = factory.SubFactory(UserFactory)
    has_access = 'True'

    class Meta:
        model = models.Access
