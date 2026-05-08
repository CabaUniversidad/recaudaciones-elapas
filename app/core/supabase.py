from supabase import create_client, Client
from app.core.config import settings

# El Service Key permite saltar políticas RLS para generar URLs firmadas
supabase_client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_KEY)