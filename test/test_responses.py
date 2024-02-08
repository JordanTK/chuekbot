from responses import GoodMorning

# test instance of good morning class- response to a message
gm = GoodMorning()

# Positive tests in each of the cases the bot should recognise this as a valid good morning message and react with a hot drink emoji
def test_good_morning():
    assert gm.good_morning("Добро утро!")
    assert gm.good_morning("ДОБРО УТРО!")
    assert gm.good_morning("Лек ден и добро утро приятели!")
    assert gm.good_morning("ДоБрО УтРо.")

# Negative test cases in each of them the bot should identify that this is not a good morning message and therefore not react to it
# with a hot drink emoji
def test_not_good_morning():
    assert not gm.good_morning("доброутро.")
    assert not gm.good_morning("Кафето е добро. Утрото не съвсем.")
    assert not gm.good_morning("утро добро")
    assert not gm.good_morning("добро, утро.")