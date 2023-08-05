from strapi_api_client.resources.base import BaseResource


class GroupResource(BaseResource):
    def get_group(self, name: str):
        response = self._requestor.request(
            method='GET',
            endpoint_url=f"{self._api_url}/interest-categories?filters[name][$eqi]={name}",
            query={'filters[name][$eqi]': name}
        )
        return response

    def create_group(self, data: dict):
        response = self._requestor.request(
            method='POST',
            endpoint_url=f"{self._api_url}/interest-categories",
            payload={'data': data}
        )
        return response

    def delete_group(self, group_id: int):
        response = self._requestor.request(
            method='DELETE',
            endpoint_url=f"{self._api_url}/interest-categories/{group_id}"
        )
        return response
