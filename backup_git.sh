#! /bin/bash


# Add name of the repos. Could be read from a file also

git_repos = "HelloWorld GoodbyeWorld"
git_repos_path = "/work/code/HelloWorld"

cur_dir = `dirname $0`
backup_dir = "${git_repos_path}/git_backups"

#Make the backup directory if does not exist

mkdir -p ${backup_dir}


for gr in ${git_repos}
do

	cp -prv $gr ${backup_dir}
done


echo "Backup completed"


