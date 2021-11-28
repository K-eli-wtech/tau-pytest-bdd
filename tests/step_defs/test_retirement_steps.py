from pytest_bdd import scenario, parsers, given, when, then
import retirement


CONVERTERS = {
    'year': int,
    'month': int,
}


scenario('../features/retire_age.feature', 'Birth year entered in range')
def test_retire_year():
    pass


@given(parsers.cfparse('the input is numbers'))
def check_input():
    raise NotImplementedError(u'STEP: Given The input is numbers')


@when(parsers.cfparse('birth "{year:Number}" is input', extra_types=EXTRA_TYPES))
@when('birth "{year:Number}" is input')
def year_in_check(check_input, year):
    raise NotImplementedError(u'STEP: When Birth "<year>" is input')


@then("The correct year and month is listed for age to retire along with how many years that will be")
def step_impl():
    raise NotImplementedError(
        u'STEP: Then The correct year and month is listed for age to retire along with how many years that will be')


@given(parsers.parse('the valid birth month is {birth_month}'),
       target_fixture='check_all_inputs',
       converters=CONVERTERS)
@given(parsers.parse('the valid birth yar is {birth_year}'),
       target_fixture='check_all_inputs',
       converters=CONVERTERS)
@given(parsers.parse('the retirement age is {retirement_age} and {remaining_months}'),
       target_fixture='check_all_inputs',
       converters=CONVERTERS)
def check_all_inputs(birth_month, birth_year, retirement_age, remaining_months):
    assert calculate_retirement_date(birth_year, birth_month, age_years=retirement_age, age_months=remaining_months)


@when(parsers.parse('I calculate the retirement date'),
      target_fixture='set_all_inputs',
      converters=CONVERTERS)
def set_all_inputs(birth_month, birth_year, retirement_age, remaining_months):
    month, year = calculate_retirement_date(birth_year=birth_year,
                                            birth_month=birth_month,
                                            age_years=retirement_age,
                                            age_months=remaining_months)
    return month, year


@then(parsers.parse('the month of retirement should be {month} as of 2021'),
      target_fixture='calculate_retire_date',
      converters=CONVERTERS)
@then(parsers.parse('the year of retirement should be {year} as of November 18, 2021'),
      target_fixture='calculate_retire_date',
      converters=CONVERTERS)
def calculate_retire_date(birth_year, birth_month, retirement_age, remaining_months):
    month, year = set_all_inputs(birth_month, birth_year, retirement_age, remaining_months)
    assert month == month
    assert year == year


@scenario('../features/retirement.feature', 'Calculate retirement age')
def test_cra():
    pass


@given(parsers.parse('the {birth_year} entered is valid'),
       target_fixture="determine_retirement_age",
       converters=CONVERTERS)
def determine_retirement_age(birth_year):
    assert calculate_retirement_age(birth_year=birth_year)


@when(parsers.parse('I enter {birth_year}'),
      target_fixture="set_birth_year",
      converters=CONVERTERS)
def set_birth_year(birth_year):
    ra, rm = calculate_retirement_age(birth_year=birth_year)
    return ra, rm


@then(parsers.parse('the retirement age should be {retirement_age} years as of year 2021'),
      target_fixture='execute_retirement_age',
      converters=CONVERTERS)
def execute_retirement_age(birth_year, retirement_age):
    age, months = set_birth_year(birth_year=birth_year)
    assert age == retirement_age


@then(parsers.parse('the remaining months of the retirement age should be {remaining_months} months'),
      target_fixture='execute_retirement_age',
      converters=CONVERTERS)
def execute_remaining_months(birth_year, remaining_months):
    age, months = set_birth_year(birth_year=birth_year)
    assert months == remaining_months