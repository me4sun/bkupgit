
##
script to backup the git repos

Requirements :

git in the PATH
azure.blob.storage module
	install with pip install azure-storage-blob (Please have the pip already)
azure blob storage connection string exported as  environment parameter something like 
 export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=xxxxxx;AccountKey=xxxxxxxxxxxxxxxxxxxxxxxxxx;EndpointSuffix=core.windows.net"
personal access token required  exported as environment variable and passed as parameter

Usage:
python backup_git.py -p <PAT> -r <repo name> -r <repo name> ....