from kirvin.clean import clean
from kirvin.load import load

data_raw = load()
data = clean(data_raw)
print(data)
