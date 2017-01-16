>https://robots.thoughtbot.com/the-magic-behind-configure-make-make-install

## sqlite3  
(yum list | grep -i sqlite)  
(yum list | grep sqlite | grep dev)  

yum install sqlite-devel  
yum install sqlite3-devel  

## python  
yum install python  
yum install python-dev  

## python3(source)  
./configure **--enable-loadable-sqlite-extensions CFLAGS=-fPIC --enable-shared**  
make  
make install  
**if there:**     
`error while loading shared libraries: libpython3.5m.so.1.0: cannot open shared object file: No such file or directory`  
\>LD_LIBRARY_PATH=MAKE_PATH  

## apache(source)  
(yum install httpd) 

**APR**  
./configure **--prefix**=APR_PATH  
make && make install  

**APR-util**  
./configure **--prefix**=APR_UTIL_PATH  
make && make install  

**apache**  
./configure **--prefix**=APACHE_PATH **--with-apr**=APR_PATH **--with-apr-util**=APR_UTIL_PATH  
make  
make install  

## mod_wsgi(source)  
./configure **--with-apxs**=$APACHE_PATH/bin/apxs **--with-python**=$PYTHON_PATH/bin/python  
make  
make install  
