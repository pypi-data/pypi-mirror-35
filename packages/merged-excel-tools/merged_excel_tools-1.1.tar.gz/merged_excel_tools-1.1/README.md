# merged_excel_tools
读取合并单元格的工具类

这是用来读取特定格式(合并单元格)的Excel表格的工具类，格式如下
![table.png](https://s1.ax1x.com/2018/08/13/Pg8gH0.png)

## install
使用pip
```python
pip install merged_excel_tools
```
## 使用方法
```python
from merged_excel_tools import *
worksheet,ranges=getMergedList("example.xlsx")
for range in ranges:
    # 这是合并单元格的首
    start = getRowFromRange(range, 0)
    # 这是合并单元格的尾
    end = getRowFromRange(range, 1)
```

### 注意
使用openpyxl来读取excel表格
