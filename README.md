# Global Signal Server

Ushbu loyihaning maqsadi:
- Cloud’da signal server ishlatish
- Agent o‘z-o‘zidan signal yuboradi
- Log saqlaydi
- Dashboard orqali ko‘rsatadi

## Deploy qilish (Render yoki Railway)

1. Repository’ni GitHub’ga push qiling.
2. Render yoki Railway’da yangi Web Service yarating:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
3. Agent uchun alohida Worker yaratib `agent.py` ishga tushiring.
4. `dashboard.html` ni browserda oching.

Bu tizim 24/7 ishlaydi, va siz Signal yuborishingiz bilan hamma loglanadi.
