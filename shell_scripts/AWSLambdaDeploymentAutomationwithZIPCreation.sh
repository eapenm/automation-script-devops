#!/bin/bash

LAMBDA_FUNCTION_NAME="your-lambda-function"
DEPLOYMENT_PACKAGE="lambda-package.zip"

# Navigate to lambda directory and create package
cd /path/to/lambda-function
zip -r $DEPLOYMENT_PACKAGE .

# Deploy to AWS Lambda
aws lambda update-function-code --function-name $LAMBDA_FUNCTION_NAME --zip-file fileb://$DEPLOYMENT_PACKAGE
