# DFAnalyzer 


DFAnalyzer Python is a Python package for data analysis, built on top of the popular DFAnalyzer for Excel. It provides a powerful set of tools for importing, exploring, cleaning, transforming, and visualizing data. It also offers features such as filtering, sorting, grouping, and performing calculations on data. DFAnalyzer Python is designed to enable users to quickly and easily analyze large amounts of data and **extract meaningful insights.**

* Find details & insight about each columns.
* Easy to perform cycles over pyspark.
* Percentage stats around NaN , Blank Values, Null Values.
* Describes datatypes of Pyspark Dataframe.
* Help in POC of data.



## Who Should use DFAnalyser

* Developers working with bigdata
* Developers using pyspark in the Data exploration.
* Developers who needs to do poc over raw data.




## Usage

### PySpark 

You can install the DFAnalyzer package using the pip command. To install DFAnalyzer, open a terminal window and type: pip install dfanalyzer. Once the installation is complete, you can start using DFAnalyzer with Python.

1. Install the preset:

    ```sh
    pip install dfanalyzer
    ```

2. Import it:

    ```diff
    import DFAnalyzer as dfa
    ```

3. Use it on existing pyspark dataframe:

    ```python
      #[isHavingNullData,%NullData,isHavingNanValues,%NanValues,isHavingBlankValues,%BlankValues,DataType]
      options=[1,1,1,1,1,1,1]#flags of what all kind of analysis you need
      dfa.analyze(df,options)

    ```
>More is about to come. Stay tuned.