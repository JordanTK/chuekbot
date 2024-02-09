from responses import GoodMorning
gm = GoodMorning()
def test_good_morning():
    assert gm.good_morning("Добро утро!")
    assert gm.good_morning("ДОБРО УТРО!")
    assert gm.good_morning("Лек ден и добро утро приятели!")
    assert gm.good_morning("ДоБрО УтРо.")
def test_not_good_morning():
    assert not gm.good_morning("доброутро.")
    assert not gm.good_morning("Кафето е добро. Утрото не съвсем.")
    assert not gm.good_morning("утро добро")
    assert not gm.good_morning("добро, утро.")