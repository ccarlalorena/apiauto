import requests
import pytest


class TestProjects:
    def setup_class(self):
        print("Setup class")
        # arrange of test
        self.token = "92ae392a6e782dd91578e76dfa1475585d3e2cfa"
        self.headers = {
            "Authorization": "Bearer {}".format(self.token)
        }
        self.url_base = "https://api.todoist.com/rest/v2/projects"

    @pytest.fixture
    def test_get_all_projects(self):
        """
        test for get all projects
        :return:
        """
        # act
        response = requests.get(self.url_base, headers=self.headers)
        print(response.json())
        list_projects = response.json()
        id_project = list_projects[1]["id"]
        # assert
        assert response.status_code == 200
        return id_project

    @pytest.mark.smoke
    @pytest.mark.create
    @pytest.mark.parametrize("name", ["CIProject2", "CIProject3", "CIProject4"])
    def test_create_project(self, name):
        """
        test to verify creation of project
        :return:
        """
        body_project = {
            "name": name
        }
        response = requests.post(self.url_base, headers=self.headers, data=body_project)
        print(response.json())
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_get_project(self, test_get_all_projects):

        url = self.url_base + "/" + test_get_all_projects
        response = requests.get(url, headers=self.headers)
        print(response.json())
        assert response.status_code == 200

    @pytest.mark.update
    def test_update_project(self, test_get_all_projects):
        url = self.url_base + "/" + test_get_all_projects
        data_update = {
            "name": "Project 2",
            "color": "red"
        }
        response = requests.post(url, headers=self.headers, data=data_update)
        print(response.json())
        assert response.status_code == 200

    @pytest.mark.smoke
    def test_delete_project(self, test_get_all_projects):
        url = self.url_base + "/" + test_get_all_projects
        response = requests.delete(url, headers=self.headers)
        # print(response.json())
        assert response.status_code == 204

    @classmethod
    def teardown_class(cls):
         print("teardown")
