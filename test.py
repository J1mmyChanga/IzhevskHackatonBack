from api.api import ApiWrapper
from api.entity import Route

URL = "https://backend.cube-hackaton.ru"
API_WRAPPER = ApiWrapper(URL)

route = Route.create("2a", "b123")
print(API_WRAPPER.user.get("39808f4b-67b5-49f8-b7ac-774b6573298b", Route))
