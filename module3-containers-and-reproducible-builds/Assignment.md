1. First installed nano to create/edit **Dockerfile**  
```$ apk add nano```  

2. Create a new directory nckflannery/lambdata  
```$ mkdir nckflannery```  
```$ cd nckflannery```  
```$ mkdir lambdata```  
```$ cd lambdatat```  

3. Once in the directory, create the file **Dockerfile**  
```$ nano Dockerfile```

4. Edit **Dockerfile** as follows:
```
FROM debian
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pandas && \
pip3 install -i https://test.pypi.org/simple/ Nckflannery-lambdata && \
python3 -c "import nckflannery; print('success')"
```  
5. Build the docker image  
```$ docker build . -t lambdata```  
6. Use some modules from the package  
```$ docker run -it lambdata /bin/bash```  
7. Testing module "is_null"
```
>>> a = pd.DataFrame([[1,2],[2,3,4,5],[2,4],[634,42,656,4]])
>>> a.head()
     0   1      2    3
0    1   2    NaN  NaN
1    2   3    4.0  5.0
2    2   4    NaN  NaN
3  634  42  656.0  4.0
>>> is_null(a)
       0      1      2      3
0  False  False   True   True
1  False  False  False  False
2  False  False   True   True
3  False  False  False  False
```
8. Testing module "iqr_outliers"  
```
>>> b = [1,2,4,5,4,5,6,67,3,34,5,6,346,6]
>>> iqr_outliers(b)
346 is a high outlier
List without outliers:
[1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 34, 67]
```
