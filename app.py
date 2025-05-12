import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
loaded_model = joblib.load('best_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

# Page config with nicer layout
st.set_page_config(page_title="Student Dropout Prediction", layout="centered")

# CSS for custom colors and styling
st.markdown(
    """
    <style>
    .header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4a90e2;
        margin-bottom: 0.5rem;
    }
    .subheader {
        font-size: 1.25rem;
        color: #6c757d;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        font-weight: 600;
        padding: 0.6rem 1.4rem;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #357ABD;
        color: white;
    }
    .result-positive {
        color: #2e7d32;  /* green */
        font-weight: 700;
        font-size: 1.3rem;
        margin-top: 1rem;
    }
    .result-negative {
        color: #c62828;  /* red */
        font-weight: 700;
        font-size: 1.3rem;
        margin-top: 1rem;
    }
    .result-neutral {
        color: #555555;  
        margin-top: 0.5rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle
st.markdown('<div class="header">Student Dropout Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Fill the inputs below and get prediction results</div>', unsafe_allow_html=True)

# Define the mapping for application modes
application_mode_mapping = {
    1: '1st phase - general contingent',
    2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses',
    10: 'Ordinance No. 854-B/99',
    15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)',
    17: '2nd phase - general contingent',
    18: '3rd phase - general contingent',
    26: 'Ordinance No. 533-A/99, item b2) (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
    39: 'Over 23 years old',
    42: 'Transfer',
    43: 'Change of course',
    44: 'Technological specialization diploma holders',
    51: 'Change of institution/course',
    53: 'Short cycle diploma holders',
    57: 'Change of institution/course (International)'
}

# Use columns to create a balanced form layout
col1, col2 = st.columns(2)

with col1:
    curricular_units_2nd_sem_approved = st.slider(
        "Curricular Units 2nd Sem Approved", 
        min_value=0, max_value=30, value=14, step=1,
        help="Number of curricular units approved in the 2nd semester."
    )
    curricular_units_2nd_sem_grade = st.slider(
        "Curricular Units 2nd Sem Grade", 
        min_value=0, max_value=20, value=16, step=1,
        help="Average grade of curricular units in the 2nd semester (0-20 scale)."
    )
    curricular_units_1st_sem_approved = st.slider(
        "Curricular Units 1st Sem Approved", 
        min_value=0, max_value=30, value=14, step=1,
        help="Number of curricular units approved in the 1st semester."
    )
    curricular_units_1st_sem_grade = st.slider(
        "Curricular Units 1st Sem Grade", 
        min_value=0, max_value=20, value=16, step=1,
        help="Average grade of curricular units in the 1st semester (0-20 scale)."
    )
# Mapping dictionaries for encoding the user selections back to numeric values
tuition_fees_mapping = {"No": 0, "Yes": 1}
debtor_mapping = {"No": 0, "Yes": 1}
gender_mapping = {"Female": 0, "Male": 1}

with col2:
    tuition_fees_up_to_date_label = st.selectbox(
        "Tuition Fees Up to Date",
        options=["No", "Yes"],
        index=1,
        help="Has the tuition fees been paid up to date?"
    )
    age_at_enrollment = st.number_input(
        "Age at Enrollment",
        min_value=15, max_value=100, step=1, value=27,
        help="Age of the student at the time of enrollment."
    )
    debtor_label = st.selectbox(
        "Debtor",
        options=["No", "Yes"],
        index=1,
        help="Is the student a debtor?"
    )
    gender_label = st.selectbox(
        "Gender",
        options=["Female", "Male"],
        index=1,
        help="Gender of the student"
    )
    application_mode = st.selectbox(
        "Application Mode",
        options=list(application_mode_mapping.keys()),
        format_func=lambda x: application_mode_mapping[x],
        help="Select the application mode from the list."
    )

# Convert the selected labels back to numeric encoding before prediction
tuition_fees_up_to_date = tuition_fees_mapping[tuition_fees_up_to_date_label]
debtor = debtor_mapping[debtor_label]
gender = gender_mapping[gender_label]

st.divider()

if st.button("Predict"):
    df_input = pd.DataFrame({
        'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
        'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
        'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
        'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
        'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
        'Age_at_enrollment': [age_at_enrollment],
        'Debtor': [debtor],
        'Gender': [gender],
        'Application_mode': [application_mode]
    })

    numerical_features = [
        'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade',
        'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade',
        'Age_at_enrollment'
    ]

    df_scaled = df_input.copy()
    df_scaled[numerical_features] = loaded_scaler.transform(df_input[numerical_features])
    df_scaled = df_scaled[['Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
                           'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
                           'Tuition_fees_up_to_date', 'Age_at_enrollment', 'Debtor', 'Gender',
                           'Application_mode']]

    mapping = {0: "Siswa Dropout", 1: "Siswa Graduate"}

    prediction = loaded_model.predict(df_scaled)[0]
    probabilities = loaded_model.predict_proba(df_scaled)[0]

    proba_dropout = probabilities[0] * 100
    proba_graduate = probabilities[1] * 100

    # Show prediction with color-coded result
    if prediction == 0:
        st.markdown(f'<div class="result-negative">Prediksi: {mapping[prediction]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result-positive">Prediksi: {mapping[prediction]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="result-neutral">Probabilitas siswa akan dropout: {proba_dropout:.2f}%</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-neutral">Probabilitas siswa akan graduate: {proba_graduate:.2f}%</div>', unsafe_allow_html=True)

