#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# execute setup

import sys
import getopt
import boto3
import time
from common_functions import usage
from common_functions import setup_usage
from common_functions import output_summary

if sys.argv[1] == "setup":

    try:
        opts, args = getopt.getopt(sys.argv[2:], 'r:s:l:i:h', [
            'region=', 'stack=', 'layer=', 'instances=', 'help'
        ])
    except getopt.GetoptError:
        setup_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            setup_usage()
            sys.exit(2)
        elif opt in ('-r', '--region'):
            region = arg
        elif opt in ('-s', '--stack'):
            stack = arg
        elif opt in ('-l', '--layer'):
            layer = arg
        elif opt in ('-i', '--instances'):
            instances = arg
        else:
            setup_usage()
            sys.exit(2)

    #instances_lt = int(instances) + 1
    print "running setup..."
    # initiate boto3 client
    client = boto3.client('opsworks', region_name=region)
    # calling deployment to specified stack layer
    run_setup = client.create_deployment(
        StackId=stack,
        LayerIds=[
            layer,
        ],
        Command={
            'Name': 'setup'
        },
        Comment='automated setup job'
    )

    deploymentId = run_setup['DeploymentId']
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
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed count: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
        elif skipped_count == int(instances):
            print "Deployment skipped...\n"
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed count: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
        elif failed_count == int(instances):
            print "Deployment failed...\n"
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed count: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
        elif fail_skip_count == int(instances):
            print "Deployment failed and some of them skipped..."
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed count: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
    except Exception, e:
        print e
