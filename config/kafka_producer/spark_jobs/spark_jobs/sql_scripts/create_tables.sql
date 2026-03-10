CREATE TABLE clinical_event_summary (
    event_type VARCHAR(50),
    count INT
);

CREATE TABLE clinical_events (
    patient_id INT,
    event_type VARCHAR(50),
    timestamp FLOAT
);
