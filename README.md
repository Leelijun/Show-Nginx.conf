# Show-Nginx.conf

#nginx path
/disk1/nginx
svn co svnurl /disk1/nginx

#svn
svn --version
svn，版本 1.7.14 (r1542130)

#install subversion-devel
yum install  subversion-devel

#install pygments
pip2.7 install pygments

# install pysvn
##pysvn-1.7.10.tar 
##tar -xvf pysvn-1.7.10.tar
##cd Source
##python setup.py configure
##make
##cd ../Tests
##make
##cd Source
##mkdir [YOUR PYTHON LIBDIR]/site-packages/pysvn
##cp pysvn/__init__.py [YOUR PYTHON LIBDIR]/site-packages/pysvn
cp pysvn/_pysvn*.so [YOUR PYTHON LIBDIR]/site-packages/pysvn


