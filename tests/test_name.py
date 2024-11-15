import pytest

from masterdata_checker.name import UserFailureException, name_checker

# @pytest.mark.parametrize(
#     'file_path, result',
#     [
#         ('whatever-filepath', ['whatever-result-we-expert', True]),
#         ('another-filepath', ['another-result-we-expert', False]),
#     ]
# )
# def test_name_checker(filepath: str, result: list[str, bool]):


def test_valid_file_name():
    file_path = 'data/object_type_CHEMICAL_v1_S.3_creator.xlsx'
    expected_output = ['File name: OK!', True]
    assert name_checker(file_path) == expected_output


def test_invalid_file_type():
    file_path = 'data/object_type_CHEMICAL_v1_S.3_creator.txt'
    with pytest.raises(UserFailureException, match='Error: Invalid file type'):
        name_checker(file_path)


def test_missing_fields():
    file_path = 'data/invalid_name.xls'
    expected_error = (
        'Invalid name format. The name should contain different fields separated by underscores (_). '
        'Consult the wiki to see which ones.'
    )
    result = name_checker(file_path)
    assert result[1] is False
    assert expected_error in result[0]


def test_invalid_entity_type():
    file_path = 'data/notype_CHEMICAL_v1_S.3_creator.xlsx'
    result = name_checker(file_path)
    assert result[1] is False
    assert 'Invalid entity type at position 1.' in result[0]


def test_invalid_entity_name():
    file_path = 'data/object_type_@name_v1_S.3_creator.xlsx'
    result = name_checker(file_path)
    assert result[1] is False
    assert 'Invalid entity name at position 2.' in result[0]


def test_invalid_version():
    file_path = 'data/object_type_CHEMICAL_version1_S.3_creator.xlsx'
    result = name_checker(file_path)
    assert result[1] is False
    assert 'Invalid version at position 3.' in result[0]


def test_invalid_division():
    file_path = 'data/object_type_CHEMICAL_v1_VP!1_creator.xlsx'
    result = name_checker(file_path)
    assert result[1] is False
    assert 'Invalid division at position 4.' in result[0]


def test_invalid_contact_person():
    file_path = 'data/object_type_CHEMICAL_v1_S.3_@creator.xlsx'
    result = name_checker(file_path)
    assert result[1] is False
    assert 'Invalid contact person at position 5.' in result[0]
