#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# execute recipes

import sys
import getopt
import boto3
import time
from common_functions import usage
from common_functions import execute_recipes_usage
from common_functions import output_summary

if sys.argv[1] == "execute-recipes":

    try:
        opts, args = getopt.getopt(sys.argv[2:], 'r:s:l:i:c:h', [
            'region=', 'stack=', 'layer=', 'instances=', 'cookbook=', 'help'
        ])
    except getopt.GetoptError:
        execute_recipes_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            execute_recipes_usage()
            sys.exit(2)
        elif opt in ('-r', '--region'):
            region = arg
        elif opt in ('-s', '--stack'):
            stack = arg
        elif opt in ('-l', '--layer'):
            layer = arg
        elif opt in ('-i', '--instances'):
            instances = arg
        elif opt in ('-c', '--cookbook'):
            cookbook = arg
        else:
            execute_recipes_usage()
            sys.exit(2)

    #instances_lt = int(instances) + 1
    print "running execute_recipe with " + str(cookbook)
    # initiate boto3 client
    client = boto3.client('opsworks', region_name=region)
    # calling deployment to specified stack layer
    run_recipes = client.create_deployment(
        StackId=stack,
        LayerIds=[
            layer,
        ],
        Command={
            'Name': 'execute_recipes',
            'Args': {
                'recipes': [
                    cookbook,
                ]
            }
        },
        Comment='automated execute_recipes job'
    )

    deploymentId = run_recipes['DeploymentId']
    # sending describe command to get status"""  """
    describe_deployment = client.describe_commands(
        DeploymentId=deploymentId
    )

    try:
        success_count = 0
        while success_count == 0:
            print "Deployment not completed yet..waiting 10 seconds before send request back to aws..."
            time.sleep(10)
            describe_deployment = client.describe_commands(
                DeploymentId=deploymentId)
            success_count = str(describe_deployment).count("successful")
            skipped_count = str(describe_deployment).count("skipped")
            failed_count = str(describe_deployment).count("failed")
            if int(success_count) + int(skipped_count) == int(instances):
                success_count = int(instances)
            elif int(skipped_count) == int(instances):
                skipped_count = int(instances)
            elif int(failed_count) == int(instances):
                failed_count = int(instances)
            elif int(skipped_count) + int(failed_count) == int(instances):
                fail_skip_count = int(instances)
        if success_count == int(instances):
            print "Deployment completed...\n"
            output_summary()
        elif skipped_count == int(instances):
            print "Deployment skipped...\n"
            output_summary()
        elif failed_count == int(instances):
            print "Deployment failed...\n"
            output_summary()
        elif fail_skip_count == int(instances):
            print "Deployment failed and some of them skipped..."
            output_summary()
    except Exception, e:
        print e
