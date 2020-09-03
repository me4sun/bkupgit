#------------  script to backup git repos ----#

import os
import zipfile  as zf 
import logging as log
import argparse as argp 
import time
import urllib
import shutil


class gitclone:

    def clone(self,gitrepo):
        pass


def parse_args():
    """Parse and save command line arguments"""
    parser = argp.ArgumentParser()
    parser.add_argument("-pat", "--pat", required=True, help="Personal Access Token")
    parser.add_argument("-store", "--storage", required=False, help="Name of the Storage Account",default="sreaccount")
    parser.add_argument("-d", "--debug", action='store_true',help="Enable debug logs")
    parser.add_argument('-r','--repo', nargs='+',action='append',help='<Required Repo List one or more> ', required=True)
    args = parser.parse_args()
    return args



def check_pat_size(pat):
    """ Size of PAT should be 40 chars"""    
    if len(pat) != 40:
        log.debug("GitHub Personal access token size not right, need 40 bytes")
        log.debug("Exiting.")
        exit()
    else:
        return 1


def main():
    args = parse_args()

    log.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=log.DEBUG)
    repolist=args.repo

    repo=["first","second"]
    for list in repo:
        print (list)

    if check_pat_size(args.pat):
        pass
    

if __name__ == '__main__':
    main()


