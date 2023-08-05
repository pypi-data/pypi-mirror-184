import json
from typing import Any, List


class ClientStorage:
    def __init__(self, page):
        self.__page = page

    def set(self, key: str, value: Any) -> bool:
        jv = self.__page._convert_attr_json(value)
        assert jv is not None
        return (
            self.__page.invoke_method(
                "clientStorage:set", {"key": key, "value": jv}, wait_for_result=True
            )
            == "true"
        )

    def get(self, key: str):
        jv = self.__page.invoke_method(
            "clientStorage:get", {"key": key}, wait_for_result=True
        )
        if jv:
            return json.loads(json.loads(jv))
        return None

    def contains_key(self, key: str) -> bool:
        return (
            self.__page.invoke_method(
                "clientStorage:containskey", {"key": key}, wait_for_result=True
            )
            == "true"
        )

    def remove(self, key: str) -> bool:
        return (
            self.__page.invoke_method(
                "clientStorage:remove", {"key": key}, wait_for_result=True
            )
            == "true"
        )

    def get_keys(self, key_prefix: str) -> List[str]:
        jr = self.__page.invoke_method(
            "clientStorage:getkeys", {"key_prefix": key_prefix}, wait_for_result=True
        )
        assert jr is not None
        return json.loads(jr)

    def clear(self) -> bool:
        return (
            self.__page.invoke_method("clientStorage:clear", wait_for_result=True)
            == "true"
        )
