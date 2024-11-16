from pandas import DataFrame

from app.stocks import format_usd, fetch_stocks_csv

def test_usd_formatting():
    assert format_usd(12.5) == "$12.50"
    assert format_usd(1.111) == "$1.11"
    assert format_usd(100) == "$100.00"

def test_stock_data_fetching():

    df = fetch_stocks_csv("SPOT")
    assert isinstance(df, DataFrame)
    assert df.columns.tolist() == ["timestamp", "open", "high", "low", "close", "adjusted_close", "volume", "dividend_amount", "split_coefficient"]
    assert len(df) > 1500

    earliest = df.iloc[-1]
    assert earliest["timestamp"] == '2018-04-03'
    assert earliest["adjusted_close"] == 149.01