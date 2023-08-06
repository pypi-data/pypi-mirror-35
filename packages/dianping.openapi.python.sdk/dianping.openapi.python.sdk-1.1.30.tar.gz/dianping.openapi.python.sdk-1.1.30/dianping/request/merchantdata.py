from dianping.auth import Sign


class Consumption(Sign):
    def __init__(self, app_key, app_secret, session, date_type, app_shop_id=None, open_shop_uuid=None):
        """
        :param app_key:
        :param app_secret:
        :param session:
        :param date_type:
        :param app_shop_id:
        :param open_shop_uuid:
        """
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/merchant/data/consumption')
        self.set_httpmethod('POST')
        self.set_app_shop_id(app_shop_id)
        self.set_date_type(date_type)
        self.set_open_shop_uuid(open_shop_uuid)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_date_type(self, date_type):
        self.add_query_param('date_type', date_type)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)


class DealGroupsConsumption(Sign):
    def __init__(self, app_key, app_secret, session, date_type, app_shop_id=None, open_shop_uuid=None):
        """
        :param app_key:
        :param app_secret:
        :param session:
        :param date_type:
        :param app_shop_id:
        :param open_shop_uuid:
        """
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/merchant/data/dealgroups')
        self.set_httpmethod('POST')
        self.set_app_shop_id(app_shop_id)
        self.set_date_type(date_type)
        self.set_open_shop_uuid(open_shop_uuid)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_date_type(self, date_type):
        self.add_query_param('date_type', date_type)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)


class Book(Sign):
    def __init__(self, app_key, app_secret, session, date_type, app_shop_id=None, open_shop_uuid=None):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/merchant/data/book')
        self.set_httpmethod('POST')

        self.set_app_shop_id(app_shop_id)
        self.set_date_type(date_type)
        self.set_open_shop_uuid(open_shop_uuid)


    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_date_type(self, date_type):
        self.add_query_param('date_type', date_type)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)

