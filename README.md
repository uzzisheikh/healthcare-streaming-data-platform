# Healthcare Streaming Data Platform

This project demonstrates a hybrid Data Lakehouse platform for healthcare data, combining Spark batch processing and Kafka-powered streaming pipelines. It ingests clinical events into Oracle and SQL Server warehouses and analytics layers, providing timely clinical and operational insights.

## Features
- Kafka producer and consumer for real-time clinical event ingestion
- Spark batch and streaming jobs
- Integration with Oracle/SQL Server for structured storage
- Modular, scalable architecture for analytics and ML

## Technologies
- Python, PySpark
- Apache Kafka
- Oracle and SQL Server
- YAML for configuration

## How to Run
1. Set up Kafka and topics as per config.yaml
2. Start the Kafka producer to simulate clinical events
3. Run Spark batch and streaming jobs
4. Connect to SQL Server/Oracle to verify data ingestion
