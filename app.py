from flask import Flask, request, redirect
import telegram

app = Flask(__name__)

# Telegram bot token va chat_id
bot = telegram.Bot(token='7644630877:AAFgLGhLpKJEYCafvbrNtgg955W5k7D4OYo')
chat_id = '5198568117'

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <title>Buyurtma berish | Slayd_Maqola</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: #f8f9fa;
                font-family: 'Segoe UI', sans-serif;
            }
            .form-container {
                max-width: 600px;
                margin: 60px auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            }
            h2 {
                text-align: center;
                margin-bottom: 25px;
                color: #343a40;
            }
            .btn-primary {
                width: 100%;
            }
            .about-section, .services-section {
                margin-top: 40px;
            }
            .service-item {
                background: #f8f9fa;
                border: 1px solid #ddd;
                padding: 20px;
                border-radius: 10px;
                margin: 10px 0;
            }
            .service-item h5 {
                font-size: 1.2rem;
                color: #343a40;
            }
            .service-item p {
                color: #6c757d;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Sayt haqida bo'lim -->
            <section class="about-section">
                <h2>🌐 Biz haqimizda</h2>
                <p>
                    "Slayd_Maqola" — maqola, slayd, kurs ishi va mustaqil ishlar tayyorlashda sizga yordam beradigan ishonchli xizmat.
                    Biz sizning bilim va ijodingizni yaxshilash uchun samarali va sifatli xizmatlarni taqdim etamiz.
                </p>
            </section>

            <!-- Xizmatlar bo'limi -->
            <section class="services-section">
                <h2>💼 Bizning Xizmatlarimiz</h2>
                <div class="service-item">
                    <h5>📄 Maqola tayyorlash</h5>
                    <p>Har qanday mavzuda maqola yozish, ilmiy va akademik talablar asosida.</p>
                    <p><strong>Narx: 10 000 so'm</strong></p>
                </div>
                <div class="service-item">
                    <h5>📊 Slaydlar tayyorlash</h5>
                    <p>PowerPoint slaydlar yaratish, taqdimotlar uchun chiroyli dizaynlar.</p>
                    <p><strong>Narx: 3 000 so'm</strong></p>
                </div>
                <div class="service-item">
                    <h5>📚 Kurs ishi tayyorlash</h5>
                    <p>Akademik kurs ishi yozish, muammolarni tahlil qilish va yondashuvlar ishlab chiqish.</p>
                    <p><strong>Narx: 30 000, 50 000 so'm</strong></p>
                </div>
                <div class="service-item">
                    <h5>📖 Mustaqil ish tayyorlash</h5>
                    <p>Mustaqil ishlarni yozish va yozma topshiriqlarni mukammallashtirish.</p>
                    <p><strong>Narx: 5 000 so'm</strong></p>
                </div>
            </section>

            <!-- Buyurtma formasi -->
            <section class="form-container">
                <h2>📝 Buyurtma berish</h2>
                <form action="/submit_order" method="POST">
                    <div class="mb-3">
                        <label for="service" class="form-label">Xizmat turi:</label>
                        <select class="form-select" name="service" required>
                            <option value="article">📄 Maqola</option>
                            <option value="slide">📊 Slayd</option>
                            <option value="coursework">📚 Kurs ishi</option>
                            <option value="independent_work">📖 Mustaqil ish</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="name" class="form-label">Ismingiz:</label>
                        <input type="text" class="form-control" name="name" required>
                    </div>
                    <div class="mb-3">
                        <label for="contact" class="form-label">Aloqa (tel/Telegram):</label>
                        <input type="text" class="form-control" name="contact" required>
                    </div>

                    <button type="submit" class="btn btn-primary">📩 Buyurtma berish</button>
                </form>
            </section>
        </div>

        <script>
            document.querySelector('select[name="service"]').addEventListener('change', function() {
                // Yangi formalarni faollashtirish
                document.getElementById('article_section').style.display = 'none';
                document.getElementById('slide_section').style.display = 'none';
                document.getElementById('coursework_section').style.display = 'none';
                document.getElementById('independent_work_section').style.display = 'none';

                if (this.value === 'article') {
                    document.getElementById('article_section').style.display = 'block';
                } else if (this.value === 'slide') {
                    document.getElementById('slide_section').style.display = 'block';
                } else if (this.value === 'coursework') {
                    document.getElementById('coursework_section').style.display = 'block';
                } else if (this.value === 'independent_work') {
                    document.getElementById('independent_work_section').style.display = 'block';
                }
            });
        </script>
    </body>
    </html>
    '''

@app.route('/submit_order', methods=['POST'])
def submit_order():
    service = request.form['service']
    name = request.form['name']
    contact = request.form['contact']

    # Xizmat turlari uchun mavzular va qo'shimcha ma'lumotlar
    if service == 'article':
        topic = request.form['article_topic']
        details = request.form['article_details']
    elif service == 'slide':
        topic = request.form['slide_topic']
        details = request.form['slide_details']
    elif service == 'coursework':
        topic = request.form['coursework_topic']
        details = request.form['coursework_details']
    elif service == 'independent_work':
        topic = request.form['independent_work_topic']
        details = request.form['independent_work_details']
    
    # Yuboriladigan matnni yaratish
    text = f"📝 *Yangi buyurtma!* \n\n👤 Ism: {name}\n📞 Aloqa: {contact}\n📌 Xizmat turi: {service}\n📚 Mavzu: {topic}\n📄 Qo‘shimcha ma'lumot: {details}"

    # Telegramga yuborish
    bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')
    return '''
        <h3 style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            ✅ Buyurtmangiz muvaffaqiyatli qabul qilindi! <br>
            Tez orada siz bilan bog‘lanamiz.
        </h3>
    '''

if __name__ == '__main__':
    app.run(debug=True)