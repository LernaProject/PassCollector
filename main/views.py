from django.contrib.auth.models import User as DjangoUser
from django.core.exceptions     import PermissionDenied
from django.db.utils            import IntegrityError
from django.http                import HttpResponse, HttpResponseRedirect, Http404

from main.models import User

import hashlib


_secret = (
    b"\xfe\xc9\xdd.=\x94\\R\x8fK\xcd#f\x03\xf5\xb4"
    b"\xb3|\xbah\xbd\xbeB\xb3\xb0\xde\xf8\xdb\xa2\xfdQJ"
    b"X\x05\nO(\xa6\x14\x90E\x05\xddV\xe7\xafB\xd5"
    b"\xe5\xef\xae\xf3\xd5\xe4%4s0\x8b\xf9cP\xceT"
)


def index(request):
    return HttpResponse()


def collect(request, user_id):
    try:
        token = request.POST["token"].encode("utf-8")
    except (KeyError, UnicodeEncodeError):
        raise PermissionDenied
    else:
        m = hashlib.sha512()
        m.update(token)
        if m.digest() != _secret:
            raise PermissionDenied

    try:
        login = request.POST["login"]
        email = request.POST["email"]
        username = request.POST["username"]
        passwd = request.POST["passwd"]
    except KeyError:
        raise Http404

    try:
        try:
            u = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            User.objects.create(
                django_user=DjangoUser.objects.create_user(login, email, passwd),
                user_id=user_id,
                username=username,
            )
        else:
            u.django_user.username = login
            u.django_user.email = email
            u.django_user.set_password(passwd)
            u.django_user.save()
            u.username = username
            u.save()
    except IntegrityError:
        raise Http404

    return HttpResponseRedirect("/")
