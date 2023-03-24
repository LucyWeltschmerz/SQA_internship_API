
from POM.endpoints.categories import Categories


def test_category(app_config):
    category = Categories()
    category.get_categories(app_config.base_url + category.get_category_endpoint, 200, "Supplements")
