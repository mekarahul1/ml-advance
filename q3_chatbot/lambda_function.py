import boto3

def build_response(message):
    return {
        "dialogAction":{
            "type":"Close",
            "fulfillmentState":"Fulfilled",
            "message":{
                "contentType":"PlainText",
                "content":message
            }
        }
    }

# DynamoDB table has two fields - question, answer
def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    
    question = event['currentIntent']['slots']['slotOne']
    question = question.lower()

    response = client.get_item(TableName='bookname', Key={'book':{'S':str(question)}})
    
    #print(context)
    message ="sorry book is not available "
    #message = "sorry book is not available "
    
    if 'Item' in response.keys():
        message = "Great !! book is available with us "
    else:
        message="sorry book is not available "
        
    return build_response(message)
