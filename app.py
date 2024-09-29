from flask import Flask, request, jsonify

app = Flask(__name__)

# Function để đọc các mã đã kích hoạt từ file
def read_activated_keys():
    try:
        with open('activated_keys.txt', 'r') as f:
            # Đọc các dòng và loại bỏ khoảng trắng thừa (nếu có)
            activated_keys = [line.strip() for line in f.readlines()]
            return activated_keys
    except FileNotFoundError:
        # Nếu file không tồn tại, trả về danh sách rỗng
        return []

# API kiểm tra mã kích hoạt
@app.route('/api/verify', methods=['POST'])
def verify_activation():
    # Đọc mã kích hoạt từ request
    data = request.get_json()
    activation_code = data.get('activation_code')
    
    # Đọc danh sách các mã đã kích hoạt từ file
    activated_keys = read_activated_keys()
    
    if activation_code in activated_keys:
        return jsonify({"status": "success", "message": "Phần mềm đã được kích hoạt!"}), 200
    else:
        return jsonify({"status": "failed", "message": "Phần mềm chưa được kích hoạt!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
