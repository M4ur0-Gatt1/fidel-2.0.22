"""Qwen Provider (Token Plan, API compatible OpenAI)."""
from providers.base import OpenAICompatProvider


class QwenProvider(OpenAICompatProvider):
    # Token Plan requiere URL específico con 'token-plan' en el dominio
    BASE_URL = "https://token-plan.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
    # Modelos disponibles en Token Plan (actualizado según /models)
    MODELS = ["qwen3.8-max-preview", "qwen3.7-max", "qwen3.7-plus", "qwen3.6-flash", "glm-5.2"]

    @staticmethod
    def provider_name(): return "Qwen"
    @staticmethod
    def default_model(): return "qwen3.7-plus"
