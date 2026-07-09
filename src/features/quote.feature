Feature: Premium verification againts excel rater 
  In order to verify the generate a premium
  in windhail LOB and compare it with the rater sheet premium

  Scenario: TS-001 - Rater Premium and Excel Premium are equal for Windhail LOB
    Given the home page is open
    When the user generates a premium
    Then the generated premium should be equal to excel rater premium
