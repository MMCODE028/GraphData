CREATE TABLE lastdata (
    data_id VARCHAR(255) PRIMARY KEY,
    co2factor FLOAT NOT NULL,
    created_at_date DATE NOT NULL,
    created_at_time TIME NOT NULL,
    day_energy FLOAT NOT NULL,
    id INTEGER NOT NULL,
    pac_sum FLOAT NOT NULL,
    pac_sum_counter INTEGER NOT NULL,
    pac_sum_temp FLOAT NOT NULL,
    power_counter INTEGER NOT NULL,	
    power_real FLOAT NOT NULL,	
    power_real_temp FLOAT NOT NULL,	
    reference VARCHAR(255) NOT NULL,	
    total_energy FLOAT NOT NULL,
    update_at_date DATE NOT NULL,
    update_at_time TIME NOT NULL
);