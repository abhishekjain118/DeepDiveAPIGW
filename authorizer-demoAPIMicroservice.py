import json

def lambda_handler(event, context):
    # TODO implement
    print("************ the event is **************")
    print(event)
    
    # check if authToken is valid
    auth = "Deny"
    if event["authorizationToken"] == 'iamgroot':
        auth = "Allow"

    #return the response
    authResponse = {
        "policyDocument":{
            "Version":"2012-10-17",
            "Statement":[
                {
                    "Action":"execute-api:Invoke",
                    "Resource":[
                        "arn:aws:execute-api:eu-west-2:548678486092:nnz4uc9tz3/*/DELETE/"
                        ],
                    "Effect":auth
                }
                ]
        } 
    }
    return authResponse
    
