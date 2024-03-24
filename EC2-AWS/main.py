import boto3, random, paramiko, time
from secrets import access_key, secret_key

region = 'eu-north-1'

ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)


response = ec2.run_instances(
    ImageId='ami-0914547665e6a707c',
    InstanceType='t3.micro',
    KeyName='Step21',
    MinCount=1,
    MaxCount=1,
    IamInstanceProfile={
        'Name': 'PYTHON'
    },
    SecurityGroups=[
        'launch-wizard-1'
    ],
    
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Bublik-' + str(random.randint(1, 100))
                }
            ]
        }
    ]
)


instance_id = response['Instances'][0]['InstanceId']

time.sleep(5)
public_ip = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0].get('PublicIpAddress')

print("Pub IP:", public_ip)

time.sleep(20)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=public_ip, port=22, username="ubuntu", key_filename="Step21.pem")
stdin, stdout, stderr = ssh_client.exec_command("sudo apt update && sudo apt install awscli apache2 -y && sudo aws s3 cp s3://voutuk/site/sign-in/ /var/www/html/ --recursive")

for line in stdout:
    print(line.strip('\n'))

ssh_client.close()
