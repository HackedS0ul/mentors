from django.urls import path
from core.views import home, SearchView, rate_user, auth_login

urlpatterns = [
    path('', home, name="home"),
    path('search/', SearchView.as_view(), name="search"),
    path('rate/<int:user_id>/', rate_user, name='rate_user'),
    path('prisijungimas/', auth_login, name="login"),
]

#<a href="{% url 'rate_user' user_id=user.id %}">Rate this user</a>
