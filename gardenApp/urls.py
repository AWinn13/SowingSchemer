from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("login/user", views.loginUser, name="loginUser"),
    path("login/create", views.register, name="register"),
    path("gardenjournal", views.gardenjournal, name="gardenjournal"),
    path("gardenjournal/create", views.createjournal, name="journal"), 
    path("seedlingjournal", views.seedlingjournal, name="seedlingjournal"),
    
    ]
urlpatterns += staticfiles_urlpatterns()

# ! EXAMPLE
# urlpatterns = [
#         path('bears', views.one_method),                        # would only match localhost:8000/bears
#         path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
#         path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
#     	path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
# ]
