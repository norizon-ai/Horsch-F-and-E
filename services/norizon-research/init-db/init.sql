-- =====================================================================
-- Norizon Authentication Database - Initial Schema
-- =====================================================================
-- This script runs automatically when the PostgreSQL container starts
-- for the first time. It creates the necessary tables for user auth.
-- =====================================================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    auth0_subject VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE,
    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Create index on auth0_subject for fast lookups
CREATE INDEX idx_users_auth0_subject ON users(auth0_subject);

-- Create index on email for lookups
CREATE INDEX idx_users_email ON users(email);

-- Create index on created_at for analytics queries
CREATE INDEX idx_users_created_at ON users(created_at DESC);

-- Insert a test user (optional - remove in production)
INSERT INTO users (auth0_subject, email, name)
VALUES ('auth0|test123', 'test@norizon.de', 'Test User')
ON CONFLICT (auth0_subject) DO NOTHING;

-- Create a function to update last_login automatically
CREATE OR REPLACE FUNCTION update_last_login()
RETURNS TRIGGER AS $$
BEGIN
    NEW.last_login = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Log schema creation
DO $$
BEGIN
    RAISE NOTICE 'Norizon authentication database initialized successfully';
END $$;
