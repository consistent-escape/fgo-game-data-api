import pytest
from fastapi.testclient import TestClient

from app.main import app

from .utils import get_response_data


client = TestClient(app)


test_cases_dict = {
    "servant_NA_collectionNo": ("NA/servant/105", "NA_Billy"),
    "servant_NA_id": ("NA/servant/201000", "NA_Billy"),
    "servant_NA_lore": ("NA/servant/100?lore=True", "NA_Helena_lore"),
    "servant_JP_collectionNo": ("JP/servant/283", "JP_Elice"),
    "servant_JP_id": ("JP/servant/304300", "JP_Elice"),
    "servant_JP_collection_servant": ("JP/servant/149", "JP_Tiamat"),
    "servant_JP_costume": ("JP/servant/1", "JP_Mash"),
    "servant_JP_id_English": ("JP/servant/304300?lang=en", "JP_Elice_EN"),
    "servant_JP_multiple_NPs_space_istar": ("JP/servant/268", "JP_Space_Ishtar"),
    "servant_JP_string_svals_values": ("JP/servant/403400?lang=en", "JP_Bartholomew"),
    "servant_JP_datavals_subState_Value2": ("JP/servant/103800", "JP_Jason"),
    "equip_JP_collectionNo": ("JP/equip/683", "JP_Aerial_Drive"),
    "equip_JP_id": ("JP/equip/9402750", "JP_Aerial_Drive"),
    "svt_NA_id": ("NA/svt/9939120", "NA_svt_9939120"),
    "item_NA_id": ("NA/item/94000201", "NA_item_94000201"),
    "MC_NA_id": ("NA/MC/110", "NA_MC_LB"),
    "quest_NA_id_phase": ("NA/quest/94020187/1", "NA_87th_floor"),
}


test_cases = [pytest.param(*value, id=key) for key, value in test_cases_dict.items()]


@pytest.mark.parametrize("query,result", test_cases)
def test_nice(query: str, result: str):
    response = client.get(f"/nice/{query}")
    assert response.status_code == 200
    assert response.json() == get_response_data("test_data_nice", result)


cases_404_dict = {
    "servant": "500",
    "equip": "3001",
    "svt": "987626",
    # "skill": "25689",
    # "NP": "900205",
    # "function": "9000",
    # "buff": "765",
    "item": "941234",
    "MC": "62537",
    "quest": "1234567",
    "quest/94025012": "2",
}


cases_404 = [pytest.param(key, value, id=key) for key, value in cases_404_dict.items()]


@pytest.mark.parametrize("endpoint,item_id", cases_404)
def test_404_nice(endpoint: str, item_id: str):
    response = client.get(f"/nice/JP/{endpoint}/{item_id}")
    assert response.status_code == 404
    if endpoint == "quest":
        assert response.json()["detail"] == "Not Found"
    else:
        assert response.json()["detail"][-9:] == "not found"


class TestServantSpecial:
    def test_NA_not_integer(self):
        response = client.get("/nice/NA/servant/lkji")
        assert response.status_code == 422
