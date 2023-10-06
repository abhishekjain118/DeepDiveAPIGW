import boto3
import json

def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    # The name of your DynamoDB table
    table_name = 'CommentsOnMyResume'


    # Extract the item (row) ID from the request body
    item_id = event['ID']

    # Define the update expression and expression attribute values
    update_expression = []
    expression_attribute_values = {}
    expression_attribute_names = {}

    # Check if 'first name' is provided in the request and update it
    if 'fName' in event and event['fName']:
        update_expression.append('#FirstName = :FirstName')
        expression_attribute_names['#FirstName'] = 'FirstName'
        expression_attribute_values[':FirstName'] = {'S': event['fName']}

    # Check if 'Last Name' is provided in the request and update it
    if 'lName' in event and event['lName']:
        update_expression.append('#LastName = :LastName')
        expression_attribute_names['#LastName'] = 'LastName'
        expression_attribute_values[':LastName'] = {'S': event['lName']}
        
    # Check if 'comment' is provided in the request and update it
    if 'comment' in event and event['comment']:
        update_expression.append('#comment = :comment')
        expression_attribute_names['#comment'] = 'comment'
        expression_attribute_values[':comment'] = {'S': event['comment']}

    # Check if 'company' is provided in the request and update it
    if 'company' in event and event['company']:
        update_expression.append('#company = :company')
        expression_attribute_names['#company'] = 'company'
        expression_attribute_values[':company'] = {'S': event['company']}

    # Build the update expression
    print(update_expression)
    update_expression = ','.join(update_expression)
    update_expression = 'set '+update_expression
    print(update_expression)
    print(expression_attribute_names)

    # Update the item in the DynamoDB table
    response = dynamodb.update_item(
        TableName=table_name,
        Key={
            'ID': {'S': item_id}  # Assuming 'id' is a string attribute
        },
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues='ALL_NEW'
    )

    # Return the updated item as the Lambda function result
    return {
        'statusCode': 200,
        'body': json.dumps(response['Attributes'])
    }

