from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import exception_handler as handler
from rest_framework.views import Response

def exception_handler(exc, context):

    response = handler(exc,context)

    if response is None:
        # print(exc)
        # print(context)
        #{'view': <CBVTest.CBV.Tester object at 0x0000016FDA5CF780>,
        # 'args': (), 'kwargs': {'pk': '3'},
        # 'request': <rest_framework.request.Request object at 0x0000016FDA605198>}

        print('%s - %s - %s ' % (context['view'], context['request'].method, exc))
        return Response({
            'detail': 'server error',

        },status=HTTP_500_INTERNAL_SERVER_ERROR,exception=True)
        # },status='200')

    return response