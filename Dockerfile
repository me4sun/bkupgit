FROM alpine 

COPY repo_back-Fri-04-Sep-2020-04-30-09.zip ./

RUN  unzip -qq ./repo_back-Fri-04-Sep-2020-04-30-09.zip

RUN  find ./HelloWorld  -iname 'README*' -exec cat {} \;
RUN  find ./GoodbyeWorld -iname 'README*' -exec cat {} \;

