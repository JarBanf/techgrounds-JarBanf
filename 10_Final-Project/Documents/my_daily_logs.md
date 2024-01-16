# <a id="top">My Daily Logs</a> 📓 📅
Here I log my daily progress, solutions, and learnings throughout the project.  

Sorted by latest to oldest.  
<br>

## Table of Contents
- Week 2
    - [Tue 16 Jan '24](#tue16jan)
        - [Finding and understanding the code I need to deploy a basic VPC.](#finding-and-understanding-the-code-i-need-to-deploy-a-basic-vpc)
    - [Mon 15 Jan '24](#mon15jan)
        - [Write some practice CDK code using cdkworkshop.com. Lambda function & API gateway.](#write-some-practice-cdk-code-using-cdkworkshopcom-lambda-function--api-gateway)
- Week 1
    - [Sun 14 Jan '24](#sun14jan)
    - [Sat 13 Jan '24](#sat13jan)
    - [Fri 12 Jan '24](#fri12jan)
        - [Create my first CDK project with AWS CDK Workshop tutorial](#create-my-first-cdk-project-with-aws-cdk-workshop-tutorial)
        - [[SOLVED] Auto-complete for `aws`-commands is not working in VSCode, causing import failure.](#auto-complete-for-aws-commands-is-not-working-in-vscode-causing-import-failure)
    - [Thu 11 Jan '24](#thu11jan)
    - [Wed 10 Jan '24](#wed10jan)
        - [Set up AWS Cloud Development Kit](#set-up-aws-cloud-development-kit)
    - [Tue 09 Jan '24](#tue09jan)
        - [Created a clear and structured document for the infrastructure requirements and questions.](#created-a-clear-and-structured-document-for-the-infrastructure-requirements-and-questions)
    - [Mon 08 Jan '24](#mon08jan)
        - [Watched an introduction video about Jira.](#watched-an-introduction-video-about-jira)
- [Log template](#log-template)  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="tue16jan">Tue 16 Jan '24</a>
### Daily Report
- I made a first version diagram of the network infrastructre. I will be using this diagram as a starting point to start building the network as IaC.
- I started with:  
    | Epic | User Story | Description | Deliverable |
    | - | - | - | - |
    | v1.0 | As a customer, I want a working application with which I can deploy a secure network. | The application must build a network that meets all requirements. An example of a stated requirement is that only traffic from trusted sources may access the management server. | 1. IaC code for the network and all components. |

### Obstacles
- Finding and understanding the code I need to deploy a basic VPC

### Solutions
- #### Finding and understanding the code I need to deploy a basic VPC.
    - Sources
        - [Vpc](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/Vpc.html)
        - [GitHub aws-cdk-examples](https://github.com/aws-samples/aws-cdk-examples/blob/master/python/ec2/instance/app.py)
        - ChatGPT
    - Working code to deploy VPC with only default parameters.

        ```py
        from constructs import Construct
        from aws_cdk import (
            Duration,
            Stack,
            aws_ec2 as ec2,
        )


        class CdkTestprojStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                #create a VPC
                my_vpc = ec2.Vpc(self, 'MyTestVpc',
                    #cidr = '10.0.0.0/16',
                    #ip_addresses = ec2.IpAddresses.cidr('10.0.0.0/16'),
                    #max_azs = 2
                )
        ```

### Learnings
- I know which construct I need to set up a VPC. I still need to find out about the available parameters I will need to build the network.
<br>

*back to [top](#top)* 
<br>

## ✏️ 📄 <a id="mon15jan">Mon 15 Jan '24</a>
### Daily Report
- I practiced CDK deployment using a tutorial.
- Also, my team and I discussed our assumptions and list of services that are important to implement in our infrastructure design. I found this meeting to be very insightful moving forward. 

### Obstacles
- Write some practice CDK code using cdkworkshop.com.

### Solutions
- #### Write some practice CDK code using cdkworkshop.com. Lambda function & API gateway.  
    Instead of the SNS/SQS code that I have in my app now, I’ll add a Lambda function with an API Gateway endpoint in front of it.  

    Users will be able to hit any URL in the endpoint and they’ll receive a heartwarming greeting from our function.  

    - Sources:
        - [Hello, CDK!](https://cdkworkshop.com/30-python/30-hello-cdk.html)

    - Make sure the sample-app is deployed in my AWS cloud. See [Create my first CDK project with AWS CDK Workshop tutorial](#create-my-first-cdk-project-with-aws-cdk-workshop-tutorial) from [Fri 12 Jan '24](#fri12jan).

    - Delete the sample code from my stack. After deletion, my stack looks like this. 
        
        ```py
        from constructs import Construct
        from aws_cdk import (
        Stack
        )


        class CdkWorkshopStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)
        ```
    - Ask toolkit to show us the difference between our CDK app and what's currently deployed.
        
        ```bash
        cdk diff
        ```
        Output:
        
        ```bash
        Stack CdkWorkshopStack
        Creating a change set, this may take a while...
        IAM Statement Changes
        ┌───┬─────────────────────────┬────────┬─────────────────┬───────────────────────────┬─────────────────────────────────────────────────────────┐
        │   │ Resource                │ Effect │ Action          │ Principal                 │ Condition                                               │
        ├───┼─────────────────────────┼────────┼─────────────────┼───────────────────────────┼─────────────────────────────────────────────────────────┤
        │ - │ ${CdkWorkshopQueue.Arn} │ Allow  │ sqs:SendMessage │ Service:sns.amazonaws.com │ "ArnEquals": {                                          │
        │   │                         │        │                 │                           │   "aws:SourceArn": "${CdkWorkshopTopic}"                │
        │   │                         │        │                 │                           │ }                                                       │
        └───┴─────────────────────────┴────────┴─────────────────┴───────────────────────────┴─────────────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Resources
        [-] AWS::SQS::Queue CdkWorkshopQueue CdkWorkshopQueue50D9D426 destroy
        [-] AWS::SQS::QueuePolicy CdkWorkshopQueue/Policy CdkWorkshopQueuePolicyAF2494A5 destroy
        [-] AWS::SNS::Subscription CdkWorkshopQueue/CdkWorkshopStackCdkWorkshopTopicD7BE9643 CdkWorkshopQueueCdkWorkshopStackCdkWorkshopTopicD7BE96438B5AD106 destroy
        [-] AWS::SNS::Topic CdkWorkshopTopic CdkWorkshopTopicD368A42F destroy


        ✨  Number of stacks with differences: 1
        ```
    - Deploy CDK

        ```bash
        cdk deploy
        ```
    
        Output:

        ```bash
        ✨  Synthesis time: 10.87s

        CdkWorkshopStack:  start: Building e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack:  success: Built e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack:  start: Publishing e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack:  success: Published e2e301c815e2e96080a1c52841ba3eca59257bb55f200a4c2bcedab40469944b:current_account-current_region
        CdkWorkshopStack: deploying... [1/1]
        CdkWorkshopStack: creating CloudFormation changeset...

        ✅  CdkWorkshopStack

        ✨  Deployment time: 79.16s

        Stack ARN:
        arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/70149150-b391-11ee-a9b0-0addcb7edc13

        ✨  Total time: 90.03s
        ```
    - Create a directory `lambda` in the root of my project tree (next to the `cdk_workshop`).
    - Add a file called `lambda/hello.py` eith the following contents:

        ```py
        import json

        def handler(event, context):
            print('request: {}'.format(json.dumps(event)))
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'text/plain'
                },
                'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
            }
        ```
        This is a simple Lambda function which returns the text "Hello, CDK! You've hit [url path]". The function's output also includes HTTP status code and HTTP headers. These are used by API Gateway to formulate the HTTP response to the user.
    - Add an `import` statement at the beginning of `cdk_workshop/cdk_workshop_stack.py`, and a `lambda.Function` to my stack.

        ```py
        from constructs import Construct
        from aws_cdk import (
            Stack,
            aws_lambda as _lambda,
        )


        class CdkWorkshopStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                # Defines an AWS Lambda resource
                my_lambda = _lambda.Function(
                    self, 'HelloHandler' ,
                    runtime=_lambda.Runtime.PYTHON_3_12 ,
                    code=_lambda.Code.from_asset('lambda'),
                    handler='hello.handler' ,
                )
        ```
    
    - Save my code, and take a quick look at the diff before I deploy.

        ```bash
        cdk diff
        ```

        Output:

        ```bash
        Stack CdkWorkshopStack
        Creating a change set, this may take a while...
        IAM Statement Changes
        ┌───┬─────────────────────────────────┬────────┬────────────────┬──────────────────────────────┬───────────┐
        │   │ Resource                        │ Effect │ Action         │ Principal                    │ Condition │
        ├───┼─────────────────────────────────┼────────┼────────────────┼──────────────────────────────┼───────────┤
        │ + │ ${HelloHandler/ServiceRole.Arn} │ Allow  │ sts:AssumeRole │ Service:lambda.amazonaws.com │           │
        └───┴─────────────────────────────────┴────────┴────────────────┴──────────────────────────────┴───────────┘
        IAM Policy Changes
        ┌───┬─────────────────────────────┬────────────────────────────────────────────────────────────────────────────────┐
        │   │ Resource                    │ Managed Policy ARN                                                             │
        ├───┼─────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
        │ + │ ${HelloHandler/ServiceRole} │ arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole │
        └───┴─────────────────────────────┴────────────────────────────────────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Resources
        [+] AWS::IAM::Role HelloHandler/ServiceRole HelloHandlerServiceRole11EF7C63 
        [+] AWS::Lambda::Function HelloHandler HelloHandler2E4FBA4D 


        ✨  Number of stacks with differences: 1
        ```

    - Deploy CDK.

        ```bash
        cdk deploy
        ```

        Output:
        
        ```bash
        ✨  Synthesis time: 9.47s

        CdkWorkshopStack:  start: Building 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        CdkWorkshopStack:  success: Built 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        CdkWorkshopStack:  start: Building 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  success: Built 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  start: Publishing 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        CdkWorkshopStack:  start: Publishing 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  success: Published 8e681d924af319446955d3bdfb9e36e8da860119419f1055a1e1447a5729f9d6:current_account-current_region
        CdkWorkshopStack:  success: Published 5f83e2a8bc7ca79afcc300d45df613dd32db40aa141b1ab5d88b910f3dbd995e:current_account-current_region
        This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
        Please confirm you intend to make the following modifications:

        IAM Statement Changes
        ┌───┬─────────────────────────────────┬────────┬────────────────┬──────────────────────────────┬───────────┐
        │   │ Resource                        │ Effect │ Action         │ Principal                    │ Condition │
        ├───┼─────────────────────────────────┼────────┼────────────────┼──────────────────────────────┼───────────┤
        │ + │ ${HelloHandler/ServiceRole.Arn} │ Allow  │ sts:AssumeRole │ Service:lambda.amazonaws.com │           │
        └───┴─────────────────────────────────┴────────┴────────────────┴──────────────────────────────┴───────────┘
        IAM Policy Changes
        ┌───┬─────────────────────────────┬────────────────────────────────────────────────────────────────────────────────┐
        │   │ Resource                    │ Managed Policy ARN                                                             │
        ├───┼─────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
        │ + │ ${HelloHandler/ServiceRole} │ arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole │
        └───┴─────────────────────────────┴────────────────────────────────────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Do you wish to deploy these changes (y/n)? y
        CdkWorkshopStack: deploying... [1/1]
        CdkWorkshopStack: creating CloudFormation changeset...

        ✅  CdkWorkshopStack

        ✨  Deployment time: 42.98s

        Stack ARN:
        arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/70149150-b391-11ee-a9b0-0addcb7edc13

        ✨  Total time: 52.45s
        ```

    - In AWS Console I can see the `CdkWorkshoStack`-resources has status `CREATE_COMPLETE`.

        ![update_complete](/10_Final-Project/includes/15jan24_dl_cdk01.png)
        <br>
        <br>

    - Test my function
        - In the AWS Lambda Console, choose `HelloHandler` function. Configure test event and save.
            
            ![configure test](/10_Final-Project/includes/15jan24_dl_cdk02.png)
            <br>
            <br>
    
        - Click Test again and wait for the execution to complete.

            ![test result](/10_Final-Project/includes/15jan24_dl_cdk03.png)
            <br>
        Status: Succeeded

    - Add a LambdaRestAPI construct to my stack.

        ```py
        from constructs import Construct
        from aws_cdk import (
            Stack,
            aws_lambda as _lambda,
            aws_apigateway as apigw,
        )


        class CdkWorkshopStack(Stack):

            def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
                super().__init__(scope, construct_id, **kwargs)

                # Defines an AWS Lambda resource
                my_lambda = _lambda.Function(
                    self, 'HelloHandler' ,
                    runtime=_lambda.Runtime.PYTHON_3_12 ,
                    code=_lambda.Code.from_asset('lambda'),
                    handler='hello.handler' ,
                )

                apigw.LambdaRestApi(
                    self, 'Endpoint' ,
                    handler=my_lambda,
                )
        ```

    - Save my code, and take a quick look at the diff before I deploy.
    
        ```bash
        cdk diff
        ```

        Output:

        ```bash
        Stack CdkWorkshopStack
        Creating a change set, this may take a while...
        IAM Statement Changes
        ┌───┬─────────────────────┬────────┬───────────────────────┬────────────────────────────────────────────────┬────────────────────────────────────────────────┐
        │   │ Resource            │ Effect │ Action                │ Principal                                      │ Condition                                      │
        ├───┼─────────────────────┼────────┼───────────────────────┼────────────────────────────────────────────────┼────────────────────────────────────────────────┤
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/*"                                         │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/*"          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/"                                          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/"           │
        │   │                     │        │                       │                                                │ }                                              │
        └───┴─────────────────────┴────────┴───────────────────────┴────────────────────────────────────────────────┴────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Resources
        [+] AWS::ApiGateway::RestApi Endpoint EndpointEEF1FD8F 
        [+] AWS::ApiGateway::Deployment Endpoint/Deployment EndpointDeployment318525DA5f8cdfe532107839d82cbce31f859259 
        [+] AWS::ApiGateway::Stage Endpoint/DeploymentStage.prod EndpointDeploymentStageprodB78BEEA0 
        [+] AWS::ApiGateway::Resource Endpoint/Default/{proxy+} Endpointproxy39E2174E 
        [+] AWS::Lambda::Permission Endpoint/Default/{proxy+}/ANY/ApiPermission.CdkWorkshopStackEndpoint018E8349.ANY..{proxy+} EndpointproxyANYApiPermissionCdkWorkshopStackEndpoint018E8349ANYproxy747DCA52 
        [+] AWS::Lambda::Permission Endpoint/Default/{proxy+}/ANY/ApiPermission.Test.CdkWorkshopStackEndpoint018E8349.ANY..{proxy+} EndpointproxyANYApiPermissionTestCdkWorkshopStackEndpoint018E8349ANYproxy41939001 
        [+] AWS::ApiGateway::Method Endpoint/Default/{proxy+}/ANY EndpointproxyANYC09721C5 
        [+] AWS::Lambda::Permission Endpoint/Default/ANY/ApiPermission.CdkWorkshopStackEndpoint018E8349.ANY.. EndpointANYApiPermissionCdkWorkshopStackEndpoint018E8349ANYE84BEB04 
        [+] AWS::Lambda::Permission Endpoint/Default/ANY/ApiPermission.Test.CdkWorkshopStackEndpoint018E8349.ANY.. EndpointANYApiPermissionTestCdkWorkshopStackEndpoint018E8349ANYB6CC1B64 
        [+] AWS::ApiGateway::Method Endpoint/Default/ANY EndpointANY485C938B 

        Outputs
        [+] Output Endpoint/Endpoint Endpoint8024A810: {"Value":{"Fn::Join":["",["https://",{"Ref":"EndpointEEF1FD8F"},".execute-api.",{"Ref":"AWS::Region"},".",{"Ref":"AWS::URLSuffix"},"/",{"Ref":"EndpointDeploymentStageprodB78BEEA0"},"/"]]}}


        ✨  Number of stacks with differences: 1
        ```

    - Deploy CDK.

        ```bash
        cdk deploy
        ```

        Output:
        
        ```bash
        ✨  Synthesis time: 11.55s

        CdkWorkshopStack:  start: Building 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        CdkWorkshopStack:  success: Built 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        CdkWorkshopStack:  start: Publishing 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        CdkWorkshopStack:  success: Published 1db71cd140606ea1a187b8db5a974ea8818f2957daaec5188b866c73f0322b45:current_account-current_region
        This deployment will make potentially sensitive changes according to your current security approval level (--require-approval broadening).
        Please confirm you intend to make the following modifications:

        IAM Statement Changes
        ┌───┬─────────────────────┬────────┬───────────────────────┬────────────────────────────────────────────────┬────────────────────────────────────────────────┐
        │   │ Resource            │ Effect │ Action                │ Principal                                      │ Condition                                      │
        ├───┼─────────────────────┼────────┼───────────────────────┼────────────────────────────────────────────────┼────────────────────────────────────────────────┤
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/*"                                         │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/*"          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/${Endpoint/DeploymentStage.prod │
        │   │                     │        │                       │                                                │ }/*/"                                          │
        │   │                     │        │                       │                                                │ }                                              │
        │ + │ ${HelloHandler.Arn} │ Allow  │ lambda:InvokeFunction │ Service:apigateway.amazonaws.com               │ "ArnLike": {                                   │
        │   │                     │        │                       │                                                │   "AWS:SourceArn": "arn:${AWS::Partition}:exec │
        │   │                     │        │                       │                                                │ ute-api:${AWS::Region}:${AWS::AccountId}:${End │
        │   │                     │        │                       │                                                │ pointEEF1FD8F}/test-invoke-stage/*/"           │
        │   │                     │        │                       │                                                │ }                                              │
        └───┴─────────────────────┴────────┴───────────────────────┴────────────────────────────────────────────────┴────────────────────────────────────────────────┘
        (NOTE: There may be security-related changes not in this list. See https://github.com/aws/aws-cdk/issues/1299)

        Do you wish to deploy these changes (y/n)? y
        CdkWorkshopStack: deploying... [1/1]
        CdkWorkshopStack: creating CloudFormation changeset...

        ✅  CdkWorkshopStack

        ✨  Deployment time: 38.34s

        Outputs:
        CdkWorkshopStack.Endpoint8024A810 = https://b6uougqw64.execute-api.eu-central-1.amazonaws.com/prod/
        Stack ARN:
        arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/70149150-b391-11ee-a9b0-0addcb7edc13

        ✨  Total time: 49.89s
        ```

    - Testing my app
        - Copy the URL and execute.

        ![](/10_Final-Project/includes/15jan24_dl_cdk04.png)
        <br>

        - My app works.
    - Because this is for learning purposes, I will be destroying the deployed CDK app.

        ```bash
        cdk destroy
        ```

### Learnings
- I got to experience a bit more how the process of CDK deployment works. A tiny bit more familiar with the CDK environment. The codes are still gibberish and intimidating to me.
- Discussing our assumptions as a team was really insightful and informational moving forward.  
<br>

*back to [top](#top)* 
<br>

## ✏️ 📄 <a id="sun14jan">Sun 14 Jan '24</a>
### Daily Report
- I completed: 

    | Epic | User Story | Description | Deliverable |
    | - | - | - | - |
    | Exploration | 2: As a team, we want a clear overview of the assumptions we have made. | You have already received a lot of information. There may be questions that none of the stakeholders have been able to answer. Your team should be able to produce an overview of the assumptions you are making as a result. | A point-by-point overview of all assumptions. |    
<br>

*back to [top](#top)* 
<br>

## ✏️ 📄 <a id="sat13jan">Sat 13 Jan '24</a>
### Daily Report
- I finished setting up my Jira SCRUM board for this project.
- Also I started structuring the project folder so it is more organized and easier to explore the process of my project.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="fri12jan">Fri 12 Jan '24</a>
### Daily Report
- I created my first CDK project and tried to understand the process and component.

### Obstacles
- Create my first CDK project with AWS CDK Workshop tutorial
- Auto-complete for `aws`-commands is not working in VSCode, causing import failure.

### Solutions
- #### Create my first CDK project with AWS CDK Workshop tutorial
    - Sources:
        - [AWS CDK Workshop](https://cdkworkshop.com/)
    - Create project directory and go to it.
        
        ```bash
        mkdir cdk_workshop && cd cdk_workshop
        ```

    - Use `cdk init` to create a new Pyhton CDK project.

        ```bash
        cdk init sample-app --language python
        ```

        Response:
        - `✅ All done!`

    - Activate the virtualenv.

        ```bash
        source .venv/bin/activate
        ```

    - Once the virtualenv is activated, install the required dependencies

        ```bash
        pip install -r requirements.txt
        ```

        Response:
        - `Successfully installed attrs-23.2.0 aws-cdk-lib-2.119.0 aws-cdk.asset-awscli-v1-2.2.201 aws-cdk.asset-kubectl-v20-2.1.2 aws-cdk.asset-node-proxy-agent-v6-2.0.1 cattrs-23.2.3 constructs-10.3.0 importlib-resources-6.1.1 jsii-1.94.0 publication-0.0.3 python-dateutil-2.8.2 six-1.16.0 typeguard-2.13.3 typing-extensions-4.9.0`

    - The first time I deploy an AWS CDK app into my environment (account/region), I’ll need to install a “bootstrap stack”.

        ```bash
        cdk bootstrap
        ```
        Response:
        - `✅  Environment aws://908959576754/eu-central-1 bootstrapped.`

    - Before deploying a CDK app, I can synthesize it first to preview the CDK app output CloudFormation file. The output CloudFormation file is the actual thing that gets uploaded into the AWS cloud.  
    To synthesize a CDK app, use the `cdk synth` command.

        ```bash
        cdk synth
        ```
        Response:
        - A CloudFormation template file including the resources.
    
    - Use `cdk deploy` to deploy the CDK app to my default AWS account/region.

        ```bash
        cdk deploy
        ```

        If presented with `Do you wish to deploy these changes (y/n)?`, enter `y`.

        Response:
        - ```bash
            ✅  CdkWorkshopStack

            ✨  Deployment time: 22.37s

            Stack ARN:
            arn:aws:cloudformation:eu-central-1:908959576754:stack/CdkWorkshopStack/0a311dd0-b15d-11ee-abb8-06f21afcb2df

            ✨  Total time: 31.47s
            ```

    - CDK apps are deployed through AWS CloudFormation. This means that I can use the AWS CloudFormation console in order to manage my stacks.

    - To clean up the stack, I can either delete the stack through the AWS CloudFormation console or use `cdk destroy`.

        ```bash
        cdk destroy
        ```

        When asked `Are you sure you want to delete: CdkWorkshopStack (y/n)?`, enter `y`,

        Response:
        - `✅  CdkWorkshopStack: destroyed`
- #### Auto-complete for `aws`-commands is not working in VSCode, causing import failure.
    Install the required python modules BEFORE activating the virtualenv.
    - First:

        ```bash
        pip install -r requirements.txt
        ```
    
    - And then:

        ```bash
        source .venv/bin/activate
        ```

### Learnings
- I know how to create, deploy, and destroy a sample-app project. I have a tiny bit of a understanding how it works.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="thu11jan">Thu 11 Jan '24</a>
### Daily Report
- I completed:
    
    | Epic | User Story | Description | Deliverable |
    | - | - | - | - |
    | Exploration | 1: As a team, we want to be clear about the requirements of the application. | You have already received a lot of information. Some requirements are already mentioned in this document, but this list may be incomplete or unclear. It is important to sort out all the uncertainties before you start doing major work. | A point-by-point description of all requirements. |
    | Exploration | 3: As a team, we want to have a clear overview of the Cloud Infrastructure that the application needs. | You have already received a lot of information. And already a design. Only aspects such as IAM/AD are still missing from the design. Identify these additional services you will need and make an overview of all services. | An overview of all services that will be used. |  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="wed10jan">Wed 10 Jan '24</a>
### Daily Report
- Together with my team we had a meeting with the product owner to discuss the requirements for the cloud infrastructure that we individually have to develop. I still have to process these requirements in a deliverable document.  

- Also, I started with the set-up of AWS CDK on my workstation.

### Obstacles
- Set up AWS Cloud Development Kit.

### Solutions
- #### Set up AWS Cloud Development Kit.

    - Sources:
        - [Working with the AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
        - [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

    - Create Access keys in IAM.
    - Install [AWS Command Line Interface](https://aws.amazon.com/cli/).

        ```bash
        curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
        sudo installer -pkg ./AWSCLIV2.pkg -target /
        ```

    - Verify that the shell can find and run the aws command in my `$PATH`.

        ```bash
        which aws
        aws --version
        ```

        Response:  
        - `/usr/local/bin/aws`
        - `aws-cli/2.15.9 Python/3.11.6 Darwin/21.6.0 exe/x86_64 prompt/off`

    - Configure my workstation so the AWS CDK uses my credentials.

        ```bash
        aws configure
        ```

        ```bash
        AWS Access Key ID [None]: my-access-key-id
        AWS Secret Access Key [None]: my-secret-key-id
        Default region name [None]: eu-central-1
        Default output format [None]: json
        ```

    - Install [Node.js](https://nodejs.org/).
    - Install AWS CDK Toolkit.  
    
        ```bash
        sudo npm install -g aws-cdk
        ```
    
    - Test CDK installation. 
    
        ```bash
        cdk --version
        ```
        
        Response: 
        - `2.118.0 (build a40f2ec)`

    - Install Package Installer for Python (`PIP`) and virtual environment manager (`virtualenv`).

        ```bash
        python3 -m ensurepip --upgrade
        python3 -m pip install --upgrade pip
        python3 -m pip install --upgrade virtualenv
        ```

### Learnings
- During the meeting with the product owner I got more information about the cloud infrastructure requirements that I will need to adhere to when developing the cloud infrastructure.

- I know now how to set up the AWS CDK on my workstation. That being said, this AWS CDK is still totally new for me. I may have successfully set up AWS CDK on my workstation, but I still do no not understand how it works, and how to interact with it.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="tue09jan">Tue 09 Jan '24</a>
### Daily Report
- I made a list of questions for our meeting with the product owner tomorrow at 9:15. I also created a clear and structured document where the requirements and questions were categorized.

### Obstacles
- Missing a clear and structured overview of the already known requirements in combination with the questions towards the other not yet known requirements. 

### Solutions
- #### Created a clear and structured [document](https://docs.google.com/drawings/d/1Emfy-G-C1uBrazpZSeBZxsg9z3ydj0bhI2TDCuuZbHs/edit?usp=sharing) for the infrastructure requirements and questions.

### Learnings
- It helps and it is more efficient to create a clear overview for myself and my team of all that we need to go into a meeting prepared.  
<br>

*back to [top](#top)*  
<br>

## ✏️ 📄 <a id="mon08jan">Mon 08 Jan '24</a>
### Daily Report
- First day of the project. I read and tried to understand what the project is about and what is expected from me.

- We will be using Jira to track our progress throughout the project. I read and watched a video on what Jira is about. Also made an account.

### Obstacles
- No idea what Jira is about.

### Solutions
- #### Watched an introduction [video](https://www.youtube.com/watch?v=GWxMTvRGIpc) about Jira.

### Learnings
- I have a better understanding why Jira is a handy tool to use during projects.  
<br>

*back to [top](#top)*  
<br>

++++++++++++++++++++
## Log template
Template for easy daily logging  

## ✏️ 📄 <a id="indert-date-here">insert-date-here</a>
### Daily Report
- ...

### Obstacles
- ...

### Solutions
- ...

### Learnings
- ...  
<br>

*back to [top](#top)* 
<br>
++++++++++++++++++++