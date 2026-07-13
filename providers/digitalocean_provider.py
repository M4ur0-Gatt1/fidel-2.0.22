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
    # fallback si /models no responde; la lista real (todos los modelos con
    # acceso) se trae en vivo de /models
    MODELS = ["llama3.3-70b-instruct", "llama3-8b-instruct",
              "deepseek-r1-distill-llama-70b", "mistral-nemo-instruct-2407",
              "openai-gpt-4o", "anthropic-claude-3.5-sonnet"]

    @staticmethod
    def provider_name(): return "DigitalOcean"

    @staticmethod
    def default_model(): return "llama3.3-70b-instruct"
