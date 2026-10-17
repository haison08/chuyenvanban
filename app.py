import os
import uuid
import traceback
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory
from werkzeug.utils import secure_filename
from converter import convert_document

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
os.makedirs(UPLOAD_DIR, exist_ok=True)
env_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#') and '=' in line:
                k, v = line.strip().split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())

DEFAULT_API_KEY = os.environ.get("GEMINI_API_KEY", "")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/convert', methods=['POST'])
def handle_convert():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': 'Không tìm thấy file tải lên.'}), 400
            
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return jsonify({'success': False, 'message': 'Tên file rỗng.'}), 400
            
        api_key = request.form.get('apiKey', '').strip() or os.getenv('GEMINI_API_KEY', '') or DEFAULT_API_KEY
        remove_signatures = request.form.get('removeSignatures', 'true').lower() == 'true'
        font_name = request.form.get('fontName', 'Times New Roman')
        
        file_id = str(uuid.uuid4())[:8]
        filename = secure_filename(uploaded_file.filename) or f"document_{file_id}.pdf"
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext not in ('.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.webp'):
            return jsonify({'success': False, 'message': 'Chỉ hỗ trợ file PDF hoặc ảnh (PNG, JPG, JPEG, TIFF).'}), 400
            
        saved_input_path = os.path.join(UPLOAD_DIR, f"{file_id}_{filename}")
        uploaded_file.save(saved_input_path)
        
        output_name = f"Chuyen_Doi_{os.path.splitext(filename)[0]}_{file_id}.docx"
        output_docx_path = os.path.join(OUTPUT_DIR, output_name)
        
        options = {
            'remove_signatures': remove_signatures,
            'font_name': font_name,
            'is_demo': False
        }
        
        result = convert_document(saved_input_path, output_docx_path, api_key=api_key, options=options)
        
        return jsonify({
            'success': True,
            'message': 'Chuyển đổi thành công 100%!',
            'download_url': f'/api/download/{output_name}',
            'filename': output_name,
            'page_count': result.get('page_count', 1),
            'pages_preview': result.get('pages_preview', [])
        })
        
    except Exception as e:
        traceback.print_exc()
        err_str = str(e)
        if "503" in err_str or "high demand" in err_str.lower():
            friendly_msg = "Máy chủ AI đang có lượng truy cập đột biến tạm thời (Spikes in demand). Hệ thống đã tự động chuyển sang mô hình ổn định, bạn hãy bấm thử lại nhé!"
        else:
            friendly_msg = f"Lỗi chuyển đổi: {err_str}"
        return jsonify({'success': False, 'message': friendly_msg}), 500

@app.route('/api/demo', methods=['POST'])
def handle_demo():
    try:
        file_id = str(uuid.uuid4())[:8]
        output_name = f"Mau_Ke_hoach_Ngay_hoi_Dai_doan_ket_2026_{file_id}.docx"
        output_docx_path = os.path.join(OUTPUT_DIR, output_name)
        
        options = {
            'remove_signatures': True,
            'font_name': 'Times New Roman',
            'is_demo': True
        }
        
        # We can use the existing sample document
        sample_pdf = os.path.join(BASE_DIR, "media_sample.pdf")
        user_uploaded_sample = "/Users/haisonnguyenphuc/.gemini/antigravity-ide/brain/f03321b5-4b4f-425e-b066-8475e4f09023/.user_uploaded/media_1792246606151.pdf"
        target_input = user_uploaded_sample if os.path.exists(user_uploaded_sample) else sample_pdf
        
        result = convert_document(target_input, output_docx_path, options=options)
        
        return jsonify({
            'success': True,
            'message': 'Đã tạo file mẫu thành công 100%!',
            'download_url': f'/api/download/{output_name}',
            'filename': output_name,
            'page_count': result.get('page_count', 6),
            'pages_preview': result.get('pages_preview', [])
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({'success': False, 'message': f'Lỗi demo: {str(e)}'}), 500

@app.route('/api/download/<filename>')
def download_file(filename):
    file_path = os.path.join(OUTPUT_DIR, secure_filename(filename))
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=filename)
    return jsonify({'success': False, 'message': 'File không tồn tại hoặc đã hết hạn.'}), 404

@app.route('/temp_pages/<path:filename>')
def serve_temp_pages(filename):
    temp_dir = os.path.join(OUTPUT_DIR, "temp_pages")
    return send_from_directory(temp_dir, filename)

if __name__ == '__main__':
    port = 5001
    print(f"🚀 PDF to Word AI Converter Web App starting at http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
