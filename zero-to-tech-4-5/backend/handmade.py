from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    "heroTitle": "关于我（来自后端）",  # → 临时加的标记，验证完删掉
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
    "featuredWork": {
        "kicker": "作品",
        "title": "文字实验室",
        "copy": "拼音和情绪，挖掘中文里的细节",
        "linkLabel": "打开作品",
    },
    "identity": {
        "motto": "已识乾坤大，尤怜草木青",
        "learning": "零到全栈",
    },
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/profile":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            body = json.dumps(profile, ensure_ascii=False)  # ensure_ascii=False：让中文原样输出
            self.wfile.write(body.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

print("后端已启动：http://localhost:8000/api/profile")
HTTPServer(("", 8000), Handler).serve_forever()
