Create Excel files from Dataframes or dictionaries.

###Features

* Built around Xlsxwriter and Pandas.

* Create Excel worksheets using either dictionaries or dataframes.

* Worksheet columns are automatically sized.

* Attractive default style.

###Create an Excel object

```python
from cheesefactory-Excel import Excel

excel = Excel(
    output_file='my_excel.xlsx'
)
```

`output_file` (str): The path and name of the Excel file to create.

###Create a worksheet using a dictionary or Pandas Dataframe

```python
excel.create_worksheet(
    worksheet_name='Sheet1',
    content='my_content',
    header='header_data'
)
```

`worksheet_name` (str): The worksheet name.  It's limited to 31 characters.  Default = `'Worksheet'`

`content` (dict or pd.Dataframe): A dictionary or dataframe of the worksheet's content.

`header` (List[str]):  The worksheet's header.  Default = `None`

###Write the Excel file

```python
excel.close()
```
