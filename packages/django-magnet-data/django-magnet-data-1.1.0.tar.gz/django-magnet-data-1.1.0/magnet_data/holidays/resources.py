#!/usr/bin/python
# coding=utf-8
# vim: set fileencoding=utf-8 :
"""
This document defines the holidays resources
"""
# standard library
import datetime

# django
from django.conf.urls import url

# others libraries
# tastypie
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.utils import trailing_slash

# decorators
from api.decorators import api_method

# api
from api.resources import MultipartResource
from api.serializers import Serializer

# models
from holidays.models import Holiday

# resources


class HolidayResource(MultipartResource):
    def prepend_urls(self):
        """
        Add the following array of urls to the HolidayResource base urls
        """
        base_url = "^(?P<resource_name>{})/".format(self._meta.resource_name)

        return [
            # value for year
            url(
                r"%s(?P<year>\d{4})%s$" % (base_url, trailing_slash()),
                self.wrap_view("value_on_year"),
                name="api_{}_value_on_year".format(self._meta.resource_name),
            ),
            # value for month
            url(
                r"%s(?P<year>\d{4})/(?P<month>\d{2})%s$" % (base_url, trailing_slash()),
                self.wrap_view("value_on_month"),
                name="api_{}_value_on_month".format(self._meta.resource_name),
            ),
            # value for date
            url(
                r"%s(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})%s$"
                % (base_url, trailing_slash()),
                self.wrap_view("value_on_date"),
                name="api_{}_value_on_date".format(self._meta.resource_name),
            ),
        ]

    @api_method(single=False, expected_methods=["get"])
    def value_on_year(self, request, year, **kwargs):
        return Holiday.objects.filter(date__year=int(year))

    @api_method(single=False, expected_methods=["get"])
    def value_on_month(self, request, year, month, **kwargs):
        return Holiday.objects.filter(date__year=int(year), date__month=int(month))

    @api_method(single=False, expected_methods=["get"])
    def value_on_date(self, request, year, month, day, **kwargs):
        date = datetime.datetime(int(year), int(month), int(day))
        return Holiday.objects.filter(date=date)


class HolidayResource(HolidayResource):
    class Meta:
        allowed_methods = ["get"]
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        queryset = Holiday.objects.all()
        resource_name = "cl"
        serializer = Serializer()

        fields = [
            "date",
            "name",
        ]
