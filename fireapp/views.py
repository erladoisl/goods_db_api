import logging
import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Folder, Good, Link, Price
from .util import filter_objects, to_representation


class GoodsView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        error = False
        user_uid = request.GET.get('user_uid', '')
        logging.info(f'Getting goods by user uid: {type(user_uid)}')

        try:
            if len(user_uid) > 0:
                try:
                    goods = filter_objects(Good.objects.all(), {'user_uid': user_uid})
                except:
                    logging.info(f'Goods not found by user uid: {user_uid}')
                    goods = []
                    error = True
            else:
                goods = Good.objects.all()

            goods_json = to_representation(goods)
        except:
            logging.error(
                f'Error while getting goods\n{traceback.format_exc()}')
            goods_json = []
            error = True
        finally: 
            return Response(data={'error': error,
                                  'data': goods_json})


class LinksView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        error = False

        try:
            links = to_representation(Link.objects.all())
        except:
            logging.error(
                f'Error while getting links\n{traceback.format_exc()}')
            links = []
            error = True
        finally: 
            return Response(data={'error': error,
                                  'data': links})


class PricesView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        error = False

        try:
            prices = to_representation(Price.objects.all())
        except:
            logging.error(
                f'Error while getting prices\n{traceback.format_exc()}')
            prices = []
            error = True
        finally: 
            return Response(data={'error': error,
                                  'data': prices})

class FoldersView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        error = False

        try:
            prices = to_representation(Folder.objects.all())
        except:
            logging.error(
                f'Error while getting folders\n{traceback.format_exc()}')
            prices = []
            error = True
        finally: 
            return Response(data={'error': error,
                                  'data': prices})