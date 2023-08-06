from dianping.auth import Sign


class QueryShopReviewRequest(Sign):
    def __init__(self, app_key, app_secret, session, begintime, endtime, star, platform, offset, limit, app_shop_id=None, open_shop_uuid=None):
        """
        :param app_key:
        :param app_secret:
        :param session:
        :param begintime:
        :param endtime:
        :param star:
        :param platform:
        :param offset:
        :param limit:
        :param app_shop_id:
        :param open_shop_uuid:
        """
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/ugc/queryshopreview')
        self.set_sign_method('MD5')
        self.set_app_shop_id(app_shop_id)
        self.set_begintime(begintime)
        self.set_endtime(endtime)
        self.set_star(star)
        self.set_platform(platform)
        self.set_offset(offset)
        self.set_limit(limit)
        self.set_httpmethod('POST')
        self.set_open_shop_uuid(open_shop_uuid)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_begintime(self, begintime):
        self.add_query_param('begintime', begintime)

    def set_endtime(self, endtime):
        self.add_query_param('endtime', endtime)

    def set_star(self, star):
        self.add_query_param('star', star)

    def set_platform(self, platform):
        self.add_query_param('platform', platform)

    def set_offset(self, offset):
        self.add_query_param('offset', offset)

    def set_limit(self, limit):
        self.add_query_param('limit', limit)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)


class QueryStarRequest(Sign):
    def __init__(self, app_key, app_secret, session, platform, app_shop_id=None, open_shop_uuid=None):
        """
        :param app_key:
        :param app_secret:
        :param session:
        :param platform:
        :param app_shop_id:
        :param open_shop_uuid:
        """
        Sign.__init__(self)
        self.set_session(session)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_app_shop_id(app_shop_id)
        self.set_platform(platform)
        self.set_sign_method('MD5')
        self.set_url('https://openapi.dianping.com/router/ugc/querystar')
        self.set_httpmethod('POST')
        self.set_open_shop_uuid(open_shop_uuid)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_platform(self, platform):
        self.add_query_param('platform', platform)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)
