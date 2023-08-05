# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_autoshapes_api import CellsAutoshapesApi
import AuthUtil

class TestCellsAutoshapesApi(unittest.TestCase):
    """ CellsAutoshapesApi unit test stubs """

    def setUp(self):
        self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_autoshapes_api.CellsAutoshapesApi(self.api_client)

    def tearDown(self):
        pass

    def test_cells_autoshapes_get_worksheet_autoshape(self):
        """
        Test case for cells_autoshapes_get_worksheet_autoshape

        Get autoshape info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet2'
        autoshapeNumber = 4  
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_autoshapes_get_worksheet_autoshape(name, sheet_name,autoshapeNumber, folder=folder)
        pass

    def test_cells_autoshapes_get_worksheet_autoshapes(self):
        """
        Test case for cells_autoshapes_get_worksheet_autoshapes

        Get worksheet autoshapes info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet2'
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_autoshapes_get_worksheet_autoshapes(name, sheet_name, folder=folder)
        pass


if __name__ == '__main__':
    unittest.main()
