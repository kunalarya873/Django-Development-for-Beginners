import pytest
from django.db import models
from inventory.models import Category

"""
## Table and Column Validation
"""

"""
- [ ] Confirm the presence of required table within the database schema.
"""


def test_model_structure_table_exists():
    try:
        from inventory.models import Category  # noqa F401
    except ImportError:
        assert False
    else:
        assert True


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""


@pytest.mark.parametrize(
    "model, field_name, expected_type",
    [
        (Category, "id", models.AutoField),
        (Category, "name", models.CharField),
        (Category, "slug", models.SlugField),
        (Category, "is_active", models.BooleanField),
        (Category, "level", models.IntegerField),
    ],
)
def test_model_structure_column_data_types(model, field_name, expected_type):
    assert hasattr(
        model, field_name
    ), f"{model.__name__} model does not have '{field_name} field"

    field = model._meta.get_field(field_name)

    assert isinstance(field, expected_type), f"Field is not type {expected_type}"


"""
- [ ] Confirm expected field count
"""


@pytest.mark.parametrize(
    "model, expected_field_count",
    [
        (
            Category,
            6,
        ),  # Replace with the expected number of fields in the SeasonalEvent model
    ],
)
def test_model_structure_field_count(model, expected_field_count):
    field_count = len(model._meta.fields)
    assert (
        field_count == expected_field_count
    ), f"{model.__name__} model has {field_count} fields, expected {expected_field_count}"


"""
- [ ] Ensure that column relationships are correctly defined.
"""


@pytest.mark.parametrize(
    "model, field_name, expected_type, related_model, on_delete_behavior, allow_null, allow_blank",
    [
        (Category, "parent", models.ForeignKey, Category, models.PROTECT, True, True),
    ],
)
def test_model_structure_relationship(
    model,
    field_name,
    expected_type,
    related_model,
    on_delete_behavior,
    allow_null,
    allow_blank,
):
    # Check if the field exists in the model
    assert hasattr(
        model, field_name
    ), f"{model.__name__} model does not have '{field_name} field"

    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if it's a ForeignKey
    assert isinstance(field, expected_type), f"Field is not type {expected_type}"

    # Check the related model
    assert (
        field.related_model == related_model
    ), f"'{field_name}' field does not relate to {related_model.__name__} model"

    # Check the on_delete behavior
    assert (
        field.remote_field.on_delete == on_delete_behavior
    ), f"'{field_name}' field does not have on_delete={on_delete_behavior}"

    # Check if the field allows null values
    assert (
        field.null == allow_null
    ), f"'{field_name}' field does not allow null values as expected"

    # Check if the field allows blank values
    assert (
        field.blank == allow_blank
    ), f"'{field_name}' field does not allow blank values as expected"


# """
# - [ ] Verify nullable or not nullable fields
# """


@pytest.mark.parametrize(
    "model, field_name, expected_nullable",
    [
        (Category, "id", False),
        (Category, "name", False),
        (Category, "slug", False),
        (Category, "is_active", False),
        (Category, "level", False),
    ],
)
def test_model_structure_nullable_constraints(model, field_name, expected_nullable):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the nullable constraint matches the expected value
    assert (
        field.null is expected_nullable
    ), f"Field '{field_name}' has unexpected nullable constraint"


# """
# - [ ] Verify the correctness of default values for relevant columns.
# """


@pytest.mark.parametrize(
    "model, field_name, expected_default_value",
    [
        (Category, "is_active", False),
        (Category, "level", 0),
    ],
)
def test_model_structure_default_values(model, field_name, expected_default_value):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the default value matches the expected value
    default_value = field.default

    assert default_value == expected_default_value


# """
# - [ ] Ensure that column lengths align with defined requirements.
# """


@pytest.mark.parametrize(
    "model, field_name, expected_length",
    [
        (Category, "name", 100),
        (Category, "slug", 120),
    ],
)
def test_model_structure_column_lengths(model, field_name, expected_length):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the max length matches the expected value
    assert (
        field.max_length == expected_length
    ), f"Field '{field_name}' has unexpected max length"


# """
# - [ ] Validate the enforcement of unique constraints for columns requiring unique values.
# """


@pytest.mark.parametrize(
    "model, field_name, is_unique",
    [
        (Category, "id", True),
        (Category, "name", False),
        (Category, "slug", True),
        (Category, "is_active", False),
        (Category, "level", False),
    ],
)
def test_model_structure_unique_fields(model, field_name, is_unique):
    # Get the field from the model
    field = model._meta.get_field(field_name)

    # Check if the max length matches the expected value
    assert field.unique == is_unique, f"Field '{field_name}' uniqueness mismatch"
