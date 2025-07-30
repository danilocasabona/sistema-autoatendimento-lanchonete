#!/bin/bash

echo "Verificando se o metrics-server está instalado..."
if ! kubectl get deployment metrics-server -n kube-system >/dev/null 2>&1; then
  echo "Instalando metrics-server..."
  kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
  echo "Aguardando metrics-server iniciar..."
  kubectl wait --for=condition=available deployment/metrics-server -n kube-system --timeout=120s
else
  echo "metrics-server já está instalado."
fi

echo "Aplicando configuração --kubelet-insecure-tls no metrics-server..."
kubectl -n kube-system patch deployment metrics-server \
  --type='json' \
  -p='[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]' 2>/dev/null || \
kubectl -n kube-system patch deployment metrics-server \
  --type='json' \
  -p='[{"op":"replace","path":"/spec/template/spec/containers/0/args/6","value":"--kubelet-insecure-tls"}]' 2>/dev/null || \
echo "Parâmetro --kubelet-insecure-tls já presente ou não foi necessário alterar."

echo "Aplicando manifestos Kubernetes..."
kubectl apply -f k8s/

echo "Aguardando pods da aplicação subirem..."
kubectl wait --for=condition=ready pod -l app=lanchonete-app --timeout=120s

echo "Fazendo port-forward para http://localhost:8000 ..."
kubectl port-forward service/lanchonete-app-service 8000:80 &
PORT_FORWARD_PID=$!

echo "Aguardando 5 segundos para garantir que o serviço está disponível..."
sleep 5

echo "Testando endpoint principal com curl:"
curl -i http://localhost:8000/health

echo "Testando documentação Swagger:"
curl -I http://localhost:8000/docs

echo ""
echo "Acesse a documentação Swagger em: http://localhost:8000/docs"
echo "Para interromper o port-forward, use: kill $PORT_FORWARD_PID"