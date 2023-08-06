# coding: utf-8
# 'ascii'
from dianping.client import Client
from dianping.request.poimaintain import POIMaintainQueryFlowStatusRequest
from dianping.request.poimaintain import PoiMaintainCreateRequest
from dianping.request.poimaintain import PoiMaintainUpdateRequest
from dianping.request.poimaintain import PoiSearchQuerybackcategoriesRequest


def poimaintainqueryflowsatustest():
    poimaintainqueryflowsatusrequest = POIMaintainQueryFlowStatusRequest('92ac75f6c6d2b9bf',
                                                                         '6132f8f4a0af2697bdd7c1acaa9739f9fc8b8d05',
                                                                         'b5f6f2ae6b6a773f41c717f75b575de1d2896e6c', 0,
                                                                         191748933)
    client = Client(poimaintainqueryflowsatusrequest)
    response = client.invoke()
    print(response)
    assert (response is not None)


if __name__ == '__main__':
    poiMaintainCreateRequest = PoiMaintainCreateRequest('100001', '1590f337484080dfa05e949f6b2c3c0357948876',
                                                        'ee45021744e2d32eab172a5b7b04ae793bc6e97d', '爱车',
                                                        '上海市长宁区安化路492号', '上海', '闵行区', '洗车')
    client = Client(poiMaintainCreateRequest)
    response = client.invoke()

if __name__ == '__main__':
    poiMaintainUpdate = PoiMaintainUpdateRequest('a6ba8d0779a195d7', '5e149b26a4766de52af096e02f62209474e3f32a',
                                                        'd85ebf0838266190e836a2596d02afd94a393513', '4721243',2)
    client = Client(poiMaintainUpdate)
    response = client.invoke()
if __name__ == '__main__':
    poiSearchQuerybackcategoriesRequest = PoiSearchQuerybackcategoriesRequest('e9ec573bcdd8d392', 'fab6db50ee7c460c2cf40ddbc317889a29ef15cf',
                                                        'afc2de476b4fdf7b0782bc3b6d92c44bb3633f74', '上海')
    client = Client(poiSearchQuerybackcategoriesRequest)
    response = client.invoke()
