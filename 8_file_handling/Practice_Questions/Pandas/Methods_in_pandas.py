'''Functions and Methods in Pandas Library.'''

#pd.Series([1, 2, 3]) -> gives a series 
#pd.Series([1,2,3]).name = 'something' -> if printed, show values with name of series
#indexing as it is
#series.values.base -> prints only the values in series, base->copy()->none
#series.index -> prints the range of indexes (0, 1, 2, ...)
#series.index = {'ind1', 'ind2', 'ind3'...} -> creates indexes for the the values
#series['index_name(ind1)'] -> prints the value corresponding to the index
#series.iloc['index(3/-1/4/-3/0)'] -> prints the value at given index
#series.iloc[0: 5] -> prints the slice of value from 0 to 5
#series > 20 -> boolean selection
#df=pd.DataFrame({'col1': ['something'], 'col2': ['anything']}, columns: ['col1', 'col2']) -> dataframe structure
#df.values -> values print
#df.index -> rangeindex print (row, col)
#df.info() -> print all info fo df
#df.size -> prints size of df
#df.shape -> prints shape of df
#df.describe() -> prints all necessaryopps for df
#df.dtype() -> prints element's type and space
#df.value_counts() -> total number of values
#df.sort_index(ascending=False) -> sorts index in desce...order
#df.sort_values('column_name', ascending=False) -> sorts column values ...
#df.groupby('col_name') -> groups data accroding to that col
#df.get_group('col_value') -> prints all the row data associated with col_value
#df.groupby('col_name')['col1', 'col2'].sum()/.mean()/etc
#pd.to_datatime(series_name) -> converts object into .datetime obj
#pd.DatetimeIndex(series_name).year/.month/.day -> extract anything
#df_1.merge(df_2, on='common_col_name') -> merges two dfs using same col
#save csv file:
#resultdf=merged_df........make it proper
#resultdf.to_csv('result.csv', index=False) -> saved file
#df.loc['index'] -> prints the value at index
#df.at['index', 'col_name'] -> prints the value on ....
#df.drop(['row_name']) -> drop by row(immutable)
#df.drop(columns=['col_name']) -> drop by col(immutable)
#df.read_csv('file_name', header=None) -> reads csv file with no header
#df.head() and df.tail() -> first 5 and last 5
#df.set_index('col_name', inplace=True) -> col becomes index of df in original
#pd.options.display.max_rows -> max rows
#pd.isnull(series) or pd.isna(series) -> true for np.nan or None present, .sum() will give total...
#pd.notnull(series) or pd.notna(series) -> false of np.nan or None present, .sum() will give total...
#df.dropna(how='any'/'all' or thresh=num) -> drops all the values which are not null
#df.fillna(num/'str') -> fill the null value
#df.fillna(method='ffill'/'bfill') -> fill the null value based on front and back value
#df.col_name.unique() -> prints the unique values only
#df.col_name.value_counts() -> counts values
#df.replace({ 'col': { 'oe':'ne', 'oe':'ne' } }) -> replaces elements with new one
#df.duplicated(keep='last'/'first'/False) -> true for duplicate values
#df.drop_duplicates(keep='last'/'first'/False, subset='col_name') -> drops for duplicate values
#df.col_name.str.split('_', expand=True) -> splits value of col into str by '_' and give separate col to each
#df.col_name.str.contains(\'something') -> true if 'something' present
#df.col_name.str.strip() -> finds space btw letters
#df.col_name.str.replace(' ', '') -> replaced space with non space

#------------------------------------------------------------------------------------------------------------------#
