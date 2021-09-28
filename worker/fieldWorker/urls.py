from django.urls import path
from fieldWorker import views
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from fieldWorker.schema import schema
urlpatterns = [
    path('fieldWorker/',views.FieldWorkerList.as_view(),name='field_worker_list'),
    path('fieldWorker/<int:pk>',views.FieldWorkerDetail.as_view(),name='field_worker_detail_api'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

urlpatterns = format_suffix_patterns(urlpatterns)