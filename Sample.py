import streamlit  as st
import pandas as pd
import numpy as np
#st.title("Streamlit Session")
#st.header("Header")
#st.subheader("Sub header")
#st.text("This is an interactive streamlit application")
#st.markdown("""
# h1 tag
## h2 tag
### h3 tag
#:moon: <br>
#:sunglasses:    
#**Fat**
#_Fat_                          
#""",True)
#st.write("hello world")
#st.write(st)
#st.write(1,2,3,4)
#st.write('the numbers are',[1,2,3,4,5])
#dic={
   # 'Name':'Hemamber',
    # 'Age':33,
     #'Place':'Visakhapatna'
     #}
#st.write(dic)


df = pd.read_csv("E:/Practice Files/hotstar.csv")
st.write(df)

st.dataframe(df)

st.table(df)

st.title('Rotten Tomatoes')
Movie_ratings= pd.read_csv("E:/Practice Files/Movie Ratings/Rotten Tomatoes Movies.csv")
st.dataframe(Movie_ratings)
#st.table(Movie_ratings)

JSON_data={
    "user_id": 12345,
    "user_info": {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 29
    },
    "purchases": [
        {
            "item_id": "A001",
            "item_name": "Laptop",
            "price": 1200.99,
            "quantity": 1
        },
        {
            "item_id": "B002",
            "item_name": "Mouse",
            "price": 25.50,
            "quantity": 2
        }
    ],
    "timestamp": "2024-08-11T15:30:00Z"
}
#st.json(JSON_data)(# to display data normally in expanded format)
#st.json(JSON_data, expanded=False)(#to disable the epanded view of the data)
st.metric('TCS Stock', value=897, delta='12.5') #(Here there is no mathematicalet sign before the 12.5 hence the system takes it as positive and then its displayed as green Upper arrow)

st.metric('TCS Stock', value=897, delta='-12.5') #(Here the - represents the down arrow hence -12.5 will be displayed with redcolor down arrow)

st.metric('TCS Stock', value=897, delta='12.5', delta_color='off') #(Here we kept delta color as off hence there is no color for arrow is displayed)