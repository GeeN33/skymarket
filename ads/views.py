from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated


from ads.models import Ad,Comment
from ads.permissions import CreatePermission, UpdateDeletePermission
from ads.serializers import AdListSerializers, AdCreateSerializers, AdDetaiSerializers, AdDestroySerializers, \
    AdUpdateSerializers, CommentCreateSerializers,CommenListtSerializers,CommenUpdateSerializers,CommentDestroySerializers


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializers
    permission_classes = [IsAuthenticated, CreatePermission]

class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializers
    def get(self, request, *args, **kwargs):

        text = request.GET.get('text', None)
        if text:
            self.queryset = self.queryset.filter(
                title__contains=text
            )
        else:
            self.queryset = self.queryset.order_by('-created_at')

        return super().get(self, request, *args, **kwargs)

class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetaiSerializers
    permission_classes = [IsAuthenticated, UpdateDeletePermission]

class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializers
    permission_classes = [IsAuthenticated, UpdateDeletePermission]

class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializers
    permission_classes = [IsAuthenticated, UpdateDeletePermission]


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializers
    permission_classes = [IsAuthenticated, CreatePermission]

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommenListtSerializers


class CommentUpdateView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommenUpdateSerializers
    permission_classes = [IsAuthenticated, UpdateDeletePermission]


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializers
    permission_classes = [IsAuthenticated, UpdateDeletePermission]




