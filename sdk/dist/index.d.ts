interface Strategy {
    id: string;
    name: string;
    description: string;
    apy: number;
    riskLevel: 'low' | 'medium' | 'high';
    protocols: string[];
}
interface RiskAnalysis {
    userProfile: string;
    riskScore: number;
    recommendations: string[];
}
interface Recommendation {
    strategyId: string;
    reason: string;
    expectedReturn: number;
}
declare class DefiAdvisorSDK {
    private baseUrl;
    constructor(baseUrl: string);
    getStrategies(): Promise<Strategy[]>;
    analyzeRisk(userAddress: string): Promise<RiskAnalysis>;
    getRecommendations(userAddress: string): Promise<Recommendation[]>;
}
export default DefiAdvisorSDK;
