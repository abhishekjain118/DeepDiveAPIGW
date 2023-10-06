import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Extract values from the event JSON
    item = event
    
    # Define the DynamoDB table name
    table_name = 'CommentsOnMyResume'
    
    # Define the update expression and attribute values
    update_expression = 'SET #FirstName = :FirstName, #LastName = :LastName, #company = :company, #comment = :comment'
    expression_attribute_values = {
        ':FirstName': {'S': item['fName']},
        ':LastName': {'S': item['lName']},
        ':company': {'S': item['company']},
        ':comment': {'S': item['comment']}
    }
    expression_attribute_names = {
        '#FirstName': 'FirstName',
        '#LastName': 'LastName',
        '#company': 'company',
        '#comment': 'comment'
    }

    # Update the item in the DynamoDB table
    response = dynamodb.update_item(
        TableName=table_name,
        Key={
            'ID': {'S': item['ID']}
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ExpressionAttributeNames=expression_attribute_names,
        ReturnValues='ALL_NEW'  # Specify what values to return after the update
    )

    # Create a response dictionary
    response_dict = {
        "statusCode": 200,
        "body": json.dumps(response['Attributes'])  # Return the updated item
    }

    return response_dict