import logging
import unittest

import requests

from api.todo_base import TodoBase
from config.config import HEADERS
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


class Sections(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url_section = "https://api.todoist.com/rest/v2/sections"
        cls.session = requests.Session()

        cls.project_id = TodoBase().get_all_projects()["body"][1]["id"]

    def test_create_session(self):
        """
        Test to create session
        :return:
        """
        data = {
            "project_id": self.project_id,
            "name": "Section 2"
        }
        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=self.url_section, data=data)
        #assert response.status_code == 200

    def test_get_all_sections(self):

        response = TodoBase().get_all_sections()
        LOGGER.info("Number of sections returned: %s", len(response["body"]))
        #assert response.status_code == 200

    def test_get_all_sections_by_project(self):
        if self.project_id:
            url_section = f"{self.url_section}?project_id={self.project_id}"

        response = RestClient().send_request("get", session=self.session, headers=HEADERS,
                                             url=url_section)
        LOGGER.info("Number of sections returned: %s", len(response["body"]))
        #assert response.status_code == 200

    def test_get_section(self):
        response = TodoBase().get_all_sections()
        response_body = response["body"]
        section_id = response_body[1]["id"]
        LOGGER.info("Section Id: %s", section_id)
        url_section = f"{self.url_section}/{section_id}"
        response = RestClient().send_request("get", session=self.session, headers=HEADERS,
                                             url=url_section)
        response = response["body"]
        #assert response.status_code == 200

    def test_delete_section(self):
        """
        Test delete section
        :return:
        """
        response = TodoBase().get_all_sections()
        response_body = response["body"]
        section_id = response_body[1]["id"]
        LOGGER.info("Section Id: %s", section_id)
        url_section = f"{self.url_section}/{section_id}"
        response = RestClient().send_request("delete", session=self.session, headers=HEADERS,
                                             url=url_section)
        response = response["body"]
        #assert response.status_code == 204

    def test_update_section(self):
        """
        Test update section
        :return:
        """
        project_created = TodoBase().create_project("Project for section")
        project_id = project_created["body"]["id"]
        section_id_list = TodoBase().create_sections(["section test"], project_id)
        data = {
            "project_id": project_id,
            "order": 2,
            "name": "section test updated"
        }


        #LOGGER.info("Section Id: %s", section_id)
        response = TodoBase().get_all_sections()
        response_body = response["body"]
        section_id = response_body[1]["id"]
        url_section = f"{self.url_section}/{section_id}"
        data_section_update = {
            "project_id": self.project_id,
            "name": "SectionUpdated"
        }
        #self.section_list.append(section_id)
        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=url_section, data=data_section_update)
        #assert response.status_code == 200

