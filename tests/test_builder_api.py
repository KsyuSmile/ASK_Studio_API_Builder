import pytest


"""Получение списка моделей сумок"""
def test_get_list_model(builder_get):
    status, result = builder_get.list_model()
    print(result)
    assert status == 200


"""Получение списка размеров сумок, корректные данные"""
@pytest.mark.parametrize("model_type", ['leather', 'osnova-s-pinami', 'plastic', 'plastic_and_leather', 'steganaya-tkan'])
def test_get_list_size(builder_get, model_type):
    status, result = builder_get.list_size(model_type)
    print(result['items'])
    assert 'items' in result
    assert status == 200


"""Получение списка размеров сумок, некорректные данные"""
@pytest.mark.parametrize("model_type", ['', '123', 'Gjdks', 123654, '_-/?%*'])
def test_get_list_size_invalid_type(builder_get, model_type):
    status, result = builder_get.list_size(model_type)
    assert status == 404
    print(status)


"""Получение сумки, позитивные тесты с корректными данными"""
def test_get_get_leather_maxi(builder_get, model_type='leather', size='maxi'):
    """Кожаная основа, размер maxi"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_leather_medium(builder_get, model_type='leather', size='medium'):
    """Кожаная основа, размер medium"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_leather_mini(builder_get, model_type='leather', size='mini'):
    """Кожаная основа, размер mini"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_s_pinami_maxi(builder_get, model_type='osnova-s-pinami', size='maxi'):
    """Основа с пинами, размер maxi"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_s_pinami_medium(builder_get, model_type='osnova-s-pinami', size='medium'):
    """Основа с пинами, размер medium"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_s_pinami_mini(builder_get, model_type='osnova-s-pinami', size='mini'):
    """Основа с пинами, размер mini"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_plastic_maxi(builder_get, model_type='plastic', size='maxi'):
    """Прозрачная основа, размер maxi"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_plastic_medium(builder_get, model_type='plastic', size='medium'):
    """Прозрачная основа, размер medium"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_plastic_mini(builder_get, model_type='plastic', size='mini'):
    """Прозрачная основа, размер mini"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_mix_maxi(builder_get, model_type='plastic_and_leather', size='maxi'):
    """Mix основа, размер maxi"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_mix_medium(builder_get, model_type='plastic_and_leather', size='medium'):
    """Mix основа, размер medium"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


def test_get_get_puffed_maxi(builder_get, model_type='steganaya-tkan', size='maxi'):
    """Puffed основа, размер maxi"""
    status, result = builder_get.get_bag(model_type, size)
    assert 'sections' in result
    assert 'parameters' in result
    assert 'accessories' in result
    assert status == 200


"""Получение сумки, негативные тесты с некорректными данными"""
@pytest.mark.parametrize("size", ['', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_leather_invalid_size(builder_get, size, model_type='leather'):
    """Кожаная основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status == 404


@pytest.mark.parametrize("size", ['', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_plastic_invalid_size(builder_get, size, model_type='plastic'):
    """Прозрачная основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status != 200


@pytest.mark.parametrize("size", ['', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_s_pinami_invalid_size(builder_get, size, model_type='osnova-s-pinami'):
    """Основа с пинами, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status != 200


@pytest.mark.parametrize("size", ['', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_mix_invalid_size(builder_get, size, model_type='plastic_and_leather'):
    """Mix основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status != 200


@pytest.mark.parametrize("size", ['', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_puffed_invalid_size(builder_get, size, model_type='steganaya-tkan'):
    """Puffed основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status != 200



