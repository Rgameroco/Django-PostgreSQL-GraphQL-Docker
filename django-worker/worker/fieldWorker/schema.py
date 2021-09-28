import graphene
from graphene_django import DjangoObjectType

from fieldWorker.models import FieldWorker

class FieldWorkerType(DjangoObjectType):
    class Meta:
        model = FieldWorker
        fields = ("id","first_name","last_name","function","created_at")

class Query(graphene.ObjectType):
    category_by_pk = graphene.Field(FieldWorkerType, id=graphene.String())
    all_fieldWorker= graphene.List(FieldWorkerType)
    def resolve_all_fieldWorker(root, info,):
        return FieldWorker.objects.all()
    def resolve_category_by_pk(root, info, pk):
        try:
            return FieldWorker.objects.get(pk=pk)
        except FieldWorker.DoesNotExist:
            return None
    
    
schema = graphene.Schema(query=Query)