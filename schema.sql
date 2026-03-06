-- Create the tracking table
CREATE TABLE suivi_brossage (
  id            BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  date_reponse  TIMESTAMPTZ NOT NULL DEFAULT now(),
  brossages     INTEGER NOT NULL CHECK (brossages IN (0, 1, 2))
);

-- Enable Row Level Security
ALTER TABLE suivi_brossage ENABLE ROW LEVEL SECURITY;

-- Allow anyone to read entries (no login required)
CREATE POLICY "anon_select" ON suivi_brossage
  FOR SELECT TO anon USING (true);

-- Allow anyone to insert entries (no login required)
CREATE POLICY "anon_insert" ON suivi_brossage
  FOR INSERT TO anon WITH CHECK (true);
