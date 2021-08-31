import streamlit as st
import pandas as pd
import numpy as np



@st.cache
def load_data(file_name, nrows=None):

    data = pd.read_csv(file_name, nrows=nrows)
    data.fillna(inplace=True, method='ffill')
    return data

def app():
    st.title('Display your data')
    st.write("Upload your dataset (a CSV file), and select how to display all its features.")
    col1, col2 = st.columns((3, 2))

    file_name = col1.file_uploader("Upload your dataset in csv or txt format", type=['txt', 'csv'])
    max_rows = col2.number_input('Select the maximum number of rows to use', format='%i', min_value=0, max_value=None)

    if max_rows is not None and max_rows > 0 and file_name is not None:
        # Load 10,000 rows of data into the dataframe.
        data = load_data(file_name, max_rows)
        columns = data.columns.values

        st.subheader('Raw data')
        st.write(data.head(10))
        chart_type = st.selectbox('Select a visualization', ['Bar chart', 'Line chart', 'Map'])

        if chart_type == 'Bar chart':
            col1, col2 = st.columns((4, 1))

            col = col1.selectbox('Select a feature to display', columns)
            density = col2.checkbox('Density')

            if st.button('Display bar chart'):
                if data.dtypes[col] == float:
                    hist, bin_edges = np.histogram(data[col], density=density)
                    keys = [str([round(bin_edges[i], 2), round(bin_edges[i+1], 2)]) for i in range(len(bin_edges)-1)]
                    description = f'% of {col} within range' if density else f'Number of {col} within range'
                    display = pd.DataFrame({
                        col: keys,
                        description: hist
                    }).set_index(col)
                    st.bar_chart(display)

                else:
                    if density:
                        tot = data[col].value_counts().values.sum()
                        st.bar_chart(data[col].value_counts() / tot)
                    else:
                        st.bar_chart(data[col].value_counts())

        elif chart_type == 'Line chart':
            col0, col1 = st.columns(2)
            col_x = col0.selectbox('Select a feature to display on x axis', columns)
            cols_y = col1.multiselect('Select one or more features to display on y axis', columns)

            if st.button('Display line chart'):
                x_values = data[col_x].values
                to_display = {col_x: x_values}

                for col_y in cols_y:
                    y_values = data[col_y].values
                    to_display[col_y] = y_values

                to_display = pd.DataFrame(to_display).set_index(col_x)
                st.line_chart(to_display)

        elif chart_type == 'Map':

            cols = st.columns(2)
            lat = cols[0].selectbox('Select the columns for latitude', data.columns.values)
            lon = cols[1].selectbox('Select the columns for longitude', data.columns.values)

            if st.button('Display map'):
                data.rename({lat: 'latitude'},axis='columns', inplace=True)
                data.rename({lon: 'longitude'},axis='columns', inplace=True)

                st.map(data)

