Feature: User Login
  To access the dashboard
  As a registered user
  I want to log in with my credentials

  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid username and password
    Then the user should see the dashboard

  Scenario: Failed login with invalid password
    Given the user is on the login page
    When the user enters valid username and invalid password
    Then the user should see an error message

  Scenario: Failed login with empty credentials
    Given the user is on the login page
    When the user leaves username and password empty
    Then the user should see a warning message

  Scenario: Failed login with locked account
    Given the user is on the login page
    When the user enters credentials of a locked account
    Then the user should see an account locked message