@retirement
Feature: Retirement Age Calculator
    I want to input my age,
    I want to find out what age I can retire.

    # Year inbound range
    Scenario Outline: Birth year entered in range
        Given The input is numbers
        When Birth "<year>" is input
        Then The correct year and month is listed for age to retire along with how many years that will be

        Examples: B-Y Boundaries
            | year |
            | 1900 |
            | 2021 |

    # Year out-of-bounds
    Scenario Outline: Birth year entered out of range
        Given The input is a number
        When Birth "<year>" is input
        Then A Value error is raised

        Examples: B-Y Error Tests
            | year  |
            | -1900 |
            | 1899  |
            | 2022  |
            | 3000  |

    # Month inbound range
    Scenario Outline: Birth month entered in range
        Given The input is a number
        When Birth "<month>" is input
        Then The correct year and month is listed for age to retire along with how many years that will be

        Examples: B-M Boundaries
            | month |
            |   1   |
            |   12  |

    # Month out-of-bounds
    Scenario Outline: Birth month entered out of range
        Given The input is a number
        When Birth "<month>" is input
        Then A Value error is raised

        Examples: B-M Error Tests
            | month |
            |   0   |
            |   13  |
