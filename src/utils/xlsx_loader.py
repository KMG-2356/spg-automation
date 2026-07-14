import pandas as pd
import openpyxl
from typing import List, Dict, Any

def get_test_data(file_path: str, test_case_id: str) -> Dict[str, List[Dict[str, Any]]]:
    """
    Dynamically loads test data for a given test_case_id across sheets,
    grouping records under their corresponding sheet names as dictionary keys.
    
    Structure:
    {
        'MasterSheet': [{'Test Case No': 'TS-01-01', 'Creds': 'python'}],
        'summary': [{'Test Case No': 'TS-01-01', 'transaction_type': 'Quote'}]
    }
    """
    try:
        structured_data: Dict[str, List[Dict[str, Any]]] = {}
        
        with pd.ExcelFile(file_path) as xls:
            wb = openpyxl.load_workbook(file_path)
            sheet_names = [s.title for s in wb.worksheets if s.sheet_state == "visible"]
            if not sheet_names:
                raise ValueError("The provided Excel file has no sheets.")
            
            master_sheet_name = sheet_names[0]
            df_master = pd.read_excel(xls, sheet_name=master_sheet_name, dtype=str)
            
            if df_master.empty:
                print(f"Warning: The master sheet '{master_sheet_name}' is empty.")
                return {}
                
            id_column_name = df_master.columns[0]
            
            filtered_master = df_master[df_master[id_column_name] == test_case_id].copy()
            if filtered_master.empty:
                print(f"Warning: '{test_case_id}' not found in master sheet '{master_sheet_name}'.")
                return {}
                return {}
            
            filtered_master = filtered_master.fillna("")
            structured_data[master_sheet_name] = filtered_master.to_dict(orient='records')
            
            for sheet_name in sheet_names[1:]:
                df_relational = pd.read_excel(xls, sheet_name=sheet_name, dtype=str)
                
                if id_column_name in df_relational.columns:
                    filtered_relational = df_relational[df_relational[id_column_name] == test_case_id].copy()
                    
                    if not filtered_relational.empty:
                        filtered_relational = filtered_relational.fillna("")
                        structured_data[sheet_name] = filtered_relational.to_dict(orient='records')
            
            return structured_data

    except Exception as e:
        raise RuntimeError(f"Failed to dynamically parse nested Excel dataset for {test_case_id}: {str(e)}")
    
if __name__ == "__main__":
    file_path = 'src/data/TestData.xlsx'
    test_id = 'TS-01-01'
    data = get_test_data(file_path, test_id)
    print(data['Locations'][0]['ZipCode'])
