# Coleta de dados de ações do IBOV
import yfinance as yf

def get_ibov_data(start, end):
    return yf.download("^BVSP", start=start, end=end)
