#! /bin/bash


repo_names=

base_path="/home/sandeep/work"
git_repos_path="${base_path}/code"
curd=`dirname $0`
uploadscript="${curd}/upload.sh"

ts=`date +"%Y-%m-%d-%H-%M"`


backup_dir="${base_path}/git_backups"
filename="${backup_dir}/git-repo-backup.${ts}.tgz"
logfile="${filename}.log"

#Make the backup directory if does not exist

mkdir -p ${backup_dir}

[[ "$?" -ne 0 ]] && echo "Can not make the directory, Please check permissions" && exit 1


tar  -czvf $filename "${git_repos_path}"	 > $logfile  2>&1


[[ "$?" -ne 0 ]] && echo "Could not create the backup file, Please check log" && exit 1


echo "Calling the script to upload the target file to Blob STorage"

 
source $uploadscript $filename

[[ "$?" -ne 0 ]] && echo "Could not upload the backup file, Please check log" && exit 1
