#!/usr/bin/env python3
"""
QuantumFolio Demo - Auto-run quantum predictions
Demonstrates both QAOA and VQE algorithms with full logging
"""

from quantum_cli import QuantumPortfolioPredictor
import time

def run_demo():
    """Run automated demo of both quantum algorithms"""
    print("\n" + "=" * 60)
    print("🚀 QuantumFolio - Automated Quantum Prediction Demo")
    print("=" * 60)
    
    # Initialize predictor
    predictor = QuantumPortfolioPredictor()
    
    print("\n🎯 Running QAOA Algorithm Demo...")
    result1 = predictor.predict_portfolio('QAOA')
    
    if result1:
        print(f"\n✅ {result1['algorithm']} Demo Complete!")
        
    time.sleep(2)  # Pause between algorithms
    
    print("\n🎯 Running VQE Algorithm Demo...")  
    result2 = predictor.predict_portfolio('VQE')
    
    if result2:
        print(f"\n✅ {result2['algorithm']} Demo Complete!")
        
    print("\n🎉 Demo Complete! Both quantum algorithms have been tested.")

if __name__ == '__main__':
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"❌ Demo error: {e}")
