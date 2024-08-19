import pandas as pd
import streamlit as st
from streamlit.logger import get_logger


logger = get_logger(__name__)
logger.info(f"Loaded data for: {st.query_params}")


@st.cache_data
def load_data():
    data_path = './data/laptop_recommendation.csv'
    _df = pd.read_csv(data_path)
    return _df


def filter_data_with_kv(d, key, accepted_values):
    _df = d.copy()
    value = st.query_params.get(key, None)
    if value in accepted_values:
        _df = _df.query(f"{key} == @value")
        print(_df)

    return _df


def filter_data_with_query_params(d):
    _df = d.copy()
    _df = filter_data_with_kv(_df, 'price_range', ('low', 'mid', 'high'))
    _df = filter_data_with_kv(_df, 'has_gpu', ('y', 'n'))
    _df = filter_data_with_kv(_df, 'is_apple', ('y', 'n'))
    _df = filter_data_with_kv(_df, 'laptop_set', ('s1', 's2', 's3'))

    return _df


def print_laptop(laptop) -> st.container:
    c = st.container()
    col1, col2 = c.columns(spec=[0.3, 0.7])
    col1.image(laptop["url_image"])
    col2.subheader(f'{laptop["name"]}')
    col2.link_button(f'Sprawdź ofertę', laptop["url_referal"], type='primary')
    c.markdown("---")

    return c


df = load_data()
df = filter_data_with_query_params(df)

for _, row in df.iterrows():
    print_laptop(row)
