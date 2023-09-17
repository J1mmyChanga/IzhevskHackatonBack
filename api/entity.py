class AbstractApiEntity:
    pass


class ApiEntity(AbstractApiEntity):
    def as_json(self) -> dict: ...

    @staticmethod
    def from_json(json_entity: dict) -> AbstractApiEntity: ...

    @staticmethod
    def create(*args, **kwargs) -> AbstractApiEntity: ...


class Route(ApiEntity):
    def __init__(self, route_id: str, title: str, description: str, activated: bool, duration: int):
        self.id = route_id
        self.title = title
        self.description = description
        self.activated = activated
        self.duration = duration

    def as_json(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            'activated': self.activated,
            'duration': self.duration
        }

    @staticmethod
    def from_json(json_entity: dict):
        return Route(
            json_entity["id"],
            json_entity["title"],
            json_entity["description"],
            json_entity["activated"],
            json_entity["duration"]
        )

    @staticmethod
    def create(title: str, description: str, activated: bool, duration: int) -> AbstractApiEntity:
        return Route("", title, description, activated, duration)


class Spot(ApiEntity):
    def __init__(self, route_id: str, spot_id: str, title: str, description: str, lon: int, lat: int):
        self.id = spot_id
        self.route_id = route_id
        self.title = title
        self.description = description
        self.lon = lon
        self.lat = lat

    def as_json(self) -> dict:
        return {
            "route_id": self.route_id,
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "longtude": self.lon,
            "latitude": self.lat
        }

    @staticmethod
    def from_json(json_entity: dict) -> AbstractApiEntity:
        return Spot(
            json_entity["route_id"],
            json_entity["id"],
            json_entity["title"],
            json_entity["description"],
            json_entity["longtude"],
            json_entity["latitude"]
        )

    @staticmethod
    def create(route_id: str, title: str, description: str, lon: int, lat: int) -> AbstractApiEntity:
        return Spot(route_id, "", title, description, lon, lat)


class Photo(ApiEntity):
    def __init__(self, route_id: str, photo_id: str, name: str, data: str):
        self.id = photo_id
        self.route_id = route_id
        self.name = name
        self.data = data

    def as_json(self) -> dict:
        return {
            "route_id": self.route_id,
            "id": self.id,
            "data": self.data,
            "name": self.name
        }

    @staticmethod
    def from_json(json_entity: dict) -> AbstractApiEntity:
        return Photo(
            json_entity["route_id"],
            json_entity["id"],
            json_entity["name"],
            json_entity["data"]
        )

    @staticmethod
    def create(route_id: str, name: str, data: str) -> AbstractApiEntity:
        return Photo(route_id, "", name, data)
