import unittest
import json
from datetime import datetime, timedelta
from trading_strategy import backtest_sma, backtest_bb, backtest_macd

class TestTradingStrategy(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        self.sample_data = []
        base_date = datetime(2023, 1, 1)
        
        # Generate 100 days of sample data
        for i in range(100):
            current_date = base_date + timedelta(days=i)
            self.sample_data.append({
                'Date': current_date.strftime('%Y-%m-%d'),
                'Close': 100 + i  # Simple upward trend
            })

    def test_backtest_sma_unit(self):
        """Unit test for SMA strategy"""
        trades, metrics = backtest_sma(self.sample_data)
        
        # Convert JSON strings back to dictionaries
        trades = json.loads(trades)
        metrics = json.loads(metrics)
        
        # Basic assertions
        self.assertIsInstance(trades, list)
        self.assertIsInstance(metrics, dict)
        self.assertIn('total_return', metrics)
        self.assertIn('total_trades', metrics)
        
        # Check that trades have required fields
        if trades:
            first_trade = trades[0]
            required_fields = {'date', 'type', 'shares', 'price', 'amount', 'balance', 'return'}
            self.assertTrue(all(field in first_trade for field in required_fields))

    def test_backtest_bb_unit(self):
        """Unit test for Bollinger Bands strategy"""
        trades, metrics = backtest_bb(self.sample_data)
        
        trades = json.loads(trades)
        metrics = json.loads(metrics)
        
        self.assertIsInstance(trades, list)
        self.assertIsInstance(metrics, dict)
        self.assertIn('total_return', metrics)
        self.assertIn('total_trades', metrics)

    def test_backtest_macd_unit(self):
        """Unit test for MACD strategy"""
        trades, metrics = backtest_macd(self.sample_data)
        
        trades = json.loads(trades)
        metrics = json.loads(metrics)
        
        self.assertIsInstance(trades, list)
        self.assertIsInstance(metrics, dict)
        self.assertIn('total_return', metrics)
        self.assertIn('total_trades', metrics)

class TestTradingStrategyIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.historical_data = []
        base_date = datetime(2023, 1, 1)
        
        # Generate more realistic price data with some volatility
        price = 100
        for i in range(200):
            current_date = base_date + timedelta(days=i)
            # Add some randomness to price movements
            import random
            price_change = random.uniform(-2, 2)
            price += price_change
            
            cls.historical_data.append({
                'Date': current_date.strftime('%Y-%m-%d'),
                'Close': price
            })

    def test_strategy_comparison(self):
        """Integration test comparing all strategies"""
        # Run all strategies
        sma_trades, sma_metrics = backtest_sma(self.historical_data)
        bb_trades, bb_metrics = backtest_bb(self.historical_data)
        macd_trades, macd_metrics = backtest_macd(self.historical_data)
        
        # Convert to dictionaries
        sma_metrics = json.loads(sma_metrics)
        bb_metrics = json.loads(bb_metrics)
        macd_metrics = json.loads(macd_metrics)
        
        # Test that all strategies executed successfully
        self.assertGreaterEqual(sma_metrics['total_trades'], 0)
        self.assertGreaterEqual(bb_metrics['total_trades'], 0)
        self.assertGreaterEqual(macd_metrics['total_trades'], 0)
        
        # Test that final balances are calculated
        self.assertGreater(sma_metrics['final_balance'], 0)
        self.assertGreater(bb_metrics['final_balance'], 0)
        self.assertGreater(macd_metrics['final_balance'], 0)

    def test_strategy_edge_cases(self):
        """Integration test for edge cases"""
        # Test with minimal data
        minimal_data = self.historical_data[:60]  # Only 60 days of data
        
        # All strategies should handle minimal data without errors
        try:
            backtest_sma(minimal_data)
            backtest_bb(minimal_data)
            backtest_macd(minimal_data)
        except Exception as e:
            self.fail(f"Strategy failed with minimal data: {str(e)}")
        
        # Test with different initial balances
        try:
            backtest_bb(self.historical_data, initial_balance=1000)
            backtest_macd(self.historical_data, initial_balance=1000000)
        except Exception as e:
            self.fail(f"Strategy failed with different initial balance: {str(e)}")

if __name__ == '__main__':
    unittest.main() 