from rest_framework import mixins
from rest_framework import generics
from fieldWorker.models import FieldWorker
from fieldWorker.serializers import FieldWorkerSerializer

class FieldWorkerList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class FieldWorkerDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
