FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 8501
CMD uvicorn backend:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.address=0.0.0.0
