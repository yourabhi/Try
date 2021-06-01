Feature: OrangeHRM Logo
  Scenario: Logo Presence on OrangeHRM Homepage
    Given Launch Chrome Browser
    When open the homepage of orangeHRM
    Then Verify Logo is present there
    And Close the browser