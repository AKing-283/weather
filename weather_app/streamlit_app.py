import streamlit as st
from weather_app.weather.models import City  # Replace with your model

def main():
    st.title("Your Django App on Streamlit")

    model_data = City.objects.all()
    st.write(model_data)

if __name__ == "__main__":
    main()