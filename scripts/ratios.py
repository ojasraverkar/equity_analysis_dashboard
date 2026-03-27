import pandas as pd

ratios = {}

def calculate_ratios(income_stmt, balance_sheet):
    
    latest_income = income_stmt.iloc[:, 0]
    net_income = latest_income.get('Net Income', None)
    revenue = latest_income.get('Total Revenue', None)

    if net_income is not None and revenue is not None and revenue != 0:
        ratios['Profit Margin'] = net_income / revenue
    else:
        ratios['Profit Margin'] = None

    latest_balance = balance_sheet.iloc[:, 0]
    total_assets = latest_balance.get('Total Assets', None)
    total_liabilities = latest_balance.get('Total Liabilities Net Minority Interest', None)
    total_equity = latest_balance.get('Stockholders Equity', None)
    total_debt = latest_balance.get('Total Debt', None)
    
    if total_liabilities is not None and total_equity is not None and total_equity != 0:
        ratios['Debt to Equity'] = total_debt / total_equity
    else:
        ratios['Debt to Equity'] = None
        
    if net_income is not None and total_equity is not None and total_equity != 0:
        ratios['ROE'] = net_income / total_equity
    else:
        ratios['ROE'] = None

    return ratios

def get_pe_ratio(info):
    return info.get('trailingPE', None)
