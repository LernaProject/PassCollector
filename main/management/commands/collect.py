from django.contrib.auth.models  import User as DjangoUser
from django.core.management.base import BaseCommand
from django.utils.six.moves      import input

from main.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-u", "--id", type=int, required=True)

    def handle(self, id, **options):
        login = input()
        email = input()
        username = input()
        passwd = input()

        try:
            u = User.objects.get(user_id=id)
        except User.DoesNotExist:
            User.objects.create(
                django_user=DjangoUser.objects.create_user(login, email, passwd),
                user_id=id,
                username=username,
            )
        else:
            u.django_user.username = login
            u.django_user.email = email
            u.django_user.set_password(passwd)
            u.django_user.save()
            u.username = username
            u.save()
