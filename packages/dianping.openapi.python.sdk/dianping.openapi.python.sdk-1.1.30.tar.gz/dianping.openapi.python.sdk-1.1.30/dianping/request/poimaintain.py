from dianping.auth import Sign


class POIMaintainQueryFlowStatusRequest(Sign):
    def __init__(self, app_key, app_secret, session, type, flowid):
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_httpmethod('GET')
        self.set_url('https://openapi.dianping.com/router/poi/maintain/queryflowstatus')
        self.set_type(type)
        self.set_flowid(flowid)

    def set_type(self, type):
        self.add_query_param('type', type)

    def set_flowid(self, flowid):
        self.add_query_param('flowid', flowid)


class PoiSearchQuerybackcategoriesRequest(Sign):
    def __init__(self, app_key, app_secret, session):
        """
        :param app_key:
        :param app_secret:
        :param session:
        """
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_httpmethod('GET')
        self.set_url('https://openapi.dianping.com/router/poi/querybackcategories')

        self.set_session = session

    def set_session(self, session):
        self.add_query_param('session', session);


class PoiMaintainCreateRequest(Sign):
    def __init__(self, app_key, app_secret, session, shop_name, address, city_name, district_name, category,
                 branch_name, alt_name, crossroad, longitude, latitude, map_type, phone, power, business_hours,
                 public_transit, region, comment):
        """
        :param app_key:
        :param app_secret:
        :param session:
        :param shop_name:
        :param address:
        :param city_name:
        :param district_name:
        :param category:
        :param branch_name:
        :param alt_name:
        :param crossroad:
        :param longitude:
        :param latitude:
        :param map_type:
        :param phone:
        :param power:
        :param business_hours:
        :param public_transit:
        :param region:
        :param comment:
        """
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_httpmethod('POST')
        self.set_url('https://openapi.dianping.com/router/poi/maintain/createpoi')

        self.set_session = session
        self.set_shop_name = shop_name
        self.set_address = address
        self.set_city_name = city_name
        self.set_district_name = district_name
        self.set_category = category
        self.set_branch_name = branch_name
        self.set_alt_name = alt_name
        self.set_crossroad = crossroad
        self.set_longitude = longitude
        self.set_latitude = latitude
        self.set_map_type = map_type
        self.set_phone = phone
        self.set_power = power
        self.set_business_hours = business_hours
        self.set_public_transit = public_transit
        self.set_region = region
        self.set_comment = comment

    def set_session(self, session):
        self.add_query_param('session', session);

    def set_shop_name(self, shop_name):
        self.add_query_param('shop_name', shop_name);

    def set_address(self, address):
        self.add_query_param('address', address);

    def set_city_name(self, city_name):
        self.add_query_param('city_name', city_name);

    def set_district_name(self, district_name):
        self.add_query_param('district_name', district_name);

    def set_category(self, category):
        self.add_query_param('category', category);

    def set_branch_name(self, branch_name):
        self.add_query_param('branch_name', branch_name);

    def set_alt_name(self, alt_name):
        self.add_query_param('alt_name', alt_name);

    def set_crossroad(self, crossroad):
        self.add_query_param('crossroad', crossroad);

    def set_longitude(self, longitude):
        self.add_query_param('longitude', longitude);

    def set_latitude(self, latitude):
        self.add_query_param('latitude', latitude);

    def set_map_type(self, map_type):
        self.add_query_param('map_type', map_type);

    def set_phone(self, phone):
        self.add_query_param('phone', phone);

    def set_power(self, power):
        self.add_query_param('power', power);

    def set_business_hours(self, business_hours):
        self.add_query_param('business_hours', business_hours);

    def set_public_transit(self, public_transit):
        self.add_query_param('public_transit', public_transit);

    def set_region(self, region):
        self.add_query_param('region', region);

    def set_comment(self, comment):
        self.add_query_param('comment', comment);


class PoiMaintainUpdateRequest(Sign):
    def __init__(self, app_key, app_secret, session, shopid, feedtype, comment, shop_name, branch_name, alt_name,
                 address, crossroad, district_name, city_name, longitude, latitude, map_type, phone, power,
                 business_hours, public_transit, category, region, enrichment):
        """
        :param app_key:
        :param app_secret:
        :param session:
        :param shopid:
        :param feedtype:
        :param comment:
        :param shop_name:
        :param branch_name:
        :param alt_name:
        :param address:
        :param crossroad:
        :param district_name:
        :param city_name:
        :param longitude:
        :param latitude:
        :param map_type:
        :param phone:
        :param power:
        :param business_hours:
        :param public_transit:
        :param category:
        :param region:
        :param enrichment:
        """
        Sign.__init__(self)
        self.set_app_key(app_key)
        self.set_secret(app_secret)
        self.set_session(session)
        self.set_httpmethod('POST')
        self.set_url('https://openapi.dianping.com/router/poi/maintain/updatepoi')

        self.set_session = session
        self.set_shopid = shopid
        self.set_feedtype = feedtype
        self.set_comment = comment
        self.set_shop_name = shop_name
        self.set_branch_name = branch_name
        self.set_alt_name = alt_name
        self.set_address = address
        self.set_crossroad = crossroad
        self.set_district_name = district_name
        self.set_city_name = city_name
        self.set_longitude = longitude
        self.set_latitude = latitude
        self.set_map_type = map_type
        self.set_phone = phone
        self.set_power = power
        self.set_business_hours = business_hours
        self.set_public_transit = public_transit
        self.set_category = category
        self.set_region = region
        self.set_enrichment = enrichment

    def set_session(self, session):
        self.add_query_param('session', session);

    def set_shopid(self, shopid):
        self.add_query_param('shopid', shopid);

    def set_feedtype(self, feedtype):
        self.add_query_param('feedtype', feedtype);

    def set_comment(self, comment):
        self.add_query_param('comment', comment);

    def set_shop_name(self, shop_name):
        self.add_query_param('shop_name', shop_name);

    def set_branch_name(self, branch_name):
        self.add_query_param('branch_name', branch_name);

    def set_alt_name(self, alt_name):
        self.add_query_param('alt_name', alt_name);

    def set_address(self, address):
        self.add_query_param('address', address);

    def set_crossroad(self, crossroad):
        self.add_query_param('crossroad', crossroad);

    def set_district_name(self, district_name):
        self.add_query_param('district_name', district_name);

    def set_city_name(self, city_name):
        self.add_query_param('city_name', city_name);

    def set_longitude(self, longitude):
        self.add_query_param('longitude', longitude);

    def set_latitude(self, latitude):
        self.add_query_param('latitude', latitude);

    def set_map_type(self, map_type):
        self.add_query_param('map_type', map_type);

    def set_phone(self, phone):
        self.add_query_param('phone', phone);

    def set_power(self, power):
        self.add_query_param('power', power);

    def set_business_hours(self, business_hours):
        self.add_query_param('business_hours', business_hours);

    def set_public_transit(self, public_transit):
        self.add_query_param('public_transit', public_transit);

    def set_category(self, category):
        self.add_query_param('category', category);

    def set_region(self, region):
        self.add_query_param('region', region);

    def set_enrichment(self, enrichment):
        self.add_query_param('enrichment', enrichment);
