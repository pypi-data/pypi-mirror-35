from dianping.auth import Sign


class ShopProductsGetRequest(Sign):
    def __init__(self, app_key, app_secret, session, open_shop_uuid, page_no, limit):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_open_shop_uuid(open_shop_uuid)
        self.set_page_no(page_no)
        self.set_limit(limit)
        self.set_sign_method('MD5')
        self.set_url('https://openapi.dianping.com/router/product/shopproducts/get')
        self.set_httpmethod('GET')

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)

    def set_page_no(self, page_no):
        self.add_query_param('page_no', page_no)

    def set_limit(self, limit):
        self.add_query_param('limit', limit)
