FROM python:3.12-slim-bookworm

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requirements
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]