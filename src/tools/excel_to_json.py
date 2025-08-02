# -*- coding: utf-8 -*-
"""
Batch read Excel files from a specified folder, map columns and export to JSON
python export_to_json.py /path/to/your/folder -o result.json
"""
import os
import json
import pandas as pd
import numpy as np  # Import numpy for handling NaN values

# Excel file path
excel_file_path = 'path/to/your/excel/file.xlsx'
# Output JSON file path
output_json_path = 'path/to/your/output/file.json'

def collect_data():
    # Column mapping: column name -> English key
    col_map = {
        'Serial Number': 'serial_number',
        'Not a Math Problem': 'not_math_problem',
        'Grammar, Word, or Format Error': 'grammar_or_format_error',
        'Minimal Condition Error': 'minimal_condition_error',
        'Condition Conflict Error': 'pi_pj_condition_error',
        'Insufficient Conditions': 'insufficient_condition',
        'Correct Problem': 'correct_problem',
        'Remarks': 'remarks'
    }
    expected_columns = list(col_map.values())
    
    # Specify second row as header
    df = pd.read_excel(excel_file_path, header=1)
    df = df.rename(columns=col_map)
    
    # Check if all expected columns exist
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        print(f"File {excel_file_path} is missing the following columns: {missing_columns}")
    
    # Keep only mapped columns
    df = df[list(col_map.values())]
    records = df.to_dict(orient='records')
    
    # Handle NaN values, replace with null
    for record in records:
        for key, value in record.items():
            if isinstance(value, float) and np.isnan(value):
                record[key] = None
    
    return records

data = collect_data()
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'Generated {output_json_path} with {len(data)} records.')