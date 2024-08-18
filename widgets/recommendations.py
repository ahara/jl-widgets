import pandas as pd
import streamlit as st
from streamlit.logger import get_logger


logger = get_logger(__name__)

st.header("Rekomendowane laptopy")


@st.cache_data
def load_data():
    logger.info(f"Loaded data for: {st.query_params}")
    data_path = './data/laptop_recommendation.csv'
    _df = pd.read_csv(data_path)
    return _df


def print_laptop(laptop) -> st.container:
    c = st.container()
    col1, col2, col3 = c.columns(3)
    col1.image(laptop["url_image"])
    #col2.link_button(f'{laptop["name"]}', laptop["url_referal"], type='primary')
    col2.subheader(f'{laptop["name"]}')
    col3.link_button(f'Sprawdź ofertę', laptop["url_referal"], type='primary')
    c.markdown("---")

    return c


df = load_data()

for _, row in df.iterrows():
    print_laptop(row)
