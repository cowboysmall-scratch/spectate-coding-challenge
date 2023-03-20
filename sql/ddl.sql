
DROP TABLE IF EXISTS selection;
DROP TABLE IF EXISTS market;
DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS sport;



CREATE TABLE IF NOT EXISTS sport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    display_name TEXT,
    slug TEXT,
    sport_order INTEGER,
    active INTEGER
);


CREATE TABLE IF NOT EXISTS event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    event_type TEXT,
    status TEXT,
    slug TEXT,
    active INTEGER,
    sport_id INTEGER,
    FOREIGN KEY (sport_id) REFERENCES sport (id)
);


CREATE TABLE IF NOT EXISTS market (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    display_name TEXT,
    market_order INTEGER,
    schema INTEGER,
    columns INTEGER,
    active INTEGER,
    event_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES event (id)
);


CREATE TABLE IF NOT EXISTS selection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    outcome TEXT,
    active INTEGER,
    market_id INTEGER,
    FOREIGN KEY (market_id) REFERENCES market (id)
);



CREATE TRIGGER IF NOT EXISTS update_event_active
AFTER UPDATE OF active ON event
WHEN (SELECT COUNT(*) FROM event WHERE sport_id = new.sport_id AND active = 1) = 0
BEGIN
    UPDATE sport SET active = 0 WHERE id = new.sport_id;
END;


CREATE TRIGGER IF NOT EXISTS update_market_active
AFTER UPDATE OF active ON market
WHEN (SELECT COUNT(*) FROM market WHERE event_id = new.event_id AND active = 1) = 0
BEGIN
    UPDATE event SET active = 0 WHERE id = new.event_id;
END;


CREATE TRIGGER IF NOT EXISTS update_selection_active
AFTER UPDATE OF active ON selection
WHEN (SELECT COUNT(*) FROM selection WHERE market_id = new.market_id AND active = 1) = 0
BEGIN
    UPDATE market SET active = 0 WHERE id = new.market_id;
END;
