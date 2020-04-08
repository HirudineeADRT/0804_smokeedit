import boto3
sqs = boto3.client("sqs")

def handler(event, context):

    try:
        data = sqs.receive_message(
            QueueUrl="https://sqs.{}.amazonaws.com/{}/hiru-test".format(environ["AWS_REGION"], environ["SIGMA_AWS_ACC_ID"]),
            MaxNumberOfMessages=1,
            VisibilityTimeout=30,
            WaitTimeSeconds=0,
            AttributeNames=["All"]
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    try:
        data = sqs.delete_message(
            QueueUrl="https://sqs.{}.amazonaws.com/{}/hiru-test".format(environ["AWS_REGION"], environ["SIGMA_AWS_ACC_ID"]),
            ReceiptHandle="test"
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
