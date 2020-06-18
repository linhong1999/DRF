from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self,data_status=0 ,data_msg='ok',http_status=None,headers=None,exception=False):

        data = {
            'status': data_status,
            'msg': data_msg
        }

        super().__init__(data=data,status=http_status,headers=headers,exception=exception)