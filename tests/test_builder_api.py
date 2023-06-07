import pytest
import json


"""Получение списка моделей сумок"""
def test_get_list_model(builder_get):
    status, result = builder_get.list_model()
    print(status)
    for body_res in result:
        print(body_res)
    assert 'BuilderSize' in result # не проходит
    assert status == 200


"""Получение списка размеров сумок, корректные данные"""
@pytest.mark.parametrize("model_type", ['leather', 'osnova-s-pinami', 'plastic', 'plastic_and_leather', 'steganaya-tkan'])
def test_get_list_size(builder_get, model_type):
    status, result = builder_get.list_size(model_type)
    assert 'items' in result
    assert status == 200
    for body_res in result:
        print(body_res)
    for list_size in result['items']:
        print(list_size)


"""Получение списка размеров сумок, некорректные данные"""
@pytest.mark.parametrize("model_type", ['', 'лжрыАЫРииыооОЫ', '123', 'Gjdks', 123654, '_-/?%*'])
def test_get_list_size_invalid_type(builder_get, model_type):
    status, result = builder_get.list_size(model_type)
    assert status == 400
    print(status)
    # Тест не пройден


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
@pytest.mark.parametrize("size", ['', 'ФнвОЫУисллпП', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_leather_invalid_size(builder_get, size, model_type='leather'):
    """Кожаная основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status == 400
    # Тест не пройден


@pytest.mark.parametrize("size", ['', 'ФнвОЫУисллпП', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_plastic_invalid_size(builder_get, size, model_type='plastic'):
    """Прозрачная основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status == 400
    # Тест не пройден


@pytest.mark.parametrize("size", ['', 'ФнвОЫУисллпП', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_s_pinami_invalid_size(builder_get, size, model_type='osnova-s-pinami'):
    """Основа с пинами, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status == 400
    # Тест не пройден


@pytest.mark.parametrize("size", ['', 'ФнвОЫУисллпП', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_mix_invalid_size(builder_get, size, model_type='plastic_and_leather'):
    """Mix основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status == 400
    # Тест не пройден


@pytest.mark.parametrize("size", ['', 'ФнвОЫУисллпП', '649786', 'ipRthOjh', 123654, '?,@%(*'])
def test_get_get_puffed_invalid_size(builder_get, size, model_type='steganaya-tkan'):
    """Puffed основа, некорректный размер"""
    status, result = builder_get.get_bag(model_type, size)
    print(result)
    assert 'error' in result
    assert status == 400
    # Тест не пройден


"""Добавление сумки в корзину с корректными данными"""
def test_get_add_bag_to_cart(builder_post, action='builder_add_to_cart', components_id='["5283","17653","4353"]', components='{"sections":{"osnova":{"pa_base_logo":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/logo-png-mask-1.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/07/maxi-logo-plastic-2.svg","positionX":0,"positionY":572,"zIndex":101,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/pink-logo-maxi.png"}},"meshok":{"pa_bag_color":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/06/transparent-base-maxi-bag-1.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/06/transparent-base-maxi-bag-1.svg?v=1685771965","positionX":0,"positionY":517,"zIndex":1,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2023/04/p1.jpg"}},"remen":{"pa_bagstrap_color":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/transparent-base-maxi-bagstrap-lanyard.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/07/transparent-base-maxi-bagstrap-lanyard.svg?v=1685771965","positionX":0,"positionY":42,"zIndex":1,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2022/06/bagstrap-lanyard-black-500h500.jpg"}}},"accessories":{},"parameters":{"width":600,"height":1183}}'):
    status, result = builder_post.add_bag_to_cart(action, components_id, components)
    assert 'cart_hash' in result
    assert 'fragments' in result
    assert status == 200


"""Добавление сумки в корзину с некорректными данными"""
@pytest.mark.parametrize("action", ['', 'проыЬлЗЦоор', '6548116846', 'tYpoqFhKjah', 97613245654, '?,@%(*'])
def test_get_add_bag_to_cart_invalid_action(builder_post, action, components_id='["5283","17653","4353"]', components='{"sections":{"osnova":{"pa_base_logo":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/logo-png-mask-1.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/07/maxi-logo-plastic-2.svg","positionX":0,"positionY":572,"zIndex":101,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/pink-logo-maxi.png"}},"meshok":{"pa_bag_color":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/06/transparent-base-maxi-bag-1.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/06/transparent-base-maxi-bag-1.svg?v=1685771965","positionX":0,"positionY":517,"zIndex":1,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2023/04/p1.jpg"}},"remen":{"pa_bagstrap_color":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/transparent-base-maxi-bagstrap-lanyard.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/07/transparent-base-maxi-bagstrap-lanyard.svg?v=1685771965","positionX":0,"positionY":42,"zIndex":1,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2022/06/bagstrap-lanyard-black-500h500.jpg"}}},"accessories":{},"parameters":{"width":600,"height":1183}}'):
    """Некорректный action"""
    status, result = builder_post.add_bag_to_cart(action, components_id, components)
    assert status == 400


@pytest.mark.parametrize("components_id", ['', 'проыЬлЗЦоор', '6548116846', 'tYpoqFhKjah', 97613245654, '?,@%(*'])
def test_get_add_bag_to_cart_invalid_components_id(builder_post, components_id, action='builder_add_to_cart', components='{"sections":{"osnova":{"pa_base_logo":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/logo-png-mask-1.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/07/maxi-logo-plastic-2.svg","positionX":0,"positionY":572,"zIndex":101,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/pink-logo-maxi.png"}},"meshok":{"pa_bag_color":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/06/transparent-base-maxi-bag-1.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/06/transparent-base-maxi-bag-1.svg?v=1685771965","positionX":0,"positionY":517,"zIndex":1,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2023/04/p1.jpg"}},"remen":{"pa_bagstrap_color":{"png":"https://askstudio.staging.juzt.studio/app/uploads/2022/07/transparent-base-maxi-bagstrap-lanyard.png","svg":"https://askstudio.staging.juzt.studio/wp-json/juzt-ask/v1/builder-image?url=https://askstudio.staging.juzt.studio/app/uploads/2022/07/transparent-base-maxi-bagstrap-lanyard.svg?v=1685771965","positionX":0,"positionY":42,"zIndex":1,"backgroundFull":"https://askstudio.staging.juzt.studio/app/uploads/2022/06/bagstrap-lanyard-black-500h500.jpg"}}},"accessories":{},"parameters":{"width":600,"height":1183}}'):
    """Некорректный components_id"""
    status, result = builder_post.add_bag_to_cart(action, components_id, components)
    print(result)
    assert status == 400
    # Тест не пройден


@pytest.mark.parametrize("components", ['', 'проыЬлЗЦоор', '6548116846', 'tYpoqFhKjah', 97613245654, '?,@%(*'])
def test_get_add_bag_to_cart_invalid_components_id(builder_post, components, action='builder_add_to_cart', components_id='["5283","17653","4353"]'):
    """Некорректный components"""
    status, result = builder_post.add_bag_to_cart(action, components_id, components)
    print(result)
    assert status == 400
    # Тест не пройден