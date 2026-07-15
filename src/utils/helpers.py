import re
from typing import Any
from openpyxl import load_workbook

def to_float(value: str) -> str:
    return f"{float(value):.2f}"

def get_num(text: str) -> str: 
    match = re.search(r"[\d,]+(?:\.\d+)?", text)
    if match:
        return match.group().replace(",", "")
    else:
        raise ValueError(f"Could not find any numeric value in text: '{text}'")

def write_excel_cell(
    file_name: str,
    sheet_name: str,
    row_number: int | None = None,
    row_value: Any = None,
    column_name: str = "",
    data: Any = None,
) -> None:
    """
    Update a single cell in an Excel file.

    Args:
        file_name: Path to the Excel file.
        sheet_name: Name of the worksheet to update.
        row_number: 1-based row number to update. If provided, this is used directly.
        row_value: Value used to find the row when row_number is not provided.
        column_name: Column name used to locate the target row when row_number is not provided.
        data: Value to write into the target cell.
    """
    workbook = load_workbook(file_name)
    sheet = workbook[sheet_name]

    if row_number is not None:
        if row_number < 1:
            raise ValueError("row_number must be 1 or greater.")
        target_row = row_number
    else:
        if row_value is None or not column_name:
            raise ValueError("Provide either row_number or both row_value and column_name.")

        headers = [cell.value for cell in sheet[1]]
        if column_name not in headers:
            raise ValueError(f"Column '{column_name}' was not found in sheet '{sheet_name}'.")

        target_column_index = headers.index(column_name) + 1

        for row in sheet.iter_rows(min_row=2, values_only=False):
            if row[0].value == row_value:
                target_row = row[1].row
                break
        else:
            raise ValueError(f"Row with {column_name}='{row_value}' was not found in sheet '{sheet_name}'.")

    if not column_name:
        raise ValueError("column_name is required when using row_number.")

    headers = [cell.value for cell in sheet[1]]
    if column_name not in headers:
        raise ValueError(f"Column '{column_name}' was not found in sheet '{sheet_name}'.")

    target_column_index = headers.index(column_name) + 1
    sheet.cell(row=target_row, column=target_column_index).value = data
    workbook.save(file_name)
    workbook.close()