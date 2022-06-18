from great_module import say_hello

def test_great_module_no_params():
    assert say_hello() == "Happy Coding !"

def test_great_module_with_params():
    assert say_hello("Everyone") == "EVERYONE, CODE FASTER !"

