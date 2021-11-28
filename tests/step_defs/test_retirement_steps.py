from pytest_bdd import scenario, parsers, given, when, then
from retirement import *


EXTRA_TYPES = {
    'Number': int,
}


CONVERTERS = {
    'year': int,
    'month': int,
}



scenario('../features/retire_age.feature', 'Birth year entered in range')
def test_retire_year():
    pass


@given('The input is numbers', target_fixture='input_valid')
def input_valid():
    pass


@when(parsers.cfparse('Birth "{year:Number}" is input', extra_types=EXTRA_TYPES))
@when('Birth "<year>" is input')
def check_year(year):
    assert _validate_age_year(year)
    year_correct = True
    return year_correct


@when(parsers.cfparse('Birth "{month:Number}" is input', extra_types=EXTRA_TYPES))
@when('Birth "<month>" is input')
def check_month(month):
    assert _validate_birth_month(month)
    month_correct = True
    return month_correct


@then('The correct year and month is listed for age to retire along with how many years that will be')
def output_correct():
    pass
