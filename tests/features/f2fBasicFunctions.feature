# Created by DharamPatel at 26/05/2021
Feature: Folder to Folder Basic Function
  # User should be able to start the plugin and access various component of workflow cluster and
  # able to run some test

  Scenario: User sees Services are running on Docker
    Given that docker compose is up and running
    When the user runs docker ps
    Then the user should be able to see cdr_plugin_folder_to_folder_website
    Then cdr_plugin_folder_to_folder
    Then cdr_plugin_folder_to_folder_notebooks
    Then docker.elastic.co/elasticsearch/elasticsearch:{VERSION}
    Then minio/minio:latest
    Then docker.elastic.co/kibana/kibana:{VERSION}
    Then cdr_plugin_folder_to_folder_notebooks for Voila

  Scenario: User can access Workflow UI
    Given that docker compose is up and running
    When the user navigate to http://localhost:1313
    Then the user should be able to access the Workflow UI
    Then able to navigate to workflow

  Scenario: User can Set IPs using Workflow
    Given the user is on http://localhost:1313
    When the user click on workflow/set-ip
    When the user enter IPs for sdk and click set-ip
    Then the user should be able to see SDK IP set with provided IP list

  Scenario: User can access F2F Workflow
    Given the user is on http://localhost:1313
    When sdk-ip is set
    When the user Navigate to Folder-to-Folder
    Then the user should see option to select scenario
    Then Output Window
    Then Elastic Search Dashboard Links

  Scenario: User can Map Base Directory using F2F Workflow
    Given the user is on http://localhost:1313/workflows/f2f-workflows/
    When sdk-ip is set
    When the user enter folder name into basedirectory field
    When the user click on set-basedir
    Then the user should see the output with base directory set to what the user have entered with HD1, HD2 and HD3

  Scenario: User can Load Files for Processing using F2F Workflow
    Given the user is on http://localhost:1313/workflows/f2f-workflows/
    When sdk-ip is set
    When the user click on Load Files
    When time is allowed to files to be loaded
    Then Output window confirm the "All files Loaded"
    Then the user can see the files in HD2/data/to-do

  Scenario: User can Process Files using F2F Workflow
    Given the user is on http://localhost:1313/workflows/f2f-workflows/
    When sdk-ip is set
    When the user has already run load files
    When the user click on processing
    When Allow time to process all the files from HD2
    Then the user should be able to see the output confirming "Loop Completed"
    Then the user should see the dashboard confirming all the sdk ips that were configured have been utilised
    Then the user should see the HD3 with processed files