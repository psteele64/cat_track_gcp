# app/tests/cats/test_serializers.py

from ctapi.serializers import CatSerializer


def test_valid_cat_serializer():
    valid_serializer_data = {
        "name": "TestKitty",
        "location": "GARAGE",
        "room_num": "1",
        "foster": 1
    }
    serializer = CatSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_cat_serializer():
    invalid_serializer_data = {
        "name": "TestKitty",
        "location": "GARAGE",
        "room_num": "1"
    }
    serializer = CatSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"foster": ["This field is required."]}