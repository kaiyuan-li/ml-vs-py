# comparing timestamp loading time between ML and Python

## create a sqlite table and read it into python
Create the database, you may need to install necessary python libraries such as `pandas`

```
pip3 install pandas
```

Then run `write.py` in terminal to create the database
```
python3 write.py
```

Now read the database by loading it into pandas dataframe.
```
python3 read.py
```

Notice the output is
```
Execution time: 0.38239097595214844 seconds
Type of element:
<class 'pandas._libs.tslibs.timestamps.Timestamp'>

Size of DataFrame:
Number of rows: 1000000
```

Pandas spent 0.38s to read 1M rows of timestamp and converted them into datetime.

## Read the same table in ML and convert timestamp to datetime
```
>> main
Elapsed time is 393.848690 seconds.
```

Notice the speed of python is 1000x comparing to ML... And the Matlab solution is not scalable at all.

## Reference

Environment and version

```
>> % Use the ver function to get version information
matlabVersion = ver;

% Extract and display MATLAB version number
disp(['MATLAB Version: ' matlabVersion(1).Version]);
MATLAB Version: 23.2
```

I'm running it on Mac M3 Pro 32G memory.