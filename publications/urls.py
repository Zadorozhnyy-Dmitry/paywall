from django.urls import path

from publications.apps import PublicationsConfig
from publications.views import PublicationListView, PublicationDetailView, PublicationCreateView, PublicationUpdateView, \
    PublicationDeleteView, AddRemoveLike

app_name = PublicationsConfig.name

urlpatterns = [
    path('', PublicationListView.as_view(), name='publication_list'),  # список публикаций
    path('view/<int:pk>/', PublicationDetailView.as_view(), name='publication_view'),  # просмотр одной публикации
    path("create/", PublicationCreateView.as_view(), name="publication_create"),  # создание публикации
    path("update/<int:pk>/", PublicationUpdateView.as_view(), name="publication_update", ),  # редактирование публикации
    path("delete/<int:pk>/", PublicationDeleteView.as_view(), name="publication_delete", ),  # удаление публикации

    path('<int:pk>/like/', AddRemoveLike.as_view(), name='like')  # установить/удалить лайк

]
