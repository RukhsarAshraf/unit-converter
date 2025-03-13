import streamlit as st

# Custom Styling
st.markdown("""
    <style>
        /* Change the background color */
        [data-testid="stAppViewContainer"] {
            background-color: #EDD7F3;
        }

        /* Main Title Styling */
        .main-title {
            font-size: 32px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }

        /* Styled Box for Result */
        .styled-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            font-size: 18px;
        }

        /* Convert Button Styling */
        .convert-btn-container {
            margin-top: 20px; /* Adjust this value to move the button down */
            text-align: center;
        }

        .convert-btn {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 16px !important;
            padding: 10px 20px !important;
            border-radius: 5px !important;
        }

        /* Custom Styling for Labels */
        .custom-label {
            font-size: 18px;
            font-weight: bold;
            color: black;
            margin-bottom: -20px; /* Reduce space between label and input */
        }

    </style>
""", unsafe_allow_html=True)

# Title with Styling
st.markdown('<h1 class="main-title">🔄 Swift Unit Converter ⚡</h1>', unsafe_allow_html=True)

# Custom Labels with Styling
st.markdown('<p class="custom-label">🔢 Enter value:</p>', unsafe_allow_html=True)
value = st.number_input("", min_value=1.0, step=1.0)

st.markdown('<p class="custom-label">📏 Convert from:</p>', unsafe_allow_html=True)
unit_from = st.selectbox("", ["meters", "kilometers", "grams", "kilograms"], key="unit_from")

st.markdown('<p class="custom-label">📐 Convert to:</p>', unsafe_allow_html=True)
unit_to = st.selectbox("", ["meters", "kilometers", "grams", "kilograms"], key="unit_to")

# Move button down using styled div
st.markdown('<div class="convert-btn-container">', unsafe_allow_html=True)

if st.button("Convert", key="convert", help="Click to convert", use_container_width=True):
    def convert_units(value, unit_from, unit_to):
        conversions = {
            "meters_kilometers": 0.001,
            "kilometers_meters": 1000,
            "grams_kilograms": 0.001,
            "kilograms_grams": 1000,
        }
        key = f"{unit_from}_{unit_to}"
        return value * conversions[key] if key in conversions else "Conversion not supported"

    result = convert_units(value, unit_from, unit_to)

    # Result box styling
    st.markdown(f"""
        <div class="styled-box">
            <b>Converted Value:</b> {result}
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Closing div tag
