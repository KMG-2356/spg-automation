Feature: Commercial Lines Propert, General Liability and Terrorism (Prop + GL + TRIA) Premium verification againts excel rater 
  In order to verify the generated a premium
  in Commercial Lines LOB and save it in the excel sheet

  Scenario: Save the premium for Property General Liability TRIA Combined LOB
    Given the login page is open
    When the user generates a premium
    Then the generated premium should be saved to excel