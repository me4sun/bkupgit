FROM ubuntu 
RUN mkdir -p /backup
ADD /home/sandeep/work/git_backups    /backup
ADD /home/sandeep/work/git_backups/git-repo-backup.2020-09-02-16-39.tgz    /backup

RUN  tar -zvf /backup/git-repo-backup.2020-09-02-16-39.tgz -C /backup  
RUN  find /backup -name 'README' -exec cat {} \;


