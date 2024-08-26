import joblib
import streamlit as st
from streamlit_option_menu import option_menu
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Log an info message
logging.info('User accessed the app.')

try:
    # Load the models
    diabetes_model = joblib.load(open('diabetes_model.joblib', 'rb'))
    heart_model = joblib.load(open('heart_model.joblib', 'rb'))
    breast_model = joblib.load(open('breast_cancer_model.joblib', 'rb'))
    parkinson_model = joblib.load(open('parkinson_model.joblib', 'rb'))
    
    with st.sidebar:
        selected = option_menu('Multiple Disease Prediction System',
                            ['Diabetes Disease Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction',
                            'Parkinson Disease Prediction'],
                            icons=['activity','heart-pulse','person'], 
                            default_index=0)

    ### Diabetes Disease Prediction -----------------------------------------------
    if selected == 'Diabetes Disease Prediction':
        st.title(':medical_symbol: Diabetes Disease Prediction')
        st.subheader('Please read the medical description below before entering the values :exclamation:')
        
        # User inputs
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Pregnancies = st.text_input("Number of times pregnant")
        with col2:
            Glucose = st.text_input("Glucose concentration")
        with col3:
            BloodPressure = st.text_input("Blood pressure (mm Hg)")
        with col1:
            SkinThickness = st.text_input("Triceps skin fold thickness (mm)")
        with col2:
            Insulin = st.text_input("Insulin (mu U/ml)")
        with col3:
            BMI = st.text_input("Body mass index")
        with col1:
            DiabetesPedigreeFunction = st.text_input("Diabetes pedigree function value")
        with col2:
            Age = st.text_input("Age of the patient")
        
        diab_diagnosis = ''
        
        if st.button("Diabetes Test result"):
            try:
                features = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
                features = [float(feature) for feature in features]

                diabete_pred = diabetes_model.predict([features])

                if diabete_pred == 1:
                    diab_diagnosis = "The person has a high probability of being Diabetic"
                else:
                    diab_diagnosis = "The person has a low probability of being Diabetic"

            except Exception as e:
                st.error(f"Error predicting diabetes: {e}")
                diab_diagnosis = "Prediction error"

        st.success(diab_diagnosis)
        
        st.header('Attention! Please follow the values given in the range') 
        st.markdown("""
            * **Pregnancies**: Number of times pregnant, range: [0-17]
            * **Glucose**: Plasma glucose concentration in an oral glucose tolerance test, range: [30.46-199]
            * **BloodPressure**: Diastolic blood pressure (mm Hg), range: [24-122]
            * **SkinThickness**: Triceps skin fold thickness (mm), range: [7-99]
            * **Insulin**: 2-Hour serum insulin (mu U/ml), range: [89.10-846]
            * **BMI**: Body mass index (weight in kg/(height in m)^2), range: [18, 67]
            * **DiabetesPedigreeFunction**: Diabetes pedigree function, range: [0-2.5]
            * **Age**: Age (years)
        """)

    ### Heart Disease Prediction -----------------------------------------
    if selected == 'Heart Disease Prediction':
        st.title(":heartpulse: Heart Disease Prediction")
        st.subheader("Please read the medical descriptions below before entering the values :exclamation:")
        
        # User inputs
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.text_input("Age of the person")
        with col2:
            sex = st.text_input("Sex: 0 for male, 1 for female")
        with col3:
            cp = st.text_input("Chest pain type")
        with col1:
            trestbps = st.text_input("Resting blood pressure (mm Hg)")
        with col2:
            chol = st.text_input("Serum cholesterol (mg/dl)")
        with col3:
            fbs = st.text_input("Fasting blood sugar (> 120 mg/dl)")
        with col1:
            restecg = st.text_input("Resting electrocardiographic results (0, 1, 2)")
        with col2:
            thalach = st.text_input("Maximum heart rate achieved")
        with col3:
            exang = st.text_input("Exercise induced angina (0 or 1)")
        with col1:
            oldpeak = st.text_input("Oldpeak")
        with col2:
            slope = st.text_input("Slope of the peak exercise ST segment")
        with col3:
            ca = st.text_input("Number of major vessels (0-3) colored by fluoroscopy")
        with col1:
            thal = st.text_input("Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)")
        
        heart_diagnosis = ''
        
        if st.button("Heart Disease Test result"):
            try:
                features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
                features = [float(feature) for feature in features]

                heart_pred = heart_model.predict([features])

                if heart_pred == 1:
                    heart_diagnosis = "The person is more likely affected by heart disease"
                else:
                    heart_diagnosis = "The person shows a low probability of having heart disease"

            except Exception as e:
                st.error(f"Error predicting heart disease: {e}")
                heart_diagnosis = "Prediction error"

        st.success(heart_diagnosis)
        
        st.header('Attention! Please follow the values given in the range') 
        st.markdown("""
            * **Age**
            * **Sex**: 0 represents Male and 1 represents Female
            * **Chest pain type**: [0-1-2-3]
            * **Resting blood pressure**: range [94-200]
            * **Serum cholesterol**: in mg/dl, range: [126-564]
            * **Fasting blood sugar** > 120 mg/dl
            * **Resting electrocardiographic results** (values 0,1,2)
            * **Maximum heart rate achieved**: range [71-202]
            * **Exercise induced angina**: Binary value, range: 0 or 1
            * **Oldpeak**: Depression induced by exercise relative to rest, range: [0-6.2]
            * **The slope of the peak exercise ST segment**: range: [0-1-2]
            * **Number of major vessels**: range [0-3] colored by fluoroscopy
            * **Thal**: 0 = normal; 1 = fixed defect; 2 = reversible defect
        """)

    ### Parkinson Disease Prediction ---------------------------------------------     
    if selected == 'Parkinson Disease Prediction':
        st.title(":person_frowning: Parkinson Disease Prediction")
        st.subheader("Please read the medical descriptions below before entering the values :exclamation:")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            fo = st.text_input("MDVP:Fo(Hz)")
        with col2:
            fhi = st.text_input("MDVP:Fhi(Hz)")
        with col3:
            flo = st.text_input("MDVP:Flo(Hz)")
        with col4:
            Jitter_percent = st.text_input("MDVP:Jitter(%)")
        with col5:
            Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
        with col1:
            RAP = st.text_input("MDVP:RAP")
        with col2:
            PPQ = st.text_input("MDVP:PPQ")
        with col3:
            DDP = st.text_input("Jitter:DDP")
        with col4:
            Shimmer = st.text_input("MDVP:Shimmer")
        with col5:
            Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
        with col1:
            APQ3 = st.text_input("Shimmer:APQ3")
        with col2:
            APQ5 = st.text_input("Shimmer:APQ5")
        with col3:
            APQ = st.text_input("MDVP:APQ")
        with col4:
            DDA = st.text_input("Shimmer:DDA")
        with col5:
            NHR = st.text_input("NHR")
        with col1:
            HNR = st.text_input("HNR")
        with col2:
            RPDE = st.text_input("RPDE")
        with col3:
            DFA = st.text_input("DFA")
        with col4:
            spread1 = st.text_input("spread1")
        with col5:
            spread2 = st.text_input("spread2")
        with col1:
            D2 = st.text_input("D2")
        with col2:
            PPE = st.text_input("PPE")
        
        parkinsons_diagnosis = ''
        
        if st.button("Parkinson Disease Test result"):
            try:
                features = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
                features = [float(feature) for feature in features]

                parkinsons_pred = parkinson_model.predict([features])

                if parkinsons_pred == 1:
                    parkinsons_diagnosis = "The person shows a high likelihood of having Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person shows a low likelihood of having Parkinson's disease"

            except Exception as e:
                st.error(f"Error predicting Parkinson's disease: {e}")
                parkinsons_diagnosis = "Prediction error"

        st.success(parkinsons_diagnosis)
        
        st.header('Attention! Please follow the values given in the range') 
        st.markdown("""
            * **MDVP:Fo(Hz)**: Average vocal fundamental frequency, range: [88.333-260.105]
            * **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency, range: [102.145-592.03]
            * **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency, range: [65.476-239.17]
            * **MDVP:Jitter(%)**: Variation in fundamental frequency, range: [0.00168-0.03316]
            * **MDVP:Jitter(Abs)**: Absolute jitter in milliseconds, range: [0.000007-0.00026]
            * **MDVP:RAP**: Relative amplitude perturbation, range: [0.00068-0.02144]
            * **MDVP:PPQ**: Five-point amplitude perturbation quotient, range: [0.00089-0.01958]
            * **Jitter:DDP**: Difference of differences of period jitter, range: [0.00204-0.06435]
            * **MDVP:Shimmer**: Variation in amplitude, range: [0.00954-0.11908]
            * **MDVP:Shimmer(dB)**: Shimmer in decibels, range: [0.085-0.554]
            * **Shimmer:APQ3**: Three-point amplitude perturbation quotient, range: [0.003-0.03593]
            * **Shimmer:APQ5**: Five-point amplitude perturbation quotient, range: [0.00455-0.06425]
            * **MDVP:APQ**: Average pitch period perturbation quotient, range: [0.00371-0.13778]
            * **Shimmer:DDA**: Degree of the difference of the average magnitude of difference of adjacent cycles, range: [0.009-0.107]
            * **NHR**: Noise-to-harmonics ratio, range: [0.004-0.314]
            * **HNR**: Harmonics-to-noise ratio, range: [8.441-33.047]
            * **RPDE**: Recurrence period density entropy, range: [0.25657-0.685151]
            * **DFA**: Detrended fluctuation analysis, range: [0.574263-0.825288]
            * **spread1**: Nonlinear measure of fundamental frequency variation, range: [-7.964058-0.336]
            * **spread2**: Nonlinear measure of fundamental frequency variation, range: [0.006272-2.284115]
            * **D2**: Nonlinear dynamic complexity measure, range: [1.423287-3.671155]
            * **PPE**: Pitch period entropy, range: [0.044539-0.527367]
        """)
    
    ### Breast Cancer Prediction ---------------------------------------------------
    if selected == 'Breast Cancer Prediction':
        st.title(":person_frowning: Breast Cancer Prediction")
        st.subheader("Please read the medical descriptions below before entering the values :exclamation:")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            mean_radius = st.text_input("Mean Radius")
        with col2:
            mean_texture = st.text_input("Mean Texture")
        with col3:
            mean_perimeter = st.text_input("Mean Perimeter")
        with col4:
            mean_area = st.text_input("Mean Area")
        with col1:
            mean_smoothness = st.text_input("Mean Smoothness")
        with col2:
            mean_compactness = st.text_input("Mean Compactness")
        with col3:
            mean_concavity = st.text_input("Mean Concavity")
        with col4:
            mean_concave_points = st.text_input("Mean Concave Points")
        with col1:
            mean_symmetry = st.text_input("Mean Symmetry")
        with col2:
            mean_fractal_dimension = st.text_input("Mean Fractal Dimension")
        with col3:
            radius_se = st.text_input("Radius SE")
        with col4:
            texture_se = st.text_input("Texture SE")
        with col1:
            perimeter_se = st.text_input("Perimeter SE")
        with col2:
            area_se = st.text_input("Area SE")
        with col3:
            smoothness_se = st.text_input("Smoothness SE")
        with col4:
            compactness_se = st.text_input("Compactness SE")
        with col1:
            concavity_se = st.text_input("Concavity SE")
        with col2:
            concave_points_se = st.text_input("Concave Points SE")
        with col3:
            symmetry_se = st.text_input("Symmetry SE")
        with col4:
            fractal_dimension_se = st.text_input("Fractal Dimension SE")
        with col1:
            worst_radius = st.text_input("Worst Radius")
        with col2:
            worst_texture = st.text_input("Worst Texture")
        with col3:
            worst_perimeter = st.text_input("Worst Perimeter")
        with col4:
            worst_area = st.text_input("Worst Area")
        with col1:
            worst_smoothness = st.text_input("Worst Smoothness")
        with col2:
            worst_compactness = st.text_input("Worst Compactness")
        with col3:
            worst_concavity = st.text_input("Worst Concavity")
        with col4:
            worst_concave_points = st.text_input("Worst Concave Points")
        with col1:
            worst_symmetry = st.text_input("Worst Symmetry")
        with col2:
            worst_fractal_dimension = st.text_input("Worst Fractal Dimension")
        
        breast_cancer_diagnosis = ''
        
        if st.button("Breast Cancer Test result"):
            try:
                features = [
                    mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension,
                    radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                    worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension
                ]
                features = [float(feature) for feature in features]

                breast_cancer_pred = breast_model.predict([features])

                if breast_cancer_pred == 1:
                    breast_cancer_diagnosis = "The person is more likely to have Breast Cancer"
                else:
                    breast_cancer_diagnosis = "The person is less likely to have Breast Cancer"

            except Exception as e:
                st.error(f"Error predicting breast cancer: {e}")
                breast_cancer_diagnosis = "Prediction error"

        st.success(breast_cancer_diagnosis)
        
        st.header('Attention! Please follow the values given in the range') 
        st.markdown("""
            * **Mean Radius**: [6.981-28.11]
            * **Mean Texture**: [9.71-39.28]
            * **Mean Perimeter**: [43.79-188.5]
            * **Mean Area**: [143.5-2501.0]
            * **Mean Smoothness**: [0.053-0.163]
            * **Mean Compactness**: [0.019-0.345]
            * **Mean Concavity**: [0.0-0.427]
            * **Mean Concave Points**: [0.0-0.201]
            * **Mean Symmetry**: [0.106-0.304]
            * **Mean Fractal Dimension**: [0.05-0.097]
            * **Radius SE**: [0.112-2.873]
            * **Texture SE**: [0.36-4.885]
            * **Perimeter SE**: [0.757-21.98]
            * **Area SE**: [6.802-542.2]
            * **Smoothness SE**: [0.001-0.031]
            * **Compactness SE**: [0.002-0.135]
            * **Concavity SE**: [0.0-0.396]
            * **Concave Points SE**: [0.0-0.053]
            * **Symmetry SE**: [0.008-0.079]
            * **Fractal Dimension SE**: [0.001-0.03]
            * **Worst Radius**: [7.93-36.04]
            * **Worst Texture**: [12.02-49.54]
            * **Worst Perimeter**: [50.41-251.2]
            * **Worst Area**: [185.2-4254.0]
            * **Worst Smoothness**: [0.071-0.223]
            * **Worst Compactness**: [0.027-1.058]
            * **Worst Concavity**: [0.0-1.252]
            * **Worst Concave Points**: [0.0-0.291]
            * **Worst Symmetry**: [0.156-0.664]
            * **Worst Fractal Dimension**: [0.055-0.208]
        """)
# try:
#     diabetes_model = joblib.load(open('diabetes_model.joblib', 'rb'))
#     heart_model = joblib.load(open('heart_model.joblib', 'rb'))
#     breast_model = joblib.load(open('breast_cancer_model.joblib', 'rb'))
#     parkinson._model = joblib.load(open('parkinson_model.joblib', 'rb'))

except Exception as e:
    logging.error(f'Error loading models: {e}')
    st.error(f'Error loading models: {e}')
    st.stop()