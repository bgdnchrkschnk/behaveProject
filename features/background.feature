# To off environment.py settings before run

Feature: Background steps introducing

  Background: common steps
    Given Open a browser
    When Go to ask.fm
    And Refresh page

  Scenario: Find a Logo
    Then Assert logo

  Scenario: Check Login form
    And Click to Sign In
    Then Assert username
    And Assert password