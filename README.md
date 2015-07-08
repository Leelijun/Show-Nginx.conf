# Show-Nginx.conf

###nginx path
/disk1/nginx<br>
svn co svnurl /disk1/nginx<br>

###svn
svn --version
svn，版本 1.7.14 (r1542130)

###install subversion-devel
yum install  subversion-devel

###install pygments
pip2.7 install pygments

### install pysvn
pysvn-1.7.10.tar <br>
tar -xvf pysvn-1.7.10.tar<br>
cd Source<br>
python setup.py configure<br>
make<br>
cd ../Tests<br>
make<br>
cd Source<br>
mkdir [YOUR PYTHON LIBDIR]/site-packages/pysvn<br>

cp pysvn/__init__.py [YOUR PYTHON LIBDIR]/site-packages/pysvn<br>
cp pysvn/_pysvn*.so [YOUR PYTHON LIBDIR]/site-packages/pysvn<br>


