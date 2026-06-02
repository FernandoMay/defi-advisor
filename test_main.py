import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from main import DeFiAdvisorAI


class TestDeFiAdvisorAI:
    def setup_method(self):
        self.advisor = DeFiAdvisorAI()

    def test_analyze_risk_profile_conservador(self):
        assert self.advisor.analyze_risk_profile({"risk_tolerance": 2}) == "conservador"

    def test_analyze_risk_profile_moderado(self):
        assert self.advisor.analyze_risk_profile({"risk_tolerance": 5}) == "moderado"

    def test_analyze_risk_profile_agresivo(self):
        assert self.advisor.analyze_risk_profile({"risk_tolerance": 9}) == "agresivo"

    def test_recommend_strategy_conservador(self):
        r = self.advisor.recommend_strategy({"risk_tolerance": 2}, {})
        assert r["strategy_id"] == "STG001"

    def test_recommend_strategy_moderado(self):
        r = self.advisor.recommend_strategy({"risk_tolerance": 5}, {})
        assert r["strategy_id"] == "STG002"

    def test_recommend_strategy_agresivo(self):
        r = self.advisor.recommend_strategy({"risk_tolerance": 9}, {})
        assert r["strategy_id"] == "STG003"

    def test_recommend_default_when_no_data(self):
        r = self.advisor.recommend_strategy({}, {})
        assert r["strategy_id"] == "STG002"

    @patch("main.RandomForestClassifier")
    @patch("main.train_test_split")
    @patch("main.accuracy_score")
    def test_train_model(self, mock_acc, mock_split, mock_rf_cls):
        mock_rf = MagicMock()
        mock_rf_cls.return_value = mock_rf
        mock_rf.predict.return_value = pd.Series(["STG001", "STG002"])
        mock_split.return_value = (
            pd.DataFrame({"a": [1]}), pd.DataFrame({"a": [2]}),
            pd.Series(["STG001"]), pd.Series(["STG002"])
        )
        self.advisor.data = pd.DataFrame({
            "user_risk_tolerance": [2, 8, 5],
            "market_volatility": [0.1, 0.7, 0.4],
            "protocol_apy": [0.03, 0.15, 0.08],
            "recommended_strategy": ["STG001", "STG003", "STG002"]
        })
        self.advisor.train_model()
        assert self.advisor.model is not None
        mock_rf.fit.assert_called_once()

    def test_recommend_strategy_with_trained_model(self):
        mock_model = MagicMock()
        mock_model.predict.return_value = ["STG003"]
        self.advisor.model = mock_model
        r = self.advisor.recommend_strategy({"risk_tolerance": 5}, {"volatility": 0.5, "protocol_apy": 0.08})
        assert r["strategy_id"] == "STG003"
