# Classification_rawdata



**file_csv** : input/part1.csv<br>

no, offset, type

**file_raw** : input/raw_data.raw<br>

binary file

<br>

**download raw data file -> ./input/**

https://drive.google.com/open?id=18eUlrHz3ll03WdgVzhFPcCg9W9ETWCdk

<br>

1. split raw file with offset and save at input/data

   input/data/0, input/data/1, … , input/data/26399

   <br>

2. make dataframe to use at train

   add byte frequency / byte data

   <br>

3. CNN Model = byte data -> Conv1D

   <br>

4. FNN Model = CNN Model.output + byte frequency input

   <br>

5. Classifiaction with K-fold and save model

   <br>

6. Check Confusion matrix