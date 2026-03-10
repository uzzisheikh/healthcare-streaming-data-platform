from pyspark.sql import SparkSession
import pyodbc

spark = SparkSession.builder.appName("BatchProcessing").getOrCreate()

# Load historical clinical data
df = spark.read.csv("data/historical_clinical_data.csv", header=True, inferSchema=True)

# Transform
df_transformed = df.groupBy("event_type").count()

# Write to SQL Server
conn_str = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=HealthcareDB;UID=sa;PWD=your_password'
conn = pyodbc.connect(conn_str)
for row in df_transformed.collect():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clinical_event_summary (event_type, count) VALUES (?, ?)", row.event_type, row['count'])
    conn.commit()
conn.close()
