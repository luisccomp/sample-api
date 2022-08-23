from ..settings import Settings


BASE_RESOURCE = "/api"
BASE_V_RESOURCE = f"{BASE_RESOURCE}/{Settings.API_VERSION}"

USERS_RESOURCE = f"{BASE_V_RESOURCE}/users"
