# AWSLambdaWeedGenomics
A Bunch of AWS Lambda functions for weedgenomics.com

# Steps to deploy
AWS Lambda documentation for deploying python functions is self explanatory. A developer should be able to figure out most from reading it. There are few intricate details that I will focus my attention as these steps have either changed in the documentation or I figured these out myself from reading technical blogs from other developers. For the purpose of discussion, I assume that you have the function which is receiving the event and returning the output as per the AWS documentation.A few things to pay attention are:

1. Always make sure to add the dependencies for the function in the root folder before zipping the function. For Example, if your function depends on biopython( which is not present in default library of python), then you need to pip install the dependecy in the root folder where function.py is present. If the dependencies are not in the root folder, then the function won't be detected at all.

2. Zip the root folder by running zip command inside the root directory and not outside the root directory.

3. If the function takes long time to execute, for example, more than 3 seconds, then you need to manually change the configuration of the function by going into AWS Lambda console and change the timeout value in the configuration section of the function manually.

4. There are two major ways of calling lambda functions in your AWS application. Both ways are complicated and require reading technical blogs or AWS documentation. You can either use AWS sdk to call lambda function in your application or use AWS API Gateway to create an API endpoint which can be accessed from anywhere as well. In my opinion, the first option is better of legibility purposes and easier to support in long term. In oprder to understand the usage of AWS sdk you need to create an incognito credential for UNAUTHORIZED access to the lambda function. Once the credential is there, you can use it to call lambda function from Javascript sdk in the web application.
