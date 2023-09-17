from api.api import ApiWrapper
from api.entity import Route

URL = "https://backend.cube-hackaton.ru"
API_WRAPPER = ApiWrapper(URL)

route = Route.create("2a", "b123")
print(API_WRAPPER.photo.get("f891e301-88bd-4d86-ae16-4c16924c21b8").data)
