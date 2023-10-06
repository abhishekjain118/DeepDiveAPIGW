import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CommentsOnMyResume')
id_db = uuid.uuid4()

def lambda_handler(event, context):
    
    #collect data from the body of the API request
    fName = event['fName']
    lName = event['lName']
    company = event['company']
    comment = event['comment']
    
    response = table.put_item(
        Item={
            'ID':str(id_db),
            'FirstName':fName,
            'LastName':lName,
            'company':company,
            'comment':comment
            }
        )
    status_code = response['ResponseMetadata']['HTTPStatusCode']

#store the data into the table
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('thank you for your comment. Your comment has been saved in the DB and the DB status code is ' + str(status_code) )
    }
