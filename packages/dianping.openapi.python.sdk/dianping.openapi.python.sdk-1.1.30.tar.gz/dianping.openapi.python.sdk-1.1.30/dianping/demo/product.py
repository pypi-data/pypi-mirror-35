from dianping.request.product import ShopProductsGetRequest
from dianping.client import Client


def shopproductsgettest():
    request = ShopProductsGetRequest('7e87e96a41771f1d', '221bfe889349161a14add89772d82ca01454ef11',
                                     '6be73c00c1afb2d71e995ee90bc2372071dfd5b1', '194984aab9bea9eaac79fcf9e4378af4',
                                     1, 100)
    client = Client(request)
    response = client.invoke()
    print(response)
    assert (response is not None)


if __name__ == '__main__':
    shopproductsgettest()