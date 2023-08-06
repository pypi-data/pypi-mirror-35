from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract.api_resource import APIResource


class SingletonAPIResource(APIResource):

    @classmethod
    def retrieve(cls, api_key=None, **params):
        return super(SingletonAPIResource, cls).retrieve(None,
                                                         api_key,
                                                         **params)

    @classmethod
    def class_url(cls):
        cls_name = cls.class_name()
        return "/v1/%s" % (cls_name,)

    def instance_url(self):
        return self.class_url()
