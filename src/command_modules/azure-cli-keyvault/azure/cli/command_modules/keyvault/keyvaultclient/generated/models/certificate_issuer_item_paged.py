# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
#pylint: skip-file
from msrest.paging import Paged


class CertificateIssuerItemPaged(Paged):
    """
    A paging container for iterating over a list of CertificateIssuerItem object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CertificateIssuerItem]'}
    }

    def __init__(self, *args, **kwargs):

        super(CertificateIssuerItemPaged, self).__init__(*args, **kwargs)
