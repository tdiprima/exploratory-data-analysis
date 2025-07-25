## Arrow serialization error

```sh
Serialization of dataframe to Arrow table was unsuccessful due to:
("Could not convert dtype('O') with type numpy.dtypes.ObjectDType:
did not recognize Python value type when inferring an Arrow data type",
'Conversion failed for column 0 with type object').
Applying automatic fixes for column types to make the dataframe Arrow-compatible.
```

This error occurs because Streamlit has trouble serializing certain pandas data types to Arrow format for display. The issue is likely with the 'Name' column (column 0) which contains string data that pandas has inferred as a generic 'object' dtype.

Key changes to fix the Arrow serialization error:

1. **Explicit type conversion**: Convert all 'object' dtype columns to 'string' type using `df[col].astype('string')`. This makes them Arrow-compatible.

2. **Improved data type display**: Instead of showing raw dtypes, create a clean DataFrame to display column types.

3. **Enhanced missing values display**: Added both count and percentage of missing values in a formatted table.

4. **Conditional statistical summary**: Only show statistical summary if numerical columns exist.

5. **Additional insights**: Added a section showing unique values for categorical columns.

The main fix is the type conversion loop that explicitly converts object columns to string type, which resolves the Arrow serialization issue. This approach maintains all the original functionality while making the app more robust and informative.

<br>
