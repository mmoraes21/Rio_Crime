import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from streamlit_folium import folium_static
from sklearn.ensemble import GradientBoostingRegressor
import folium
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.set_page_config(page_title="Rio Crime",
                   page_icon=":knife:")


def load_data():
    data = pd.read_csv('final_df3.csv')
    return data

def preprocess_data(data, target, areas_list):
    X = data[['Month', 'Year'] + areas_list]
    y = data[target]
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def predict_crime_count(model, future_date, area, areas_list):
    future_date = datetime.strptime(future_date, '%Y-%m-%d')
    month = future_date.month
    year = future_date.year

    input_dict = {
        'Month': month,
        'Year': year,
    }

    for a in areas_list:
        input_dict[a] = 1 if area == a else 0

    input_df = pd.DataFrame([input_dict])
    count_prediction = model.predict(input_df)
    return count_prediction[0]

def main():
    st.title('Crime Count Prediction')

    data = load_data()
    target_options = ['Attempted murder', 'Rape', 'Missing people', 'Homicides', 'Thefts', 'Kidnapping']
    target = st.selectbox('Select target variable', target_options)
    
    areas_list = ['Bangu', 'Barra da Tijuca', 'Bonsucesso',
       'Botafogo', 'Campinho', 'Campo Grande', 'Catete', 'Cidade Nova',
       'Complexo do Alemão', 'Copacabana', 'Engenho Novo', 'Guaratiba',
       'Gávea', 'Honório Gurgel', 'Ilha do Governador', 'Inhaúma', 'Ipanema',
       'Irajá', 'Leblon', 'Madureira', 'Marechal Hermes', 'Mem de Sá', 'Méier',
       'Pavuna', 'Penha', 'Piedade', 'Praça Mauá', 'Praça da Bandeira',
       'Praça da República', 'Realengo', 'Recreio', 'Ricardo de Albuquerque',
       'Rocinha', 'Santa Cruz', 'Santa Teresa', 'São Cristóvão', 'Tanque',
       'Taquara', 'Tijuca', 'Todos os Santos', 'Vicente de Carvalho',
       'Vila Isabel']

    X, y = preprocess_data(data, target, areas_list)
    model = train_model(X, y)

    user_future_date = st.date_input('Select a future date', min_value=datetime.today())
    user_area = st.selectbox('Select an area', areas_list)

    if st.button('Predict', help="The count displayed is regarding the selected month, not the day."):
        predicted_crime_count = predict_crime_count(model, str(user_future_date), user_area, areas_list)
        st.write(f"Prediction : {int(predicted_crime_count)}")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
   
        st.write(f"Mean Absolute Error (MAE): {mae}")
        st.write(f"Mean Squared Error (MSE): {mse}")
        st.write(f"R-squared (R²): {r2}")

if __name__ == "__main__":
    main()


st.markdown("---")


def generate_map():
    m = folium.Map(location=[-22.9208992, -43.4049743], zoom_start=10)
   
    locations = {
        'Bangu': (-22.8651287, -43.4633017),
    'Barra da Tijuca': (-22.9933807, -43.372282),
    'Bonsucesso': (-22.8666774, -43.25227),
    'Botafogo': (-22.948233, -43.1870279),
    'Campinho': (-22.8840104, -43.3492987),
    'Campo Grande': (-22.9025792, -43.572189),
    'Catete': (-22.9273119, -43.1741989),
    'Cidade Nova': (-22.9114947, -43.2045911),
    'Complexo do Alemão': (-22.8609113, -43.2678693),
    'Copacabana': (-22.97323, -43.1923549),
    'Engenho Novo': (-22.9079636, -43.2692827),
    'Guaratiba': (-22.9966116, -43.6506038),
    'Gávea': (-22.9806434, -43.2376226),
    'Honório Gurgel': (-22.844147, -43.3659608),
    'Ilha do Governador': (-22.8047566, -43.2374985),
    'Inhaúma': (-22.8723208, -43.2880716),
    'Ipanema': (-22.9844157, -43.1983036),
    'Irajá': (-22.8425026, -43.3247973),
    'Leblon': (-22.9837189, -43.2219737),
    'Madureira': (-22.8740729, -43.3290273),
    'Marechal Hermes': (-22.8619709, -43.3766948),
    'Mem de Sá': (-22.9123121, -43.1830871),
    'Méier': (-22.9045728,-43.2750804),
    'Pavuna': (-22.8191705, -43.365432),
    'Penha': (-22.8355099, -43.282657),
    'Piedade': (-22.8928815, -43.2998454),
    'Praça Mauá': (-22.8968093, -43.1828839),
    'Praça da Bandeira': (-22.9109799, -43.2110829),
    'Praça da República': (-22.9072893, -43.1916985),
    'Realengo': (-22.8784748, -43.4316251),
    'Recreio': (-23.0211552, -43.4763094),
    'Ricardo de Albuquerque': (-22.8426351, -43.4006332),
    'Rocinha': (-22.9876188, -43.2433081),
    'Santa Cruz': (-22.9189205, -43.6946375),
    'Santa Teresa': (-22.9230533, -43.1844352),
    'São Cristóvão': (-22.8955134, -43.2287101),
    'Tanque': (-22.9149596, -43.3624768),
    'Taquara': (-22.9208992, -43.3909743),
    'Tijuca': (-22.9326363, -43.2416569),
    'Todos os Santos': (-22.8957936, -43.2918657),
    'Vicente de Carvalho': (-22.8598582, -43.3117725),
    'Vila Isabel': (-22.9192794, -43.2599834)
    }

    for name, coords in locations.items():
        folium.Marker(coords, popup=name).add_to(m)

    return m

st.title('Rio de Janeiro Map')

mymap = generate_map()

folium_static(mymap)