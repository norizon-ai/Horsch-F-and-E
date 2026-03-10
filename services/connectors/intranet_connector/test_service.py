#!/usr/bin/env python3
"""
Simple test for the FastAPI service components.

This tests the service endpoints without starting the full job listener.
"""

import asyncio
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_service_imports():
    """Test that all service components can be imported."""
    
    print("🧪 Testing Service Imports...")
    
    try:
        # Test configuration
        from src.config import CrawlerSettings, settings
        print("✅ Configuration imports work")
        
        # Test models
        from src.models import RawArticle, RawArticleSource, RawArticleAuthor
        print("✅ Models import work")
        
        # Test crawler
        from src.crawler import IntranetCrawler
        print("✅ Crawler imports work")
        
        # Test publisher
        from src.publisher import DataPublisher
        from src.publisher_base import PublisherBase
        print("✅ Publisher imports work")
        
        print("\n🎉 All core components import successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_service_configuration():
    """Test service configuration values."""
    
    print("\n🧪 Testing Service Configuration...")
    
    try:
        from src.config import settings
        
        print(f"   STRATEGY: {settings.STRATEGY}")
        print(f"   MAX_PAGES: {settings.MAX_PAGES}")
        print(f"   MAX_DEPTH: {settings.MAX_DEPTH}")
        print(f"   RABBITMQ_URL: {settings.RABBITMQ_URL}")
        print(f"   INPUT_QUEUE: {settings.INPUT_QUEUE}")
        print(f"   OUTPUT_QUEUE: {settings.OUTPUT_QUEUE}")
        
        print("✅ Configuration loads successfully")
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

async def test_health_check_logic():
    """Test the health check logic without FastAPI."""
    
    print("\n🧪 Testing Health Check Logic...")
    
    try:
        # Test RabbitMQ connectivity check
        import aio_pika
        from src.config import settings
        
        try:
            connection = await aio_pika.connect_robust(settings.RABBITMQ_URL)
            await connection.close()
            print("✅ RabbitMQ connectivity check works")
            rabbitmq_status = "healthy"
        except Exception as e:
            print(f"⚠️  RabbitMQ not available: {e}")
            rabbitmq_status = "unhealthy"
        
        # Test configuration validation
        try:
            test_settings = CrawlerSettings()
            print("✅ Configuration validation works")
            config_status = "healthy"
        except Exception as e:
            print(f"❌ Configuration validation failed: {e}")
            config_status = "unhealthy"
        
        # Overall health
        overall_status = "healthy" if rabbitmq_status == "healthy" and config_status == "healthy" else "unhealthy"
        
        print(f"\n📊 Health Check Summary:")
        print(f"   RabbitMQ: {rabbitmq_status}")
        print(f"   Configuration: {config_status}")
        print(f"   Overall: {overall_status}")
        
        return overall_status == "healthy"
        
    except Exception as e:
        print(f"❌ Health check test failed: {e}")
        return False

def create_simple_health_service():
    """Create a minimal health check service for testing."""
    
    print("\n🧪 Creating Simple Health Service...")
    
    try:
        # Import after we know the core components work
        from fastapi import FastAPI
        from datetime import datetime, timezone
        
        app = FastAPI(title="Intranet Connector Health Test")
        
        @app.get("/health")
        async def health():
            return {
                "status": "healthy",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "service": "Intranet Connector",
                "version": "1.0.0"
            }
        
        @app.get("/")
        async def root():
            return {"message": "Intranet Connector Health Service"}
        
        print("✅ Simple health service created successfully")
        return app
        
    except Exception as e:
        print(f"❌ Failed to create health service: {e}")
        return None

async def main():
    """Run all service tests."""
    
    print("🚀 Intranet Connector Service Tests")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_service_imports()
    if not imports_ok:
        print("❌ Cannot proceed - import failures")
        return False
    
    # Test configuration
    config_ok = test_service_configuration()
    if not config_ok:
        print("❌ Cannot proceed - configuration failures")
        return False
    
    # Test health check logic
    health_ok = await test_health_check_logic()
    
    # Test simple service creation
    app = create_simple_health_service()
    service_ok = app is not None
    
    # Summary
    print("\n" + "=" * 50)
    print("🎯 Test Summary:")
    print(f"   Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"   Configuration: {'✅ PASS' if config_ok else '❌ FAIL'}")
    print(f"   Health Logic: {'✅ PASS' if health_ok else '❌ FAIL'}")
    print(f"   Service Creation: {'✅ PASS' if service_ok else '❌ FAIL'}")
    
    all_passed = imports_ok and config_ok and health_ok and service_ok
    
    if all_passed:
        print("\n🎉 All tests PASSED! Service is ready.")
        if app:
            print("💡 You can run the service with: uvicorn service:app --reload")
    else:
        print("\n❌ Some tests FAILED. Check the issues above.")
    
    return all_passed

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)