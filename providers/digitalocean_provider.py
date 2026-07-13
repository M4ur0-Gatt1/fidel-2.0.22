"""DigitalOcean GenAI Platform — Serverless Inference (API compatible OpenAI).

Endpoint correcto: https://inference.do-ai.run/v1
Da acceso, detrás de una sola base URL, a modelos de Meta (Llama), DeepSeek,
Mistral, OpenAI y Anthropic. La lista COMPLETA se trae en vivo de /models.
Auth: token personal de DigitalOcean o "model access key"
(https://cloud.digitalocean.com/gen-ai/model-access-keys).

Nota: `api.paperspace.io` era el endpoint viejo y devolvía una lista limitada;
por eso "solo mostraba algunos modelos". config.py migra el base_url viejo.
"""
from providers.base import OpenAICompatProvider


class DigitalOceanProvider(OpenAICompatProvider):
    BASE_URL = "https://inference.do-ai.run/v1"
    # fallback si /models no responde; la lista REAL (todos los modelos a los que
    # tenés acceso) se trae en vivo de /models. OJO con el formato de los IDs de
    # DO: 'openai-gpt-4o-mini', 'llama3-8b-instruct' (confirmados en la doc), NO
    # 'llama3.3-70b-instruct' con puntos → eso da 403 "not available".
    MODELS = ["openai-gpt-4o-mini", "openai-gpt-4o", "llama3-8b-instruct",
              "llama3.3-70b-instruct", "anthropic-claude-3.5-sonnet",
              "deepseek-r1-distill-llama-70b"]

    @staticmethod
    def provider_name(): return "DigitalOcean"

    @staticmethod
    def default_model(): return "openai-gpt-4o-mini"
