import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://vpaznvslotfbdqwptizp.supabase.co';
const supabaseKey =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZwYXpudnNsb3RmYmRxd3B0aXpwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg0MjIyOTMsImV4cCI6MjAyMzk5ODI5M30.f6PokQiuDqVtTRM0yZqJWvuWtbJBbApxIWfHpJXPyD0';

export const supabase = createClient(supabaseUrl, supabaseKey);
