import pandas as pd

ratios = {}

def calculate_ratios(income_stmt, balance_sheet):
    
    latest_income = income_stmt.iloc[:, 0]
    net_income = latest_income.get('Net income', None)
    revenue = latest_income.get('Total evenue', None)
    ratios['Profit Margin'] = net_income / revenue

    latest_balance = balance_sheet.iloc[:, 0]
    total_assets = latest_balance.get('Total assets', None)
    total_liabilities = latest_balance.get('Total laibilities', None)
    total_equity = latest_balance.get('Total equity', None)
    ratios['Debt to Equity'] = total_liabilities / total_equity
    ratios['ROE'] = net_income / total_equity

    return ratios

def get_pe_ratio(info):
    return info.get('trailingPE', None)

