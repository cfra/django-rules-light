import django
from django.conf.urls import include, url
from django.views import generic
from django.contrib.auth.models import User

import rules_light
# not need in this particular project ... oh well it'll serve as example
rules_light.autodiscover()
# import our project specific rules
import auth_rules
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^rules/', include('rules_light.urls')),

    url(r'^$', generic.ListView.as_view(model=User,
        template_name='auth/user_list.html' if django.VERSION < (1, 7)
        else 'auth/new_user_list.html'), name='auth_user_list'),
    url(r'user/(?P<username>[\w_-]+)/$',
        rules_light.class_decorator(generic.DetailView).as_view(
            slug_field='username', slug_url_kwarg='username', model=User),
        name='auth_user_detail'),
    url(r'user/(?P<username>[\w_-]+)/update/$',
        rules_light.class_decorator(generic.UpdateView).as_view(
            slug_field='username', slug_url_kwarg='username', model=User),
        name='auth_user_update'),
]
