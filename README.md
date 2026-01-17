Week 1 – Data Ingestion & Cleaning
- Loaded raw telecom churn data into Apache Spark
- Performed schema validation and row count checks
- Cleaned data (type casting, null handling)
- Repartitioned data for scalability
- Prepared target variable for ML

Week 2 – Feature Engineering & DAG Analysis
- Used Spark SQL and window functions to engineer user-level features
- Created rolling averages and aggregate metrics
- Applied business logic features (e.g., high-value customers)
- Analyzed Spark execution plan (DAG) to identify bottlenecks
- Tuned partitions and cached data for performance

Week 3 – Distributed Model Training & Evaluation
- Built ML pipelines using Spark MLlib
- Trained Logistic Regression and Random Forest models
- Evaluated models using BinaryClassificationEvaluator (AUC)
- Compared training time and scalability
- Saved the best-performing model for production use

Week 4 – Production-Style Batch Prediction
- Loaded the saved Spark ML pipeline
- Simulated new customer data for batch inference
- Generated churn probability predictions
- Exported results as CSV to simulate a daily batch job

# Technologies Used
- Apache Spark
- Spark SQL
- Spark MLlib
- PySpark
- Google Colab
- GitHub

Key Highlights
- Scalable data processing using Apache Spark
- SQL-based feature engineering at scale
- DAG-based performance analysis
- Distributed machine learning
- Production-style batch inference pipeline


---

## ✅ Conclusion
This project demonstrates how Apache Spark can be used to build an **end-to-end, scalable machine learning pipeline**, from raw data ingestion to production-ready batch predictions.
