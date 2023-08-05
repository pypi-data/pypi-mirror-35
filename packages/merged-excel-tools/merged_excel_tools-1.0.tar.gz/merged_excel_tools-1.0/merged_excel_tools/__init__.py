def getMergedList(xls_name):
    from openpyxl import load_workbook
    import re
    wb = load_workbook(filename=xls_name)
    ws = wb.active
    ranges = ws.merged_cell_ranges
    myRanges = [x for x in ranges if re.match("A[0-9]+:A[0-9]+", x)]
    myRanges.sort(key=lambda x: getRowFromRange(x, 0))
    return myRanges


def getRowFromRange(range, index):
    return int(range.split(':')[index][1:])
