CREATE TABLE IF NOT EXISTS event_keeper (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event TEXT NOT NULL,
    begin_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_date DATETIME NOT NULL,
    active INTEGER DEFAULT 1
);

