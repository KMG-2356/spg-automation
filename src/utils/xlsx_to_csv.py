import os
import pandas as pd


def excel_to_csv(excel_file: str, output_dir: str = None) -> list:
    """Converts all sheets of an Excel file into individual CSV files.

    :param excel_file: Path to the source .xlsx file
    :param output_dir: Destination folder (defaults to the Excel file's folder)
    :return: A list of file paths to the generated CSVs
    """
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"Source file not found: {excel_file}")

    # Set default output directory if none provided
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(excel_file))

    os.makedirs(output_dir, exist_ok=True)
    generated_files = []

    try:
        # Load the Excel file without reading sheets into memory yet
        with pd.ExcelFile(excel_file) as xls:
            for sheet_name in xls.sheet_names:
                # Read individual sheet
                df = pd.read_excel(xls, sheet_name=sheet_name)

                # Clean sheet name for the filename (remove invalid characters)
                safe_sheet_name = "".join(
                    [
                        c
                        for c in sheet_name
                        if c.isalnum() or c in (" ", "_", "-")
                    ]
                ).strip()
                csv_filename = f"{safe_sheet_name}.csv"
                csv_filepath = os.path.join(output_dir, csv_filename)

                # Export to CSV
                # index=False prevents pandas from writing a column of row numbers (0, 1, 2...)
                df.to_csv(csv_filepath, index=False, encoding="utf-8")
                print(f"Successfully converted sheet [{sheet_name}] -> {csv_filepath}")
                generated_files.append(csv_filepath)

        return generated_files

    except Exception as e:
        raise RuntimeError(f"Conversion failed: {str(e)}")


# --- Example Usage ---
if __name__ == "__main__":
    # Replace with your actual file path
    source_excel = "src/data/TestData.xlsx"
    target_folder = "src/data/csv_exports"

    excel_to_csv(source_excel, target_folder)