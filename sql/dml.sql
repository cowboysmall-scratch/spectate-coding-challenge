
INSERT INTO sport
    (name, display_name, slug, sport_order, active)
VALUES
    ('SPORT_01_NAME', 'SPORT_01_DISPLAY_NAME', 'SPORT_01_SLUG', 1, True),
    ('SPORT_02_NAME', 'SPORT_02_DISPLAY_NAME', 'SPORT_02_SLUG', 2, True),
    ('SPORT_03_NAME', 'SPORT_03_DISPLAY_NAME', 'SPORT_03_SLUG', 3, False);


INSERT INTO event
    (name, event_type, status, slug, active, sport_id)
VALUES
    ('EVENT_01_NAME', 'EVENT_TYPE_01', 'PREPLAY', 'EVENT_01_SLUG', True,  1),
    ('EVENT_02_NAME', 'EVENT_TYPE_02', 'INPLAY',  'EVENT_02_SLUG', True,  1),
    ('EVENT_03_NAME', 'EVENT_TYPE_03', 'INPLAY',  'EVENT_03_SLUG', True,  2),
    ('EVENT_04_NAME', 'EVENT_TYPE_04', 'PREPLAY', 'EVENT_04_SLUG', False, 2),
    ('EVENT_05_NAME', 'EVENT_TYPE_05', 'INPLAY',  'EVENT_05_SLUG', False, 3),
    ('EVENT_06_NAME', 'EVENT_TYPE_06', 'PREPLAY', 'EVENT_06_SLUG', False, 3);


INSERT INTO market
    (name, display_name, market_order, schema, columns, active, event_id)
VALUES
    ('MARKET_01_NAME', 'MARKET_01_DISPLAY_NAME', 2, 1, 2, True,  1),
    ('MARKET_02_NAME', 'MARKET_02_DISPLAY_NAME', 2, 1, 2, True,  1),
    ('MARKET_03_NAME', 'MARKET_03_DISPLAY_NAME', 2, 1, 2, True,  2),
    ('MARKET_04_NAME', 'MARKET_04_DISPLAY_NAME', 2, 1, 2, False, 2),
    ('MARKET_05_NAME', 'MARKET_05_DISPLAY_NAME', 2, 1, 2, False, 3),
    ('MARKET_06_NAME', 'MARKET_06_DISPLAY_NAME', 2, 1, 2, False, 3);


INSERT INTO selection
    (name, price, outcome, active, market_id)
VALUES
    ('SELECTION_01_NAME', 9.99, 'WIN', True,  1),
    ('SELECTION_02_NAME', 9.99, 'WIN', True,  1),
    ('SELECTION_03_NAME', 9.99, 'WIN', True,  2),
    ('SELECTION_04_NAME', 9.99, 'WIN', False, 2),
    ('SELECTION_05_NAME', 9.99, 'WIN', False, 3),
    ('SELECTION_06_NAME', 9.99, 'WIN', False, 3);
