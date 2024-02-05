import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

# Заглавная буква

@pytest.mark.parametrize('word, result',[
    ("саша", "Саша"),
    ("zoey", "Zoey"),
    (" ", " "),
    ("", "")

])

def test_capitilize(string_utils,word, result ):
    assert string_utils.capitilize(word) == result

#Удаление пробелов перед словом 

@pytest.mark.parametrize("spacing, no_spacing", [
    (" Привет", "Привет"),
    ("  Hi", "Hi"),
    ("   453", "453"),
    ("Что", "Что"),
    ("", ""),
    (" ", "")
])

def test_trim(string_utils,spacing, no_spacing ):
    assert string_utils.trim(spacing) == no_spacing

# Принимает на вход текст с разделителем и возвращает список строк

@pytest.mark.parametrize("no_delimeter, with_delimetr", [
    ("Привет,пока,нет,что,где",["Привет","пока","нет","что","где"]),
    ("2,3,4,6,4,@,345",["2","3","4","6","4","@","345"]),
    ("2,3", ["2","3"]),
    ("",[])
])
def test_to_list(string_utils,no_delimeter, with_delimetr ):
    assert string_utils.to_list(no_delimeter) == with_delimetr

#Возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.parametrize("string, symbol, T_and_F", [
     ("Sasha", "a",True),
     ("Sasha", "S",True),
     ("Паша", "ш",True),
     ("Геннадий тут", "т",True),
     ("","",True),
     (" "," ",True)
])

def test_contains(string_utils,string, symbol, T_and_F):
     assert string_utils.contains(string, symbol) == T_and_F

# Удаление определнного символа

@pytest.mark.parametrize("str,del_symbol, total", [
     ("Sasha", "as","Sha"),
     ("Камаз", "амаз","К"),
     ("Механизированный", "зированный","Механи"),
     ("","",""),   
])

def test_delete_symbol(string_utils,str,del_symbol, total):
     assert string_utils.delete_symbol(str,del_symbol) == total

#true или false,если строка начинается с заданным символа 

@pytest.mark.parametrize("start_with, symbol, TF", [
     ("Sasha", "S", True),
     ("Камаз", "К", True),
     ("Зулендер", "а", False),
     ("","",True),
     (" "," ",True),
     ("2456", "2", True)
])

def test_starts_with(string_utils, start_with, symbol, TF):
    assert string_utils.starts_with(start_with, symbol) == TF

#true или false,если строка заканчивается с заданным символа 

@pytest.mark.parametrize("end_with, symbol, T__F", [
     ("Нечаев", "в", True),
     ("Саша", "А", False),
     ("Ивановы", "R", False),
     ("","",True),
     (" "," ",True),
     ("9761235", "5", True) 
])

def test_end_with(string_utils, end_with, symbol, T__F):
    assert string_utils.end_with(end_with, symbol) == T__F

#Возвращает `True`, если строка пустая и `False` - если нет

@pytest.mark.parametrize("string, T__F", [
     ("  ", True),
     ("Саша", False),
     ("", True),
     ("784", False)  
])

def test_is_empty(string_utils,string,T__F):
    assert string_utils.is_empty(string) == T__F

#Преобразует список элементов в строку с указанным разделителем

@pytest.mark.parametrize("lst, joiner, result", [
     ([1, 2, 3, 6, 7], ", " , "1, 2, 3, 6, 7"),
     (["Ghost", "Tsushima"], "-", "Ghost-Tsushima"),
     ([], "," , "")
])

def test_list_to_string(string_utils,lst, joiner, result):
    assert string_utils.list_to_string(lst,joiner) == result
