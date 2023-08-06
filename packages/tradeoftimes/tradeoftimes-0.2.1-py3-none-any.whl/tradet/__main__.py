import tradet
import sys

app = tradet.TradeGameApp(sys.argv[1] if len(sys.argv) > 1 else None)
app.MainLoop()