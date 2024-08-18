import pandas as pd
import streamlit as st

st.header("Rekomendowane laptopy")


@st.cache_data
def load_data():
    data_path = './data/laptop_recommendation.csv'
    _df = pd.read_csv(data_path)
    return _df


def print_laptop(laptop) -> st.container:
    c = st.container()
    col1, col2 = c.columns(2)
    col1.image(laptop["url_image"])
    col2.link_button(f'{laptop["name"]}', laptop["url_referal"], type='primary')
    c.markdown("---")

    return c


df = load_data()

for _, row in df.iterrows():
    print_laptop(row)

# st.markdown(st.query_params)
# referrer

from streamlit.logger import get_logger

logger = get_logger(__name__)

logger.info(st.query_params)