Feature: Sign in system
  Scenario Outline: Successful login in system
    Given Login page of Sample App
    When Type username "<admin>" and password "<password>"
    And Click Log In button
    Then Success message is displayed
    Examples:
      | admin | password |
      | 1     | pwd      |
      | 2     | pwd      |