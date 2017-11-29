import boto3
ids =  ['i-085b40b54a319eb2d']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds=ids).stop()
