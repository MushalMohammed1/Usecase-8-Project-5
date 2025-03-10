import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("Coursera.csv")

# Sidebar for navigation
st.sidebar.title("Select the page")
page = st.sidebar.radio("Go to", ["Clustering Model", "Course Filtering"])

# If the user selects the "Clustering Model" page
if page == "Clustering Model":
    st.title("Feature Inputs for Clustering 🚀")

    # Select clustering model
    model_choice = st.selectbox(
        "Select Clustering Model:",
        ["K-Means", "K-Modes"]
    )

    # K-Means clustering model
    if model_choice == "K-Means":
        st.write("Please enter the values for the following features:")

        # User input for features for K-Means
        rate = st.number_input("Rate :", min_value=0, step=1)
        reviews = st.number_input("Reviews:", min_value=0.0, step=0.1)
        level = st.selectbox("Level:", ["Beginner", "Intermediate", "Mixed", "Advanced"])

        st.write(f"You selected: Rate: {rate}, Reviews: {reviews}, Level: {level}")

    # K-Modes clustering model
    if model_choice == "K-Modes":
        st.write("Please enter the values for the following features:")

        # User input for features for K-Modes
        level = st.selectbox("Level:", ["Beginner", "Intermediate", "Mixed", "Advanced"])
        subject = st.selectbox("Subject:", df['Subject'].unique())  # Get unique subjects from the data
        duration = st.selectbox("Duration:", ['Less Than 2 Hours', '1 - 3 Months', '1 - 4 Weeks', '3 - 6 Months'])

        st.write(f"You selected: Level: {level}, Subject: {subject}, Duration: {duration}")

# If the user selects the "Course Filtering" page
if page == "Course Filtering":
    st.markdown(
        """
        <style>
        body {
            direction: ltr;
            text-align: left;
            width: 100%;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .streamlit-container {
            width: 100% !important;
        }
        .block-container {
            width: 100% !important;
        }

        header {
            background-color: #ffffff;
            color: black;
            padding: 20px;
            text-align: left;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            width: 100%;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            border-bottom: 2px solid #4a90e2;
        }

        .logo {
            width: 100px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-right: 20px;
        }

        .title {
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
            margin: 0;
            font-family: 'Georgia', serif;
        }

        .card {
            background: linear-gradient(135deg, #ffffff, #f0f4f8);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: left;
            font-size: 16px;
            margin-bottom: 20px;
            box-sizing: border-box;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            width: 100%;
            animation: fadeIn 0.5s ease-in-out;
        }

        .card-title {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 15px;
            font-family: 'Georgia', serif;
        }

        .card-details {
            font-size: 16px;
            color: #34495e;
            margin-bottom: 10px;
            line-height: 1.6;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .stButton>button {
            background: linear-gradient(135deg, #4a90e2, #357abd);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: background 0.3s ease, transform 0.3s ease;
            font-size: 16px;
            font-weight: bold;
        }

        .stButton>button:hover {
            background: linear-gradient(135deg, #357abd, #4a90e2);
            transform: translateY(-2px);
        }

        @media (max-width: 768px) {
            .columns-container {
                flex-direction: column;
            }
            .card {
                width: 100%;
            }
            .logo {
                width: 80px;
            }
            .title {
                font-size: 28px;
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }

        ::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        .stMarkdown {
            margin-bottom: 20px;
        }

        .stSelectbox, .stButton {
            margin-bottom: 20px;
        }

        .filter-section {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        .emoji {
            font-size: 20px;
            margin-right: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header with logo and title
    st.markdown(
        """
        <header>
            <img class="logo" src="https://149357281.v2.pressablecdn.com/wp-content/uploads/2020/12/android-chrome-512x512-1.png" alt="App Logo">
            <div class="title"> Course Filtering 🎓📚</div>
        </header>
        """, unsafe_allow_html=True)

    # App description
    st.markdown(
        """
        <div style="text-align: left; font-size: 20px; margin-top: 20px; color: #34495e;">
            Welcome to the <strong>Course Filtering App</strong>! 🚀 This application allows you to filter courses based on subject, institution, level, and learning product. 
            We aim to help you find courses that match your interests and learning goals. Select your filters and explore a variety of courses to enhance your skills. 
            Let's get started! 🌟
        </div>
        """, unsafe_allow_html=True
    )

    # Filters with Emojis
    subject_filter = st.selectbox('📚 Select Subject', ['None'] + list(df['Subject'].unique()))
    institution_filter = st.selectbox('🏛 Select Institution', ['None'] + list(df['Institution'].unique()))
    level_filter = st.selectbox('🎓 Select Level', ['None'] + list(df['Level'].unique()))
    learning_product_filter = st.selectbox('📘 Select Learning Product', ['None'] + list(df['Learning Product'].unique()))

    # Apply filters
    if st.button('Filter Data'):
        filtered_df = df.copy()

        if subject_filter != 'None':
            filtered_df = filtered_df[filtered_df['Subject'] == subject_filter]

        if institution_filter != 'None':
            filtered_df = filtered_df[filtered_df['Institution'] == institution_filter]

        if level_filter != 'None':
            filtered_df = filtered_df[filtered_df['Level'] == level_filter]

        if learning_product_filter != 'None':
            filtered_df = filtered_df[filtered_df['Learning Product'] == learning_product_filter]

        # Display filtered data as cards
        st.write('### Filtered Courses:')

        # Check if no results found
        if filtered_df.empty:
            st.warning("No courses found with the selected filters. 😢")
        else:
            # Create a container for the cards in 2 columns
            cols = st.columns(2)  # Now displaying 2 cards per row
            col_idx = 0  # Start with the first column

            for _, row in filtered_df.iterrows():
                with cols[col_idx]:
                    st.markdown(
                        f"""
                        <div class="card">
                            <div class="card-title">{row['Title']}</div>
                            <div class="card-details">📌 Subject: {row['Subject']}</div>
                            <div class="card-details">🏛 Institution: {row['Institution']}</div>
                            <div class="card-details">🎓 Level: {row['Level']}</div>
                            <div class="card-details">📘 Learning Product: {row['Learning Product']}</div>
                            <div class="card-details">⭐ Rate: {row['Rate']}</div>
                            <div class="card-details">📝 Reviews: {row['Reviews']}</div>
                        </div>
                        """, unsafe_allow_html=True
                    )

                # Move to the next column
                col_idx += 1
                if col_idx == 2:  # Reset the column index after 2 cards
                    col_idx = 0

