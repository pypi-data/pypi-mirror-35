from dianping.client import Client
from dianping.request.merchantdata import Consumption
from dianping.request.merchantdata import DealGroupsConsumption
from dianping.request.merchantdata import Book


def consumprequesttest():
    consumprequest = Consumption(1000069, '6862bd6012020b0fd385652905db18d4c9eaa835',
                                 '24b4e5e0e94119930686399d02439415013ab013',
                                 'J000001', 30)

    client = Client(consumprequest)
    response = client.invoke()
    print(response)
    assert (response is not None)


def dealgroupquesttest():
    dealgroupquest = DealGroupsConsumption(1000069, '6862bd6012020b0fd385652905db18d4c9eaa835',
                                               '24b4e5e0e94119930686399d02439415013ab013',
                                               30)

    client = Client(dealgroupquest)
    response = client.invoke()
    print(response)
    assert (response is not None)


def booktest():
    bookquest = Book(1000069, '6862bd6012020b0fd385652905db18d4c9eaa835',
                              '24b4e5e0e94119930686399d02439415013ab013',
                              'J000001')

    client = Client(bookquest)
    response = client.invoke()
    print(response)
    assert (response is not None)


if __name__ == '__main__':
    consumprequesttest()
    dealgroupquesttest()
    booktest()
