from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    # path("",view=views.index,name="index"), fuctionnbased view
    path('',view=views.IndexClassView.as_view(),name='index'),# this is the class generic view
    path("item/",view=views.item,name="item"),
    path("<int:item_id>/",view=views.detail,name='detail'),
    path('add/',view=views.create_item,name='create_item'),
    path('update/<int:id>/',view=views.update_item,name='update_item'),
    path('delete/<int:id>/',view=views.delete_item,name='delete_item'),
]