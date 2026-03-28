import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class DeFiAdvisorAI:
    def __init__(self):
        self.model = None
        self.data = None

    def load_data(self, filepath):
        # Simulación de carga de datos de mercado y perfiles de usuario
        self.data = pd.read_csv(filepath)

    def train_model(self):
        # Simulación de entrenamiento de un modelo de clasificación para recomendaciones
        if self.data is None:
            print("Error: No hay datos cargados para entrenar el modelo.")
            return

        X = self.data[['user_risk_tolerance', 'market_volatility', 'protocol_apy']]
        y = self.data['recommended_strategy']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        print(f"Precisión del modelo: {accuracy_score(y_test, predictions)}")

    def analyze_risk_profile(self, user_data):
        # Simulación de análisis de perfil de riesgo del usuario
        risk_score = user_data.get('risk_tolerance', 5) # Escala de 1 a 10
        if risk_score <= 3:
            return "conservador"
        elif risk_score <= 7:
            return "moderado"
        else:
            return "agresivo"

    def recommend_strategy(self, user_data, market_data):
        # Simulación de recomendación de estrategia basada en perfil de riesgo y datos de mercado
        if self.model is None:
            print("Advertencia: Modelo no entrenado. Usando recomendaciones básicas.")
            user_risk_type = self.analyze_risk_profile(user_data)
            if user_risk_type == "conservador":
                return {"strategy_id": "STG001", "description": "Staking de bajo riesgo en stablecoins."}
            elif user_risk_type == "moderado":
                return {"strategy_id": "STG002", "description": "Lending en protocolos establecidos con APY moderado."}
            else:
                return {"strategy_id": "STG003", "description": "Yield farming en pools de alta liquidez."}
        else:
            # Aquí se usaría el modelo entrenado para hacer predicciones más sofisticadas
            # Por simplicidad, se simula una predicción
            input_data = pd.DataFrame([[user_data.get('risk_tolerance', 5), market_data.get('volatility', 0.5), market_data.get('protocol_apy', 0.08)]],
                                      columns=['user_risk_tolerance', 'market_volatility', 'protocol_apy'])
            predicted_strategy = self.model.predict(input_data)[0]
            return {"strategy_id": predicted_strategy, "description": f"Estrategia recomendada: {predicted_strategy}"}

if __name__ == "__main__":
    advisor_ai = DeFiAdvisorAI()

    # Crear un archivo CSV de datos de ejemplo para el entrenamiento
    sample_data = {
        'user_risk_tolerance': [2, 8, 5, 3, 7, 9, 1, 6, 4, 10],
        'market_volatility': [0.1, 0.7, 0.4, 0.2, 0.6, 0.8, 0.15, 0.5, 0.3, 0.9],
        'protocol_apy': [0.03, 0.15, 0.08, 0.05, 0.12, 0.20, 0.04, 0.10, 0.06, 0.25],
        'recommended_strategy': ['STG001', 'STG003', 'STG002', 'STG001', 'STG002', 'STG003', 'STG001', 'STG002', 'STG001', 'STG003']
    }
    sample_df = pd.DataFrame(sample_data)
    sample_df.to_csv('sample_defi_data.csv', index=False)

    advisor_ai.load_data('sample_defi_data.csv')
    advisor_ai.train_model()

    user_profile = {"risk_tolerance": 6}
    market_conditions = {"volatility": 0.6, "protocol_apy": 0.10}
    recommendation = advisor_ai.recommend_strategy(user_profile, market_conditions)
    print(f"Recomendación para el usuario: {recommendation}")
