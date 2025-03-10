-- !!CHANGE THE PASSWORD!!
CREATE USER app_user WITH PASSWORD 'securepassword';

-- Initial Permissions
GRANT CONNECT ON DATABASE your_db TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
-- Give permission to future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO app_user;r;
