# Cloud SDK Postman Runner

## Prerequisite
1. Postman is installed https://www.postman.com/downloads/
2. Newman is installed for running the collection via CLI https://www.npmjs.com/package/newman

## Running in Postman
1. Import the postman collection and environment
2. Update working directory to test_files in postman settings (this is needed so that  files are loaded properly)
3. Execute requests 1 by 1 or via postman runner


## Running via Newman

```
newman run 'Glasswall File Rebuild Product API.postman_collection.json' -e cloud-sdk.postman_environment.json --working-dir test_files/
```
