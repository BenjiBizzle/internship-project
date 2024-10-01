# Created by B at 10/1/24
Feature: User can go to settings and see the right number of UI elements
  # Enter feature description here

  Scenario: User can see the right number of UI elements
    Given Open the main page
    When Log in to the page
    Then Click on settings option
    Then Verify correct page opens
    And Verify there are 12 options for the settings
    Then Verify connect the company button is available