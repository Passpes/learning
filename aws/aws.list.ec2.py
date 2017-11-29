import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print (instance.id)
# ec2.instances.filter(InstanceIds=i-085b40b54a319eb2d).stop()
