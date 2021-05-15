from django.urls import path
from . import views

urlpatterns = [
    path('',views.page1,name="page1"),
    path('page2',views.page2,name="page2"),
    path('page3',views.page3,name="page3"),
    path('page4',views.page4,name="page4"),
    path('estanteria1',views.estanteria1,name="estanteria1"),
    path('estanteria2',views.estanteria2,name="estanteria2"),
    path('estanteria3',views.estanteria3,name="estanteria3"),
    path('estanteria4',views.estanteria4,name="estanteria4"),
    path('oficina1',views.oficina1,name="oficina1"),
    path('oficina2',views.oficina2,name="oficina2"),
    path('oficina3',views.oficina3,name="oficina3"),
    path('oficina4',views.oficina4,name="oficina4"),
]
