#!/usr/bin/env python3
"""
Script hỗ trợ triển khai Cloudflare Worker trực tiếp qua Cloudflare REST API
Sử dụng: python3 deploy_worker.py <CLOUDFLARE_API_TOKEN> [ACCOUNT_ID]
"""
import sys
import json
import urllib.request
import os

WORKER_NAME = "gemini-proxy"
SCRIPT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cloudflare_worker.js")

def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python3 deploy_worker.py <CLOUDFLARE_API_TOKEN> [ACCOUNT_ID]")
        return 1

    api_token = sys.argv[1].strip()
    account_id = sys.argv[2].strip() if len(sys.argv) > 2 else ""

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # 1. Nếu chưa có account_id, tự động lấy qua API /accounts
    if not account_id:
        print("🔍 Đang tìm Account ID từ Cloudflare API Token...")
        req = urllib.request.Request("https://api.cloudflare.com/client/v4/accounts", headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                if data.get("success") and data.get("result"):
                    account_id = data["result"][0]["id"]
                    account_name = data["result"][0]["name"]
                    print(f"✅ Tìm thấy Account: {account_name} (ID: {account_id})")
                else:
                    print("❌ Không tìm thấy Account nào. Vui lòng kiểm tra quyền của Token (Workers Scripts: Edit).")
                    return 1
        except Exception as e:
            print(f"❌ Lỗi khi lấy Account ID: {e}")
            return 1

    # 2. Đọc mã nguồn worker
    with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
        worker_code = f.read()

    # 3. Đẩy mã nguồn lên Cloudflare Worker
    print(f"🚀 Đang triển khai Worker '{WORKER_NAME}' lên Cloudflare...")
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{WORKER_NAME}"
    upload_headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/javascript"
    }
    req = urllib.request.Request(url, data=worker_code.encode("utf-8"), headers=upload_headers, method="PUT")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            if data.get("success"):
                print("✅ Triển khai mã nguồn Worker thành công!")
            else:
                print(f"❌ Triển khai thất bại: {data.get('errors')}")
                return 1
    except Exception as e:
        if hasattr(e, "read"):
            print(f"❌ Lỗi API: {e.read().decode()}")
        else:
            print(f"❌ Lỗi khi tải lên: {e}")
        return 1

    # 4. Kích hoạt subdomain workers.dev cho worker
    print("🌐 Đang kích hoạt subdomain workers.dev...")
    subdomain_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{WORKER_NAME}/subdomain"
    subdomain_payload = json.dumps({"enabled": True}).encode("utf-8")
    req = urllib.request.Request(subdomain_url, data=subdomain_payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            print("✅ Đã bật workers.dev thành công!")
    except Exception as e:
        print(f"⚠️ Lưu ý về subdomain: {e}")

    # 5. Lấy subdomain URL
    subdomain_info_url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/subdomain"
    req = urllib.request.Request(subdomain_info_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            subdomain_data = json.loads(resp.read().decode())
            subdomain = subdomain_data.get("result", {}).get("subdomain", "")
            if subdomain:
                final_url = f"https://{WORKER_NAME}.{subdomain}.workers.dev"
                print("\n" + "="*50)
                print(f"🎉 URL Worker của bạn là:\n👉 {final_url}")
                print("="*50)
    except Exception as e:
        print(f"⚠️ Không lấy được tên subdomain: {e}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
