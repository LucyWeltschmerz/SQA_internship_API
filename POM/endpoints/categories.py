from POM.base_api.base_api import BaseApi


class Categories(BaseApi):
    get_category_endpoint = "/api_testing/category/read.php"

    def get_categories(self, url, expected_status_code, expected_category):
        response = self.get_request(url)
        self.check_status_code(response, expected_status_code)
        expected_value = self.get_json_value_by_key(response,"$.records..name", expected_category)
        # print(expected_value)
        return expected_value
