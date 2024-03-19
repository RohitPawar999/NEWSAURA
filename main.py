import streamlit as st
import requests

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def tech_news():
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def sports_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def politics_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def health_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']


def enter_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def fetch_weather():
    url = "http://api.weatherapi.com/v1/current.json?key=4eef9a49617a42d29d9114817241903&q=india&aqi=no"
    response = requests.get(url)
    data = response.json()
    return data

def trending_news():
    url ="https://newsapi.org/v2/top-headlines?country=in&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def articles():
    url="https://newsapi.org/v2/everything?q=tesla&from=2024-02-19&sortBy=publishedAt&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']

def apple():
    url="https://newsapi.org/v2/everything?q=apple&from=2024-03-18&to=2024-03-18&sortBy=popularity&apiKey=97f6ae1c888c4c128e055b58fcb901b4"
    response = requests.get(url)
    data = response.json()
    return data['articles']









def main():
    st.set_page_config(page_title="🌐 NewsAura 📰", page_icon="🌐")
    st.markdown(
        """
        <style>
            .reportview-container {
                background: linear-gradient(90deg, #d4eaff 0%, #ffffff 100%);
            }
            .sidebar .sidebar-content {
                background: linear-gradient(90deg, #ffffff 0%, #d4eaff 100%);
            }
            .sidebar .sidebar-content .block-container {
                color: #333;
            }
            .stButton>button {
                color: #fff;
                background-color: #007bff;
                border-color: #007bff;
            }
            .stButton>button:hover {
                background-color: #0056b3;
                border-color: #0056b3;
            }
            .stRadio>div>label {
                color: #333;
            }
            .stRadio>div>div {
                color: #333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and logo
    st.title("🌐 NewsAura 📰")
    st.write(
        "Welcome to NewsAura, your gateway to the latest and most trending news from around the world. Stay informed with our comprehensive coverage of breaking news, insightful analysis, and in-depth reports.")
    st.markdown("---")

    # Sidebar
    st.sidebar.title("🌐 NewsAura 📰")
    #st.sidebar.image("C:/Users/rohit/OneDrive/Desktop/Power BI/OIP.png", use_column_width=True)
    st.sidebar.markdown("---")
    st.sidebar.subheader("News Categories")
    selected_category = st.sidebar.selectbox("Select a category:", (
        "Trending", "Business", "Tech", "Sports", "Politics", "Health", "Entertainment"))
    st.sidebar.markdown("---")
    st.sidebar.subheader("Articles")
    submit=st.sidebar.button("Top Articles")
    if submit:
        news_data_1=articles()+apple()
        for news_item in news_data_1:
            st.subheader(f"- {news_item['title']}")
            if news_item['urlToImage']:  # Check if image URL exists
                st.image(news_item['urlToImage'], width=700)
            st.write(news_item['description'])
            st.write(news_item['url'])
            st.markdown("---")


    st.sidebar.markdown("---")

    # Weather information
    weather_data = fetch_weather()
    if 'error' in weather_data:
        st.sidebar.error(weather_data['error']['message'])
    else:
        st.sidebar.subheader("Weather Information")
        st.sidebar.write("Location:", weather_data['location']['name'])
        st.sidebar.write("Temperature (°C):", weather_data['current']['temp_c'])
        st.sidebar.write("Condition:", weather_data['current']['condition']['text'])
        st.sidebar.write("Wind Speed (km/h):", weather_data['current']['wind_kph'])
        st.sidebar.write("Humidity:", weather_data['current']['humidity'])
        st.sidebar.write("Cloud Cover (%):", weather_data['current']['cloud'])

    # News categories


    # Fetch news based on selected category
    if selected_category == "Business":
        st.subheader("Business Headlines")
        news_data = fetch_news()
    elif selected_category == "Tech":
        st.subheader("Tech Headlines")
        news_data = tech_news()
    elif selected_category == "Sports":
        st.subheader("Sports Headlines")
        news_data = sports_news()
    elif selected_category == "Politics":
        st.subheader("Political Headlines")
        news_data =  politics_news()
    elif selected_category == "Health":
        st.subheader("Health Headlines")
        news_data = health_news()
    elif selected_category == "Entertainment":
        st.subheader("Entertainment Headlines")
        news_data = enter_news()
    else:
        st.subheader("Trending Headlines")
        news_data = trending_news()

    # Display news headlines
    if news_data:
        for news_item in news_data:
            st.subheader(f"- {news_item['title']}")
            if news_item['urlToImage']:  # Check if image URL exists
                st.image(news_item['urlToImage'], width=700)
            st.write(news_item['description'])
            st.write(news_item['url'])
            st.markdown("---")


if __name__ == "__main__":
    main()









