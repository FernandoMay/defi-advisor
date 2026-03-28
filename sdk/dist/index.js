"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
class DefiAdvisorSDK {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }
    getStrategies() {
        return __awaiter(this, void 0, void 0, function* () {
            // Simula una llamada a la API para obtener estrategias DeFi
            console.log('Fetching DeFi strategies...');
            const response = yield fetch(`${this.baseUrl}/strategies`);
            if (!response.ok) {
                throw new Error(`Error fetching strategies: ${response.statusText}`);
            }
            return response.json();
        });
    }
    analyzeRisk(userAddress) {
        return __awaiter(this, void 0, void 0, function* () {
            // Simula una llamada a la API para analizar el riesgo del usuario
            console.log(`Analyzing risk for user: ${userAddress}...`);
            const response = yield fetch(`${this.baseUrl}/risk-analysis`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ userAddress }),
            });
            if (!response.ok) {
                throw new Error(`Error analyzing risk: ${response.statusText}`);
            }
            return response.json();
        });
    }
    getRecommendations(userAddress) {
        return __awaiter(this, void 0, void 0, function* () {
            // Simula una llamada a la API para obtener recomendaciones personalizadas
            console.log(`Fetching recommendations for user: ${userAddress}...`);
            const response = yield fetch(`${this.baseUrl}/recommendations?userAddress=${userAddress}`);
            if (!response.ok) {
                throw new Error(`Error fetching recommendations: ${response.statusText}`);
            }
            return response.json();
        });
    }
}
exports.default = DefiAdvisorSDK;
