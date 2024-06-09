# Install Tutorial

## 1. Cài đặt thư viện cần thiết:

```bash
pip install -r requirements.txt
```

## 2. Hướng dẫn cài đặt chương trình: 

- Clone chương trình về máy: 

```bash
git clone git@github.com:hoangnhatminh0809/ml-project.git
```

- Tải và giải nén bộ tiền xử lý của BERT: https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3

- Tải và giải nén bộ mã hóa của BERT: https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-12_H-768_A-12/2

- Sửa đường dẫn trong thử mục bert.py: preprocess_url và encoder_url

## Chạy chương trình:

### Phương pháp 1: Mạng neural:

- Chạy file "train.py" để huấn luyện và lưu trữ mạng nơ-ron.
- Import chat_nn.py trong app.py và test.py.
- Chạy file "app.py" để khởi chạy giao diện đồ họa của chatbot, hoặc chạy file "test.py" để đánh giá độ chính xác của chatbot.

### Phương pháp 2: k-NN:

- Import chat_knn.py trong app.py và test.py.
- Chạy file "app.py" để khởi động giao diện đồ họa của chatbot, hoặc chạy file "test.py" để đánh giá độ chính xác của chatbot.
