# Created by JamiePool at 14/06/2021
Feature: # SDK API Tests
  # Enter feature description here

  Scenario: User can request a health check
    Given the SDK machine is running
    When the Endpoint http://<ip_address>:8080/api/health is called
    #Can pass API URL as string and reuse method in other tests
    Then the user is returned status OK

  Scenario: User can request engine version
    Given the SDK machine is running
    When the Endpoint http://<ip_address>:8080/api/detail/version is called
    Then the user is returned the version ID of sdkEngineVersion
    And sdkApiVersion

  Scenario: User can request file type detection
    Given the SDK machine is running
    And the user can access http://<ip_address>:8080
    When the user runs Endpoint http://<ip_address>:8080/api/filetypedetection/base64
#    And the user uploads file it wants to use #This data should be passed as part of above call
    Then the user is returned response code 200 and response containing: file type name and size
    #Above step should be split into two so the step 'Then the user receives a 200 OK response' can be reused

  Scenario: User can request processing of a file
    Given the SDK machine is running
    And Health Check shows status OK
    When the Endpoint http://<ip_address>:8080/api/rebuild/file is called
#    And file is supplied #This data should be passed as part of above call
    Then the user receives a 200 OK response
    And the returned binary representation of the Processed File

  Scenario: User can request processing of a file in base64 format
    Given the SDK machine is running
    And Health Check shows status OK
    When the Endpoint http://<ip_address>:8080/api/rebuild/base64 is called
#    And an Encoded Base64 string of a file is supplied #This data should be passed as part of above call
    Then the user receives a 200 OK response
    And the returned Encoded Base64 string of the Processed File

  Scenario: User can request processing of zip file
    Given the SDK machine is running
    And Health Check shows status OK
    When the Endpoint http://<ip_address>:8080/api/rebuild/api/rebuild/zipfile is called
#    And zip file is supplied #This data should be passed as part of above call
    Then the user receives a 200 OK response
    And the returned binary representation of processed zip file

  Scenario: User can request processing protected zip file
    Given the SDK machine is running
    And Health Check shows status OK
    When the Endpoint http://<ip_address>:8080/api/rebuild/protectedzipfile is called
#    And protected zip file and password are provided #This data should be passed as part of above call
    Then the user receives a 200 OK response
    And the returned binary representation of protected zip file

  Scenario: User can request file analysis
    Given the SDK machine is running
    And Health Check shows status OK
    When the Endpoint http://<ip_address>:8080/api/analyse/base64 is called
#    And file is supplied #This data should be passed as part of above call
    Then the user receives a 200 OK response
    And analysis report is returned

  Scenario: User can request xml report of rebuilt file
    Given the SDK machine is running
    And a File has been processed
    When the Endpoint http://<ip_address>:8080/api/analyse/xmlreport?fileId={FILE_ID} is called
    Then the user receives a 200 OK
    And is able to download the xml report

  Scenario: User can request analysis as zip file using FileId
    Given the SDK machine is running
    And a File has been processed
    When the Endpoint http://<ip_address>:8080/api/analyse/rebuildzip
#    And the fileId is provided #This data should be passed as part of above call
    Then the user receives a 200 OK
    And zip file's binary content is returned

  Scenario: User can request analysis as zip file using binary data
    Given the SDK machine is running
    And a File has been processed
    When the Endpoint http://<ip_address>:8080/api/analyse/rebuild-zip-from-file
#    And the zip file is provided #This data should be passed as part of above call
    Then the user receives a 200 OK
    And the zip file's binary content is returned to the client.

  Scenario: User can request analysis as zip file with base64 representation
    Given the SDK machine is running
    And a File has been processed
    When the Endpoint http://<ip_address>:8080/api/analyse/rebuild-zip-from-base64
#    And the zip file is provided #This data should be passed as part of above call
    Then the user receives a 200 OK
    And zip file is returned in the response body