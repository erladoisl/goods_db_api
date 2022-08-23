import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from fireapp.serializer import to_representation
from .models import Good


class GoodsView(APIView):
    def get(self, request, *args, **kwargs):
        user_uid = request.GET.get('user_id', '')
        res = {}
        logging.info(f'Getting goods by user uid: {user_uid}')

        if len(user_uid) > 0:
            try:
                res = Good.objects.get(user_uid=user_uid)
            except:
                logging.info(f'Goods not found by user uid: {user_uid}')
                goods = []
        else:
            goods = Good.objects.all()

        res = to_representation(goods)

        return Response(data=res)

    def post(self, req, *args, **kwargs):
        return Response(data={'GoodsView post'})
