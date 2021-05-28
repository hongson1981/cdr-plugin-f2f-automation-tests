from behave import *
#import os
import subprocess

def system_out(command):
    p = subprocess.check_output(command, shell=True)
    return p.decode("utf-8")

use_step_matcher("re")


#@given("that docker compose is up and running")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #print('hello')
#
#@when("the user runs docker ps")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #out = system_out('docker ps')
    #print(out)
    #assert out.find('')
#
#
#@then("the user should be able to see cdr_plugin_folder_to_folder_website")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
##    assert out.find('abuntu')
    #raise NotImplementedError(u'STEP: Then cdr_plugin_folder_to_folder')
#
#
#@then("cdr_plugin_folder_to_folder")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then cdr_plugin_folder_to_folder')
#
#
#@then("cdr_plugin_folder_to_folder_notebooks")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then cdr_plugin_folder_to_folder_notebooks')
#
#
#@then("docker\.elastic\.co/elasticsearch/elasticsearch:\{VERSION}")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then docker.elastic.co/elasticsearch/elasticsearch:{VERSION}')
#
#
#@then("minio/minio:latest")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then minio/minio:latest')
#
#
#@then("docker\.elastic\.co/kibana/kibana:\{VERSION}")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then docker.elastic.co/kibana/kibana:{VERSION}')
#
#
#@then("cdr_plugin_folder_to_folder_notebooks for Voila")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then cdr_plugin_folder_to_folder_notebooks for Voila')
#
#
#@when("the user navigate to http://localhost:1313")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user navigate to http://localhost:1313')
#
#
#@then("the user should be able to access the Workflow UI")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then the user should be able to access the Workflow UI')
#
#
#@then("able to navigate to workflow")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then able to navigate to workflow')
#
#
#@given("the user is on http://localhost:1313")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Given the user is on http://localhost:1313')
#
#
#@when("the user click on workflow/set-ip")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user click on workflow/set-ip')
#
#
#@when("the user enter IPs for sdk and click set-ip")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user enter IPs for sdk and click set-ip')
#
#
#@then("the user should be able to see SDK IP set with provided IP list")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then the user should be able to see SDK IP set with provided IP list')
#
#
#@when("sdk-ip is set")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When sdk-ip is set')
#
#
#@when("the user Navigate to Folder-to-Folder")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user Navigate to Folder-to-Folder')
#
#
#@then("the user should see option to select scenario")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then the user should see option to select scenario')
#
#
#@then("Output Window")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then Output Window')
#
#
#@then("Elastic Search Dashboard Links")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then Elastic Search Dashboard Links')
#
#
#@given("the user is on http://localhost:1313/workflows/f2f-workflows/")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Given the user is on http://localhost:1313/workflows/f2f-workflows/')
#
#
#@when("the user enter folder name into basedirectory field")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user enter folder name into basedirectory field')
#
#
#@when("the user click on set-basedir")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user click on set-basedir')
#
#
#@then("the user should see the output with base directory set to what the user have entered with HD1, HD2 and HD3")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(
        #u'STEP: Then the user should see the output with base directory set to what the user have entered with HD1, HD2 and HD3')
#
#
#@when("the user click on Load Files")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user click on Load Files')
#
#
#@when("time is allowed to files to be loaded")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When time is allowed to files to be loaded')
#
#
#@then('Output window confirm the "All files Loaded"')
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then Output window confirm the "All files Loaded"')
#
#
#@then("the user can see the files in HD2/data/to-do")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then the user can see the files in HD2/data/to-do')
#
#
#@when("the user has already run load files")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user has already run load files')
#
#
#@when("the user click on processing")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When the user click on processing')
#
#
#@when("Allow time to process all the files from HD2")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: When Allow time to process all the files from HD2')
#
#
#@then('the user should be able to see the output confirming "Loop Completed"')
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then the user should be able to see the output confirming "Loop Completed"')
#
#
#@then("the user should see the dashboard confirming all the sdk ips that were configured have been utilised")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(
        #u'STEP: Then the user should see the dashboard confirming all the sdk ips that were configured have been utilised')
#
#
#@then("the user should see the HD3 with processed files")
#def step_impl(context):
    #"""
    #:type context: behave.runner.Context
    #"""
    #raise NotImplementedError(u'STEP: Then the user should see the HD3 with processed files')