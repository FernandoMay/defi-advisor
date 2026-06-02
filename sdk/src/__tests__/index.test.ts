import DefiAdvisorSDK from '../index';

describe('DefiAdvisorSDK', () => {
  const sdk = new DefiAdvisorSDK('https://api.example.com');

  beforeEach(() => {
    global.fetch = jest.fn();
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  it('should construct with base URL', () => {
    expect(sdk).toBeDefined();
  });

  it('should fetch strategies successfully', async () => {
    const mockStrategies = [{ id: 'STG001', name: 'Staking', apy: 0.05, riskLevel: 'low', protocols: ['Aave'], description: 'test' }];
    (global.fetch as jest.Mock).mockResolvedValue({ ok: true, json: () => Promise.resolve(mockStrategies) });

    const result = await sdk.getStrategies();
    expect(result).toEqual(mockStrategies);
    expect(global.fetch).toHaveBeenCalledWith('https://api.example.com/strategies');
  });

  it('should throw on strategies fetch error', async () => {
    (global.fetch as jest.Mock).mockResolvedValue({ ok: false, statusText: 'Not Found' });
    await expect(sdk.getStrategies()).rejects.toThrow('Error fetching strategies: Not Found');
  });

  it('should analyze risk for user address', async () => {
    const mockRisk = { userProfile: 'moderado', riskScore: 5, recommendations: ['STG002'] };
    (global.fetch as jest.Mock).mockResolvedValue({ ok: true, json: () => Promise.resolve(mockRisk) });

    const result = await sdk.analyzeRisk('0x123');
    expect(result).toEqual(mockRisk);
    expect(global.fetch).toHaveBeenCalledWith('https://api.example.com/risk-analysis', expect.objectContaining({ method: 'POST' }));
  });

  it('should throw on risk analysis error', async () => {
    (global.fetch as jest.Mock).mockResolvedValue({ ok: false, statusText: 'Bad Request' });
    await expect(sdk.analyzeRisk('0x123')).rejects.toThrow('Error analyzing risk: Bad Request');
  });

  it('should fetch recommendations', async () => {
    const mockRecs = [{ strategyId: 'STG001', reason: 'good', expectedReturn: 0.1 }];
    (global.fetch as jest.Mock).mockResolvedValue({ ok: true, json: () => Promise.resolve(mockRecs) });

    const result = await sdk.getRecommendations('0x456');
    expect(result).toEqual(mockRecs);
  });
});
