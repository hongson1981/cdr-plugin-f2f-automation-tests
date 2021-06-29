# Created by DharamPatel at 24/06/2021
Feature: Folder to Folder Plugin UI is Accessible and fully functional
  # Enter feature description here

  Background: folder to folder containers are up and running
    Given All F2F containers are UP and running
    And user is on http://<IP/URL>:<PORT>

  Scenario: User can access CDR Plugin UI
    When the user navigate to "http://<ip/URL>:<port>"
    Then the user should see CDR F2F UI

  Scenario: User can access Workflows page
    When User Navigate to Workflows
    Then the user should see Workflows and Configration tabs
    And Output Window
    And Elastic Dashboard Links

  Scenario: User can set base directory
    When the user click on configuration tab
    And the user select Scenarios from radio button and select Scenario from Drop-down and click on "Set base dir"
    Then the user should see the pop-up confirming "Successfully Configured"

  Scenario: User can load SDK IPs from AWS
    When the user click on configuration tab
    And the user click on "Load from AWS"
    Then the user should be able to see list of SDK IP from AWS

  Scenario: User can set SDK IPs from AWS
    When the user click on configuration tab
    And the user click on "Load from AWS"
    And click on "Set Plugin IPs"
    Then the user should be able to see pop-up confirming "Successfully set"

  Scenario: User can set SDK IPs manually
    When the user click on configuration tab
    And the user clic on Add button
    And user enter IP and Port for Running SDK
    And the user click on "Set Plugin IPs"
    Then the user should be able to see pop-up confirming "Successfully set"

  Scenario: User can "clear" files from HD2
    When User click on Workflows tab
    And user click on "Clear Data"
    Then Output window confirm "Data cleared from HD2"
    And the user should be able to see pop-up confirming "Clear Data And Status Folders Successfully"
    And the user does not see the files in HD2/data/todo

  Scenario: User can "load" files for processing
    When User click on Workflows tab
    And the user has set base dir
    And sdk-ip is set
    And the user click on Load Files
    Then Output window confirm the "PreProcessing is done"
    And the user can see the files in HD2/data/to-do

  Scenario: User can "start" processing files
    When User click on Workflows tab
    And the user has set base dir
    And sdk-ip is set
    And the user has already run "Load Files"
    And the user click on "Start Processing"
    Then the user should be able to see the output confirming "Loop Completed"
    And the user see the pop-up confirming "Processing completed successfully"
    And the user should see processing data and metrics in "Processed Files v8" Dashboard
    And the user should see the dashboard confirming all the sdk ips that were configured have been utilised
    And the user should see processed files in HD3

  Scenario: User can "stop" processing files
    When User click on Workflows tab
    And the user has set base dir
    And sdk-ip is set
    And the user has already run "Load Files"
    And the user click on "Start Processing"
    And user allow for processing to start
    And the user press "Stop Processing" button
    Then the user should be able to see the output confirming "Processing stopped done"
    And user should see pop-up confirming "Stopped Successfully"
    And the user should see that no new metrics is present in "Processed Files v8" Dashboard

  Scenario: User can see processing status
    When User click on Workflows tab
    And click on Status button
    Then the user should see pop-up confirming "current_status" set to corresponding value (Started/Stopped)

  Scenario: User can see current configuration
    When User click on Workflows tab
    And click on View Config link
    Then the user can see server configuration

  Scenario: User can access CDR F2F documentation
    When the user navigate to url "http://<IP/URL>:<PORT>/docs/"
    Then the user should see Docs Pages
