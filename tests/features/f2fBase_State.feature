# Created by DharamPatel at 26/05/2021
Feature: Folder to Folder Base State
  # User should be able to start the plugin and access various component of workflow cluster and
  # able to run some test

  Scenario Outline: User can access <container>
    Given that docker compose is up and running
    When the user sends a request to http://localhost:<port>
    Then the user should receive a <expected_code> response from <container><actual_code>
    Examples: dockerContainers
        | port | container | expected_code | actual_code |
        | 1313 | UI        | 200          |              |
        | 8880 | Swagger   | 200          |              |
        | 5601 | Kibana    | 200          |              |
        | 9000 | Minio     | 200          |              |
        | 8888 | Jupyter   | 200          |              |
        | 8866 | Voila     | 200          |              |

  Scenario: can view Processing Status
    Given Given that docker compose is up and running
    When the Endpoint http://{IP_ADDRESS}:8080/processing/status is called
    Then the user should receive a response showing the processing status

  Scenario: User can Set IPs
    Given that docker compose is up and running
    When the Endpoint http://{IP_ADDRESS}:8080/configuration/configure_multiple_gw_sdk_endpoints is called
    Then the user should be able to see SDK IP set with provided IP list

  Scenario: User can Map Base Directory
    Given that docker compose is up and running
    And sdk-ip is set
    When the Endpoint http://{IP_ADDRESS}:8080/configuration/config/ is called
    Then the user should see a response showing the base directory matches the user input
    And mapped directory contains hd1, hd2 and hd3

  Scenario: User can Load Files for Processing
    Given Given that docker compose is up and running
    And sdk-ip is set
    When the Endpoint http://{IP_ADDRESS}:8080/pre-processor/pre-process?thread_count=10 is called
    Then the user will see response "All files Loaded"
    Then the user can see the files in HD2/data/to-do
    And the user can see the files in {path}hd2/to-do

  Scenario: User can Process Files
    Given that docker compose is up and running
    And sdk-ip is set
    And the user has already run load files
    When the Endpoint http://{IP_ADDRESS}:8080/processing/start?thread_count=10 is called
    Then the user should be able to see the output confirming "Loop Completed"
    And the user should see the HD3 with processed files