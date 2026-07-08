Feature: User Login
  In order to verify the site Login
  As a demo
  I want to Login user using the given credentials

  Scenario: TS-01-02 - Successful Login
    Given the login page is open
    When the user logs in with valid user
    Then the login should be successfull
