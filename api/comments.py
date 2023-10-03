import logging
import unittest

import requests

from api.todo_base import TodoBase
from config.config import HEADERS
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


class Comments(unittest.TestCase):
    """
    Setup Class comments
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup executed only one
        :return:
        """
        cls.url_comments = "https://api.todoist.com/rest/v2/comments"
        cls.session = requests.Session()

        cls.project_list = []
        cls.task_list = []

        # cls.task_id = TodoBase().get_all_tasks()["body"][1]["id"]
        # cls.comment_id = TodoBase().get_all_comments(cls.task_id)["body"][0]["id"]

    def test_get_all_comments(self):
        """
        Test to get all comments
        :return:
        """
        response_create_task = TodoBase().create_task(self)
        task_id = response_create_task["body"]["id"]
        self.task_list.append(task_id)
        response = self.create_comment(task_id=task_id, content="Test Comment 01")
        comment_id = response["body"]["id"]
        url_comment = f"{self.url_comments}/{comment_id}"
        response_get = RestClient().send_request("get", session=self.session, url=url_comment, headers=HEADERS)

    def test_create_comment_by_project(self):
        """
        Test to create comment
        :return:
        """
        project_created = TodoBase().create_project("Project Comments")
        project_id = project_created["body"]["id"]
        response = self.create_comment(project_id=project_id, content="Section Test")
        self.project_list.append(project_id)

        # assert response.status_code == 200

    def test_delete_comment(self):
        """
        Test for delete comment
        :return:
        """
        project_created = TodoBase().create_project("Project TestComment Delete")
        project_id = project_created["body"]["id"]
        self.project_list.append(project_id)
        response = self.create_comment(project_id=project_id, content="Test Adding Comment")
        assert response["status"] == 200
        comment_id = response["body"]["id"]
        url = f"{self.url_comments}/{comment_id}"
        response_get = RestClient().send_request("delete", session=self.session, url=url, headers=HEADERS)

    def test_update_comment(self):
        """
        Test for update comment
        :return:
        """
        project_created = TodoBase().create_project("Project TestComment")
        project_id = project_created["body"]["id"]
        response = self.create_comment(project_id=project_id, content="Test Adding Comment")
        assert response["status"] == 200
        comment_id = response["body"]["id"]
        response = self.update_comment(comment_id=comment_id, content="Test Adding Comment updated")
        self.project_list.append(project_id)

    def create_comment(self, project_id=None, task_id=None, content=None):
        """
        Method to create a comment
        :param project_id:
        :param task_id:
        :param content:
        :return:
        """
        data = {
            "content": content
        }
        if project_id:
            data["project_id"] = project_id
        if task_id:
            data["task_id"] = task_id

        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=self.url_comments, data=data)
        return response

    def update_comment(self, comment_id=None, content=None):
        """
        Method to update a comment
        :param self:
        :param comment_id:
        :param content:
        :return:
        """
        data = {
            "content": content
        }
        url_comment = f"{self.url_comments}/{comment_id}"
        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=self.url_comments, data=data)
        return response

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class")
        # delete projects created
        TodoBase().delete_projects(cls.project_list)
        TodoBase().delete_tasks(cls.task_list)
