from dianping.auth import Sign


class BookResultCallBackRequest(Sign):
    def __init__(self, app_key, app_secret, session, order_id, book_status, code, app_order_id=None, app_shop_id=None, open_shop_uuid=None):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/book/bookresultcallback')
        self.set_httpmethod('POST')
        self.set_order_id(order_id)
        self.set_book_status(book_status)
        self.set_app_shop_id(app_shop_id)
        self.set_code(code)
        self.set_app_order_id(app_order_id)
        self.set_open_shop_uuid(open_shop_uuid)

    def set_order_id(self, orderid):
        self.add_query_param('order_id', orderid)

    def set_book_status(self, book_status):
        self.add_query_param('book_status', book_status)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_app_order_id(self, app_order_id):
        self.add_query_param('app_order_id', app_order_id)

    def set_code(self, code):
        self.add_query_param('code', code)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)


class CancelBookCallBackRequest(Sign):
    def __init__(self, app_key, app_secret, session, order_id, code, cancel_result, app_shop_id=None, open_shop_uuid=None):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/book/cancelbookcallback')
        self.set_httpmethod('POST')
        self.set_order_id(order_id)
        self.set_app_shop_id(app_shop_id)
        self.set_code(code)
        self.set_cancel_result(cancel_result)
        self.set_open_shop_uuid(open_shop_uuid)

    def set_order_id(self, order_id):
        self.add_query_param('order_id', order_id)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_code(self, code):
        self.add_query_param('code', code)

    def set_cancel_result(self, cancel_result):
        self.add_query_param('cancel_result', cancel_result)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)


class IsvConsumeRequest(Sign):
    def __init__(self, app_key, app_secret, session, order_id, app_shop_id=None, open_shop_uuid=None):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/book/isvconsume')
        self.set_httpmethod('POST')
        self.set_order_id(order_id)
        self.set_app_shop_id(app_shop_id)
        self.set_open_shop_uuid(open_shop_uuid)

    def set_order_id(self, order_id):
        self.add_query_param('order_id', order_id)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)


class RefundAuditResultRequest(Sign):
    def __init__(self, app_key, app_secret, session, audit_result, order_id, app_shop_id=None, open_shop_uuid=None):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/book/refundauditresult')
        self.set_httpmethod('POST')
        self.set_order_id(order_id)
        self.set_app_shop_id(app_shop_id)
        self.set_audit_result(audit_result)
        self.set_open_shop_uuid(open_shop_uuid)

    def set_order_id(self, order_id):
        self.add_query_param('order_id', order_id)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_audit_result(self, audit_result):
        self.add_query_param('audit_result', audit_result)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)


class ToSynOrdersRequest(Sign):
    def __init__(self, app_key, app_secret, session, page_no, limit, app_shop_id=None, open_shop_uuid=None):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_url('https://openapi.dianping.com/router/book/query/tosynorders')
        self.set_httpmethod('POST')
        self.set_app_shop_id(app_shop_id)
        self.set_page_no(page_no)
        self.limit = limit
        self.set_open_shop_uuid(open_shop_uuid)

    def set_app_shop_id(self, app_shop_id):
        self.add_query_param('app_shop_id', app_shop_id)

    def set_page_no(self, page_no):
        self.add_query_param('page_no', page_no)

    def set_limit(self, limit):
        self.add_query_param('limit', limit)

    def set_open_shop_uuid(self, open_shop_uuid):
        self.add_query_param('open_shop_uuid', open_shop_uuid)

    class BookTimeModifyNotifyRequest(Sign):
        def __init__(self, app_key, app_secret, session, order_id, begintime, modify_result,
                     app_period_id, app_shop_id=None, app_order_id=None, code=None, period_name=None, open_shop_uuid=None):
            Sign.__init__(self)
            self.set_app_key(app_key)
            self.set_secret(app_secret)
            self.set_session(session)
            self.set_url('https://openapi.dianping.com/router/book/booktimemodifynotify')
            self.set_httpmethod('POST')
            self.set_app_shop_id(app_shop_id)
            self.set_order_id(order_id)
            self.set_begintime(begintime)
            self.set_modify_result(modify_result)

            self.set_app_period_id(app_period_id)
            self.set_code(code)
            self.set_app_period_name(period_name)
            self.set_app_order_id(app_order_id)
            self.set_open_shop_uuid(open_shop_uuid)

        def set_app_shop_id(self, app_shop_id):
            self.add_query_param('app_shop_id', app_shop_id)

        def set_order_id(self, order_id):
            self.add_query_param('order_id', order_id)

        def set_begintime(self, begintime):
            self.add_query_param('begintime', begintime)

        def set_modify_result(self, modify_result):
            self.add_query_param('modify_result', modify_result)

        def set_code(self, code):
            self.add_query_param('code', code)

        def set_app_period_id(self, app_period_id):
            self.add_query_param('code', app_period_id)

        def set_app_period_name(self, app_period_name):
            self.add_query_param('app_period_name', app_period_name)

        def set_open_shop_uuid(self, open_shop_uuid):
            self.add_query_param('open_shop_uuid', open_shop_uuid)

        def set_app_order_id(self, app_order_id):
            self.add_query_param('app_order_id', app_order_id)
