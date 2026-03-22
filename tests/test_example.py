import pytest
import allure

@allure.feature("Примеры тестов")
@allure.story("Провальные тесты")
def test_fail1():
    assert False

@allure.story("Провальные тесты")
def test_fail2():
    assert False

@allure.story("Провальные тесты")
def test_fail3():
    assert False

@allure.story("Провальные тесты")
def test_fail4():
    assert False

@allure.story("Провальные тесты")
def test_fail5():
    assert False

@allure.story("Провальные тесты")
def test_fail6():
    assert False

@allure.story("Провальные тесты")
def test_fail7():
    assert False

@allure.feature("Примеры тестов")
@allure.story("Успешные тесты")
def test_pass1():
    pass

@allure.story("Успешные тесты")
def test_pass2():
    pass

@allure.story("Успешные тесты")
def test_pass3():
    pass

@allure.story("Успешные тесты")
def test_pass4():
    pass

@allure.story("Успешные тесты")
def test_pass5():
    pass

@allure.story("Успешные тесты")
def test_pass6():
    pass

@allure.story("Успешные тесты")
def test_pass7():
    pass

@allure.story("Успешные тесты")
def test_pass8():
    pass

@allure.story("Успешные тесты")
def test_pass9():
    pass

@allure.story("Успешные тесты")
def test_pass10():
    pass

@allure.story("Успешные тесты")
def test_pass11():
    pass

@allure.story("Успешные тесты")
def test_pass12():
    pass

@allure.story("Успешные тесты")
def test_pass13():
    pass

@allure.story("Успешные тесты")
def test_pass14():
    pass

@allure.story("Успешные тесты")
def test_pass15():
    pass

@allure.feature("Примеры тестов")
@allure.story("Пропущенные тесты")
@pytest.mark.skip
def test_skipped1():
    pass

@pytest.mark.skip
def test_skipped2():
    pass

@pytest.mark.skip
def test_skipped3():
    pass