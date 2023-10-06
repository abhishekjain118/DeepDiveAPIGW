import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Get the ID to be deleted from the event
    id_to_delete = event.get('ID')

    # Ensure that the ID is not empty
    if not id_to_delete:
        return {
            "statusCode": 400,
            "body": json.dumps("ID is missing in the input event.")
        }

    try:
        # Delete the item from the DynamoDB table
        response = dynamodb.delete_item(
            TableName='CommentsOnMyResume',
            Key={
                'ID': {'S': id_to_delete}
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Item deleted successfully.")
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"An error occurred: {str(e)}")
        }
