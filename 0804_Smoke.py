import boto3
s3 = boto3.client("s3")

def handler(event, context):
    print(event)
    try:
        data = s3.list_objects(
            Bucket="as2-test-lahiru",
            MaxKeys=10
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
