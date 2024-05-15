Feature: Sign in system
  Scenario: Successful login in system
    Given Login page of Sample App
    When Type username "admin" and password "pwd"
    And Click Log In button
    Then Success message is displayed

