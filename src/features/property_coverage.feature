Feature: Commercial Lines Property Coverage (CP) Premium verification againts excel rater 
  In order to verify the generated a premium
  in Commercial Lines LOB and save it in the excel sheet

  Scenario: Save the premium for Commercial Property LOB
    Given the login page is open
    When the user generates a premium
    Then the generated premium should be saved to excel