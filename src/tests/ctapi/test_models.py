# app/tests/cats/test_models.py

import pytest

from ctapi.models import Cat


@pytest.mark.django_db
def test_cat_model():
    cat = Cat(name="TestKitty", location="GARAGE", room_num="1", foster=1)
    cat.save()
    assert cat.name== "TestKity"
    assert cat.location == "GARAGE"
    assert cat.room_num == "1"
    assert cat.foster == "1"
    assert str(cat) == cat.name