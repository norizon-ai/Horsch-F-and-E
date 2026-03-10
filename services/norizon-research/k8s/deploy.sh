#!/bin/bash

# Norizon Research - Kubernetes Deployment Script
# Usage: ./deploy.sh [environment]
# Example: ./deploy.sh production

set -e

ENVIRONMENT=${1:-staging}
NAMESPACE="norizon-research"

echo "🚀 Deploying Norizon Research to Kubernetes ($ENVIRONMENT)"
echo "=================================================="

# Check kubectl is available
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl not found. Please install kubectl first."
    exit 1
fi

# Create namespace
echo "📦 Creating namespace..."
kubectl apply -f namespace.yaml

# Create secrets (if not already created)
echo "🔐 Creating secrets..."
if kubectl get secret norizon-research-secrets -n $NAMESPACE &> /dev/null; then
    echo "   Secrets already exist, skipping..."
else
    echo "   ⚠️  Please update 02-secrets.yaml with your OpenAI API key first!"
    echo "   Then run: kubectl apply -f 02-secrets.yaml"
    echo "   Continuing deployment (this will fail if secrets don't exist)..."
fi

# Deploy SearxNG
echo "🔍 Deploying SearxNG..."
kubectl apply -f searxng-deployment.yaml

# Wait for SearxNG to be ready
echo "⏳ Waiting for SearxNG to be ready..."
kubectl wait --for=condition=ready pod -l app=norizon-searxng -n $NAMESPACE --timeout=120s

# Deploy DeepResearch
echo "🧠 Deploying DeepResearch..."
kubectl apply -f deepresearch-deployment.yaml

# Wait for DeepResearch to be ready
echo "⏳ Waiting for DeepResearch to be ready..."
kubectl wait --for=condition=ready pod -l app=norizon-deepresearch -n $NAMESPACE --timeout=180s

# Deploy Proxy
echo "🔄 Deploying Proxy..."
kubectl apply -f proxy-deployment.yaml

# Wait for Proxy to be ready
echo "⏳ Waiting for Proxy to be ready..."
kubectl wait --for=condition=ready pod -l app=norizon-proxy -n $NAMESPACE --timeout=120s

# Deploy Frontend
echo "🎨 Deploying Frontend..."
kubectl apply -f frontend-deployment.yaml

# Wait for Frontend to be ready
echo "⏳ Waiting for Frontend to be ready..."
kubectl wait --for=condition=ready pod -l app=norizon-research-frontend -n $NAMESPACE --timeout=120s

# Apply HPA (Horizontal Pod Autoscaler)
echo "📊 Applying autoscaling policies..."
kubectl apply -f hpa.yaml

# Show deployment status
echo ""
echo "✅ Deployment complete!"
echo "=================================================="
echo "📋 Deployment Status:"
kubectl get pods -n $NAMESPACE
echo ""
echo "🌐 Services:"
kubectl get svc -n $NAMESPACE
echo ""
echo "🔗 Ingress:"
kubectl get ingress -n $NAMESPACE
echo ""
echo "📊 HPA Status:"
kubectl get hpa -n $NAMESPACE
echo ""
echo "🎉 Norizon Research is now deployed!"
echo ""
echo "Access the application:"
INGRESS_HOST=$(kubectl get ingress -n $NAMESPACE -o jsonpath='{.items[0].spec.rules[0].host}')
if [ -n "$INGRESS_HOST" ]; then
    echo "🌐 https://$INGRESS_HOST"
else
    echo "🌐 Use port-forward: kubectl port-forward -n $NAMESPACE svc/norizon-research-frontend-service 3000:80"
fi
