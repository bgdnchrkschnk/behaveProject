Feature: Home page of a google

  Scenario: Page loads successfully
    Given Open a Firefox browser
    When Navigate to a google home page
    Then Google Home Page url is correct

  Scenario: Searching something in a search bar
    Given A google home page
    When Search something in a search bar
    Then Central logo is not visible
    And Page url is not as home page
