#------------  script to backup git repos to azure blob storage ----#

import os
import logging as log
import argparse as argp 
import datetime
import shutil
import tempfile 
import subprocess
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def parse_args():
    """Parse and save command line arguments"""
    parser = argp.ArgumentParser()
    parser.add_argument("-pat", "--pat", required=False, help="Personal Access Token")
    parser.add_argument("-user", "--username", required=False,default="me4sun",help="Personal Access Token")
    parser.add_argument("-store", "--storage", required=False, help="Name of the Storage Account",default="sreaccount")
    parser.add_argument("-d", "--debug", action='store_true',help="Enable debug logs")
    parser.add_argument('-r','--repo', nargs='+',action='append',help='<Required Repo List one or more> ', required=True)
    args = parser.parse_args()
    return args


def upload_blob(zipfile,container_name="gitbackups"):
    
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=zipfile)
        log.info("Uploading to Azure Storage as blob: " + zipfile)

        with open(zipfile, "rb") as data:
            blob_client.upload_blob(data)

    except Exception as ex:
        log.debug('Exception:'+ str(ex))

    return 1
        
        


def check_pat_size(pat):
    """ Size of PAT should be 40 chars"""    
    if len(pat) != 40:
        log.debug("GitHub Personal access token size not right, need 40 bytes")
        log.debug("Exiting.")
        exit()
    else:
        return 1


def deltmp(tmpd):
    for root, dirs, files in os.walk(tmpd):
        for file in files:
            print(os.path.join(root, file))
            os.remove(os.path.join(root, file))



def clone_repos(user,pat,rl,tmpd):
    """ Clones the repos to a tmp folder.  """
    numcloned=0
      
    for repo in rl:
        git_url=r'https://{}@github.com/{}/{}'.format(pat,user,repo[0])
        gcmd=r'git clone {}'.format(git_url)
        os.chdir(tmpd)
        log.info("Attempting to clone " + repo[0])
        p1 = subprocess.Popen(gcmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p1.wait()
        if p1.returncode == 0:
            log.info("Successfully Cloned: " + repo[0])
            numcloned +=1
        else:
            log.debug("Does not look like we could Clone successfully " + repo[0] + ". Please check name and permissions etc")
            log.debug(p1.communicate()[1].decode())
        
    return numcloned

            

def main():
    args = parse_args()

    log.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=log.DEBUG)
    repolist=args.repo

    if check_pat_size(args.pat):
        log.info("Analysing repo Names")       
    
    
    tmpd = tempfile.mkdtemp()

    repos_cloned=clone_repos(args.username,args.pat,repolist,tmpd)

    log.info("Repos able to clone :" + str(repos_cloned) )
    if repos_cloned == 0:
        log.debug("Nothing to zip, check config please")
        exit -1
    
    tmpzipdir=tempfile.mkdtemp()
    ffmt=datetime.datetime.utcnow().strftime('%a-%d-%b-%Y-%H-%M-%S')

    repo_zipfile = 'repo_back-'+ffmt

    os.chdir(tmpzipdir)
   
    if( shutil.make_archive(repo_zipfile, 'zip', tmpd) ):
        log.info("Zipped repos successfully")
    else:
        log.debug ("could not create archive of repos.")

    zipfile_with_path=os.path.abspath(repo_zipfile+".zip")
    log.info("uploading the file " + zipfile_with_path)
    
    if(upload_blob(zipfile_with_path)):
        log.info("Successfully uploaded ZipFile")
    else:
        log.debug("Could not upload zip file, check permissions")

## Clean up 
    log.info("Cleaning Up tmp files and folders")
    deltmp(zipfile_with_path)
    deltmp(tmpd)
    
# End of Main


if __name__ == '__main__':
    main()
    

