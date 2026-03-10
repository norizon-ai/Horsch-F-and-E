#!/bin/bash

# Norizon Research - Quick Start Script
# This script sets up and starts the entire platform

set -e

echo "🚀 Norizon Research - Quick Start"
echo "=================================="
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose not found. Please install Docker Compose first."
    exit 1
fi

echo "✅ Prerequisites met!"
echo ""

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created (you can customize it later)"
else
    echo "✅ .env file already exists"
fi

echo ""

# Ask which mode
echo "Select deployment mode:"
echo "1) Development (with hot reload)"
echo "2) Production"
echo ""
read -p "Enter choice [1-2]: " choice

case $choice in
    1)
        echo ""
        echo "🔧 Starting development environment..."
        echo ""
        docker-compose -f docker-compose.dev.yml up -d
        echo ""
        echo "✅ Development environment started!"
        echo ""
        echo "📍 Access points:"
        echo "   Frontend:     http://localhost:5173"
        echo "   API:          http://localhost:5000"
        echo "   Ollama:       http://localhost:11434"
        echo "   SearxNG:      http://localhost:8080"
        echo ""
        echo "📝 Note: First startup may take 5-10 minutes to download Ollama models"
        echo ""
        echo "📊 View logs:"
        echo "   docker-compose -f docker-compose.dev.yml logs -f"
        echo ""
        echo "🛑 To stop:"
        echo "   docker-compose -f docker-compose.dev.yml down"
        ;;
    2)
        echo ""
        echo "🏭 Building and starting production environment..."
        echo ""
        docker-compose build
        docker-compose up -d
        echo ""
        echo "✅ Production environment started!"
        echo ""
        echo "📍 Access point:"
        echo "   Frontend:     http://localhost:3000"
        echo ""
        echo "📝 Note: First startup may take 5-10 minutes to download Ollama models"
        echo ""
        echo "📊 View logs:"
        echo "   docker-compose logs -f"
        echo ""
        echo "🛑 To stop:"
        echo "   docker-compose down"
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "🎉 Happy researching!"
