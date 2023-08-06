from __future__ import absolute_import, division, print_function

from pingpp.api_resources.abstract import CreateableAppBasedAPIResource
from pingpp.api_resources.abstract import ListableAppBasedAPIResource


class BalanceTransfer(CreateableAppBasedAPIResource,
                      ListableAppBasedAPIResource):
    OBJECT_NAME = 'balance_transfer'

    @classmethod
    def class_name(cls):
        return 'balance_transfer'
