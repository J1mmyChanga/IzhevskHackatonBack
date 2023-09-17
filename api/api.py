import requests
from typing import Type, List

from .entity import *


class AbstractApi:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.session = requests.Session()


class UserApi(AbstractApi):
    def create(self, api_entity: ApiEntity):
        self.session.post(
            f"{self.api_url}/user/{api_entity.__class__.__name__.lower()}s/create",
            json=api_entity.as_json()
        )

    def get_all(self, entity_type: Type[ApiEntity], **kwargs) -> List[AbstractApiEntity]:
        return list(map(
            lambda x: entity_type.from_json(x),
            self.session.post(
                f"{self.api_url}/user/{entity_type.__name__.lower()}s/get/all",
                json=kwargs
            ).json()
        ))

    def get(self, entity_id: str, entity_type: Type[ApiEntity]) -> AbstractApiEntity:
        return entity_type.from_json(self.session.post(
            f"{self.api_url}/user/{entity_type.__name__.lower()}s/get",
            json={"id": entity_id}
        ).json())


class AdminApi(AbstractApi):
    def update(self, api_entity: ApiEntity):
        self.session.post(
            f"{self.api_url}/admin/{api_entity.__class__.__name__.lower()}s/update",
            json=api_entity.as_json()
        )

    def delete(self, api_entity: ApiEntity):
        self.session.post(
            f"{self.api_url}/admin/{api_entity.__class__.__name__.lower()}s/update",
            json={"id": api_entity.id}
        )


class ApiWrapper:
    def __init__(self, url: str):
        self._admin = AdminApi(url)
        self._user = UserApi(url)

    @property
    def admin(self):
        return self._admin

    @property
    def user(self):
        return self._user
