from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.ia import envioMensagem
import json

@csrf_exempt
def analyze_performance(request):
    """
    Rota para receber resumo do desempenho e gerar recomendação via IA.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            summary = data.get("summary", "")

            if not summary:
                return JsonResponse({"error": "Campo 'summary' é obrigatório."}, status=400)

            result = envioMensagem(summary)
            return JsonResponse({"recommendation": result})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método não permitido."}, status=405)
