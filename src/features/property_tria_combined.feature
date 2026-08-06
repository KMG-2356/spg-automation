Feature: Commercial Lines Auto Commercial Property and Terrorism Premium verification against excel rater 
  In order to verify the generated a premium
  in Commercial Lines LOB and save it in the excel sheet

  Scenario: Save the premium for Property TRIA Combined LOB
    Given the login page is open
    When the user generates a premium
    Then the generated premium should be saved to excel