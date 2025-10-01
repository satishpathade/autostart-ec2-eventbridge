import boto3

def lambda_handler(event, context):
    # Initialize EC2 client
    ec2 = boto3.client('ec2', region_name='ap-south-1')  # change to your region
    
    # Replace with your instance IDs
    instance_ids = 'your-instanceId'  # add you id
    
    try:
        # Start the instance(s)
        response = ec2.start_instances(InstanceIds=instance_ids)
        
        return {
            'statusCode': 200,
            'body': f'Started instance(s): {instance_ids}',
            'response': response
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
