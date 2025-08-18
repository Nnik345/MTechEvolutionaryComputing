import pandas as pd
import numpy as np
from statistics import mode, StatisticsError
from collections import Counter

def analyze_numerical_data(data, column_name):
    values = data[column_name].dropna()
    
    mean_val = values.mean()
    median_val = values.median()
    
    try:
        mode_val = mode(values)
    except StatisticsError:
        mode_val = values.mode().iloc[0] if not values.mode().empty else "No unique mode"
    
    return mean_val, median_val, mode_val

def main():
    try:
        df = pd.read_csv('Foundations of Data Engineering\Ex 6\sample_people.csv')
        print("Data loaded successfully!")
        print(f"Dataset shape: {df.shape}")
        print("\nFirst few rows of the data:")
        print(df.head())
        print("\n" + "="*50)
        
        columns_to_analyze = ['height', 'weight', 'age', 'salary']
        
        print("STATISTICAL ANALYSIS")
        print("="*50)
        
        for column in columns_to_analyze:
            print(f"\n{column.upper()} ANALYSIS:")
            print("-" * 30)
            
            mean_val, median_val, mode_val = analyze_numerical_data(df, column)
            
            print(f"Mean: {mean_val:.2f}")
            print(f"Median: {median_val:.2f}")
            print(f"Mode: {mode_val}")
            
            print(f"Min: {df[column].min()}")
            print(f"Max: {df[column].max()}")
            print(f"Standard Deviation: {df[column].std():.2f}")
        
        print("\n" + "="*50)
        print("SUMMARY:")
        print("="*50)
        
        summary_data = []
        for column in columns_to_analyze:
            mean_val, median_val, mode_val = analyze_numerical_data(df, column)
            summary_data.append({
                'Column': column.capitalize(),
                'Mean': f"{mean_val:.2f}",
                'Median': f"{median_val:.2f}",
                'Mode': str(mode_val),
                'Min': df[column].min(),
                'Max': df[column].max()
            })
        
        summary_df = pd.DataFrame(summary_data)
        print(summary_df.to_string(index=False))
        
    except FileNotFoundError:
        print("Error: sample_people.csv file not found!")
        print("Make sure the file is in the same directory as this script.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 