import requests

from api.base_url import BaseUrl


class BuilderGet(BaseUrl):
    def list_model(self):
        res = requests.get(self.base_url + '/wp-json/juzt-ask/v1/builder-models')
        status = res.status_code
        result = res.json()
        return status, result

    def list_size(self, model_type):
        params = {'type': model_type}
        res = requests.get(self.base_url + '/wp-json/juzt-ask/v1/builder-sizes', params=params)
        status = res.status_code
        result = res.json()
        return status, result

    def get_bag(self, model_type, size):
        params = {'type': model_type, 'size': size}
        res = requests.get(self.base_url + '/wp-json/juzt-ask/v1/builder-data', params=params)
        status = res.status_code
        result = res.json()
        return status, result


class BuilderPost(BaseUrl):
    def add_bag_to_cart(self, action, components_id, components):
        params = {'action': action, 'components_id': components_id, 'components': components}
        res = requests.post(self.base_url + '/wp/wp-admin/admin-ajax.php', params=params)
        status = res.status_code
        result = res.json()
        return status, result


