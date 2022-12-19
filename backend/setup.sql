--Create our database table
CREATE TABLE task (
    id INTEGER PRIMARY KEY,
    summary VARCHAR(1024),
    description TEXT,
    is_active Boolean DEFAULT 1
);

-- Populate our table with some dummy data

INSERT INTO task (
    summary,
    description
 ) VALUES (
    "Take out the trash",
    "Take the trash out to the dumpster by the driveway"
 );

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash the car",
    "Either take the car ti the car wasghh or do it yourself"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "prepare lunch",
    "Make a wholesome meal"
);
