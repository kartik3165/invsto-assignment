import pymysql
import pandas as pd
import sqlalchemy

db = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    database="Analysis"
)

def load_data():
    url = 'https://docs.google.com/spreadsheets/d/1-rIkEb94tZ69FvsjXnfkVETYu6rftF-8/export?format=csv'
    data = pd.read_csv(url)
    cursor = db.cursor()

    for _, row in data.iterrows():
        sql = """
            INSERT INTO ticker_data (datetime, instrument, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (row['datetime'], row['instrument'], row['open'], row['high'], row['low'], row['close'], row['volume'])
        cursor.execute(sql, values)

    db.commit()
    cursor.close()
    db.close()

def analysis():
    engine = sqlalchemy.create_engine("mysql+pymysql://root:admin@127.0.0.1/Analysis")
    query = "SELECT * FROM ticker_data ORDER BY datetime"
    data = pd.read_sql(query, engine)

    data['datetime'] = pd.to_datetime(data['datetime'])

    short_window = 10
    long_window = 30

    data['SMA_short'] = data['close'].rolling(window=short_window).mean()
    data['SMA_long'] = data['close'].rolling(window=long_window).mean()

    data['signal'] = 0
    data.loc[data['SMA_short'] > data['SMA_long'], 'signal'] = 1
    data.loc[data['SMA_short'] <= data['SMA_long'], 'signal'] = -1

    data['daily_return'] = data['close'].pct_change()
    data['strategy_return'] = data['signal'].shift(1) * data['daily_return']

    cumulative_strategy_return = (1 + data['strategy_return']).cumprod()
    cumulative_market_return = (1 + data['daily_return']).cumprod()

    print("Strategy Performance:")
    print(cumulative_strategy_return.tail())

while True:
    print('1. Add Data In DB\n2. Analysis Data')
    ch = int(input('Select Option : '))

    match ch:
        case 1:
            load_data()

        case 2:
            analysis()

        case _:
            print('Plz.. valid input')
