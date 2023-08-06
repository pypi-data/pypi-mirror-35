#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# common help

import sys
import getopt

def usage():
    print 'usage: aws-opsworks [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
    print 'To see help text, you can run: \n' + \
          sys.argv[0] + ' --help \n' + \
          sys.argv[0] + ' [options] --help \n'
    print 'available options:\n - execute-recipes\n - update-custom-cookbooks\n - setup\n'

def execute_recipes_usage():
    print 'usage: \n' + \
        sys.argv[1] + ' --region [region] --stack [opsworks_stack_id] --layer [opsworks_layer_id] --instances [opsworks_layer_instance_count] --cookbook [cookbook]\n'


def update_custom_cookbooks_usage():
    print 'usage: \n' + \
        sys.argv[1] + ' --region [region] --stack [opsworks_stack_id] --layer [opsworks_layer_id] --instances [opsworks_layer_instance_count]\n'

def setup_usage():
    print 'usage: \n' + \
        sys.argv[1] + ' --region [region] --stack [opsworks_stack_id] --layer [opsworks_layer_id] --instances [opsworks_layer_instance_count]\n'

def output_summary():
    print "Summary: \n success instances: " + \
        str(success_count) + "\n skipped instances: " + \
        str(skipped_count) + "\n failed count: " + str(failed_count) + "\n"
    print "Check the deployment logs...\n"
    for logs in describe_deployment['Commands']:
        print logs['LogUrl']
