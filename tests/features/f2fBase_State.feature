# Created by DharamPatel at 26/05/2021
Feature: Folder to Folder Base State
  # User should be able to start the plugin and access various component of workflow cluster and
  # able to run some test

  Scenario Outline: User can access <container>
    Given that docker compose is up and running
    When the user sends a request to http://localhost:<port>
    Then the user should receive a <expected_code> response from <container>
    Examples: dockerContainers
        | port | container | expected_code |
        | 8880 | Swagger   | 200          |
        | 5601 | Kibana    | 200          |
        | 9000 | Minio     | 403          |
        | 1313 | UI        | 200          |
        | 8888 | Jupyter   | 200          |
        | 8866 | Voila     | 200          |
        | 9200 | Elastic   | 200          |

  Scenario Outline: can view Processing Status
    Given that docker compose is up and running
    When the Endpoint http://<ip_address>:<port>/<endpoint> is called
    Then the user should receive a <expected_code>
    And showing the processing status
    Examples:
        | ip_address | port | endpoint          | method | body | expected_code | headers |
        | 127.0.0.1  | 8880 | processing/status | GET    | None | 200           | None    |

  Scenario Outline: User can Set IPs
    Given that docker compose is up and running
    When the Endpoint http://<ip_address>:<port>/<endpoint> is called
    Then the user should receive a <expected_code>
    And the user should be able to see SDK IP set with provided IP list
    Examples:
        | ip_address | port | endpoint | method | body | expected_code | headers |
        | 127.0.0.1  | 8880 | configuration/configure_gw_sdk_endpoints | POST | { "Endpoints": [{ "IP": "gw-cloud-sdk-455649808.eu-west-1.elb.amazonaws.com", "Port": "8080" }]} | 200 | {"accept": "application/json","Content-Type": "application/json"} |

  Scenario Outline: User can Map Base Directory
    Given that docker compose is up and running
    And sdk-ip is set
    When the Endpoint http://<ip_address>:<port>/<endpoint> is called
    Then the user should receive a <expected_code>
    And the user should see a response showing the base directory matches the user input
    And mapped directory contains hd1, hd2 and hd3
    Examples:
      | ip_address   | port   | endpoint   | method | body | expected_code | headers |
      | 127.0.0.1 | 8880 | configuration/configure_env/ | POST | { "hd1_path": "./test_data/scenario-2/hd1","hd2_path": "./test_data/scenario-2/hd2","hd3_path": "./test_data/scenario-2/hd3"} | 200 | {"accept": "application/json","Content-Type": "application/json"} |

  Scenario Outline: User can Load Files for Processing
    Given that docker compose is up and running
    And sdk-ip is set
    When the Endpoint http://<ip_address>:<port>/<endpoint> is called
    Then the user should receive a <expected_code>
    And the user will see response "All files Loaded"
    And the user can see the files in HD2/data/to-do
    And the user can see the files in {path}hd2/to-do
    Examples:
      | ip_address   | port   | endpoint   | method | body | expected_code | headers |
      | 127.0.0.1 | 8880 | pre-processor/pre-process?thread_count=10 | POST |  | 200 | {"accept": "application/json"} |

  Scenario Outline: User can Process Files
    Given that docker compose is up and running
    And sdk-ip is set
    And the user has already run load files
    When the Endpoint http://<ip_address>:<port>/<endpoint> is called
    Then the user should receive a <expected_code>
    And the user should be able to see the output confirming "Loop Completed"
    And the user should see the HD3 with processed files
    Examples:
      | ip_address   | port   | endpoint   | method        | body | expected_code | headers |
      | 127.0.0.1 | 8880 | processing/start?thread_count=10 | POST |  | 200 | {"accept": "application/json"} |