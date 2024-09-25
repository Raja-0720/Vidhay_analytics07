
import streamlit as st
import pandas as pd

# Dummy dataset for courses (replace this with your scraped data)
bg_color = """
<style>
body {
    background-color: #f0f2f6;  /* Light grey background */
}
</style>
"""
st.markdown(bg_color, unsafe_allow_html=True)

data = {
    "Course Title": [
        "Python for Data Science",
        "Machine Learning Basics",
        "Deep Learning with TensorFlow",
        "Data Visualization with PowerBI",
        "Natural Language Processing with Python",
"Introduction to Generative  AI",
"Free Generative AI Courses",
"Getting Started with Large Language Models",
        "Tableau for Beginners",
        "Microsoft Excel: Formulas & Functions",
        "Introduction to Business Analytics",
        "Introduction to AI & ML",
        "Big Mart Sales Prediction Using R",
        "Time Series Forecasting using Python"

    ],
    "Course Description": [
        "Learn Python, the most in-demand language for Data Science.",
        "An introductory course on the basics of machine learning.",
        "Master deep learning concepts with hands-on TensorFlow projects.",
        "Visualize your data using PowerBI in this comprehensive course.",
        "Explore the world of NLP and build practical applications with Python.",
        "This course introduces the foundational concepts of Generative AI, focusing on how models like GANs and transformers can create new content such as images, text, and audio. Participants will explore real-world applications, gaining hands-on experience with popular tools like GPT ",
        "Microsoft Excel by mastering essential formulas and functions. From basic calculations to advanced data manipulation, learners will gain the skills needed to analyze and visualize data effectively.",
        ""
"Generative AI courses designed to equip you with the skills and knowledge needed to create innovative AI-generated content",
        "This course provides a comprehensive introduction to Large Language Models (LLMs), covering their architecture, training processes, and real-world applications",
        "a powerful data visualization tool, guiding them through its interface and essential features. Participants will learn how to create interactive dashboards and insightful visualizations to effectively analyze and present data.",
        "This course provides an overview of business analytics, exploring key concepts, tools, and techniques used to analyze data for informed decision-making.",
        "This course offers a foundational understanding of Artificial Intelligence (AI) and Machine Learning (ML), covering key concepts, algorithms, and applications in various industries.",
        "participants will learn to use R programming for predictive analytics by analyzing Big Mart sales data. Through hands-on projects, they will develop models to forecast sales trends and optimize business strategies effectively.",
        "This course provides a comprehensive introduction to time series forecasting using Python, covering essential techniques and libraries for analyzing temporal data. "


    ]
}

# Convert the dummy data to a pandas DataFrame
df = pd.DataFrame(data)


# Function for searching courses
def search_courses(query):
    # Convert the query to lowercase for case-insensitive search
    query = query.lower()

    # Filter courses based on whether the query appears in the title or description
    results = df[
        df['Course Title'].str.lower().str.contains(query) |
        df['Course Description'].str.lower().str.contains(query)
        ]

    return results if not results.empty else "No courses found for your query."


# Streamlit Interface
st.title("Smart Search for Analytics Vidhya Courses")
query = st.text_input("Enter your search query here...")

# Display the search results when the user submits the query
if query:
    results = search_courses(query)

    if isinstance(results, str):
        st.write(results)
    else:
        for index, row in results.iterrows():
            st.write(f"### {row['Course Title']}")
            st.write(f"{row['Course Description']}")
            st.write("---")  # Separator line for each course
