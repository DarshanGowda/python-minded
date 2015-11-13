__author__ = 'rdarshan'

"""
Automation script to push tag to remote

requires:
    1) git, os, sys, argparse
    2) your pwd should be your git repo

usage:
    tagRelease.py -h will show the required details to run this script
"""

from git import Repo
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='''Automation Tag Release Tool''',
                                 epilog="""Expects 3 command line args RemoteName, RemoteBranchName and TagName""")
parser.add_argument('RemoteName', type=str, help='remote name to pull Data/push new tag')
parser.add_argument('RemoteBranchName', type=str, help='remote branch name to pull data')
parser.add_argument('TagName', type=str, help='tag name to push to remote')
parser.parse_args()

remote_name, remote_branch, tag_name = sys.argv[1:]
repo_obj = Repo(os.getcwd())
git_ref = repo_obj.git
git_ref.pull(remote_name, remote_branch)
git_ref.tag(tag_name)
git_ref.push(remote_name, tag_name)

# ################# remove remote git tag #################
# git_ref.push(remote_name, ":"+tag_name)
# git_ref.tag('-d', tag_name)
# ################# remove remote git tag #################
