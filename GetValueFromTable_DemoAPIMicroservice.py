import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')

    # The name of your DynamoDB table
    table_name = 'CommentsOnMyResume'

    all_records = []
    try:
        # Scan the entire table to fetch all rows
        response = dynamodb.scan(TableName=table_name)

        # Extract the items (rows) from the response
        # Add the records from the initial response to the list
        all_records.extend(response.get('Items', []))
        #items = response.get('Items', [])

        while 'LastEvaluatedKey' in response:
            response = dynamodb.scan(
            TableName=table_name,
            # Use the LastEvaluatedKey to get the next page of results
            ExclusiveStartKey=response['LastEvaluatedKey']
            )
            all_records.extend(response.get('Items', []))
    
        # Return the items as the Lambda function result
        return {
            'statusCode': 200,
            'body': all_records
        }
    except Exception as e:
        # Handle any errors
        return {
            'statusCode': 500,
            'body': str(e)
        }





