import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
#st.title('Title')
data = pd.DataFrame(np.random.randn(100,3),
                    columns=['A','B','C'])
#st.line_chart(data) #this is create line charts
#st.line_chart(data, y=['A']) # this is to create linechart for column A
#st.line_chart(data, y=['B']) # this is to create linechart for column B
#st.line_chart(data, y=['C']) # this is to create linechart for column C
#data
#st.area_chart(data)
#st.area_chart(data, y=['A'])
#st.area_chart(data, y=['B'])
#st.area_chart(data, y=['C'])
#st.header('UPI_Transactions')
#data=pd.read_csv('E:/Practice Files/hotstar.csv')
#st.dataframe(data)
#st.line_chart(data, y=['year']) #this is create line charts
#fig,ax=plt.subplots()
#ax.scatter(data['A'],data['B'])
#st.pyplot(fig)
#chart = alt.chart(data).mark_circle().encode(x='A', y='B')
#st.altair_chart(chart, use_container_width=True)
#st.graphviz_chart("""digraph{
                  #watch ->like
                  #like->share
                  #share->create
                  #create->watch
                  #}""")
data = pd.DataFrame({
    'lat': [37.7749, 40.7128, 34.0522, 41.8781, 47.6062],
    'lon': [-122.4194, -74.0060, -118.2437, -87.6298, -122.3321]
})
st.map(data) 