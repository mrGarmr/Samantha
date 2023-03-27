![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Samantha+Neural+Network)

## Samantha - це веб-сервіс, що класифікує зображення з використанням згорткових нейронних мереж. 

У цьому проекті демонструється використання Нейронної мережі для класифікації зображень із набору даних CIFAR-10 за допомогою transfer learning.

Моделі, які використовуються для класифікації наших зображень, створено з попередньо підготовлених класифікаторів зображень VGG16.

Ця мережа спочатку були навчена класифікувати зображення з набору даних Imagenet. Цей набір даних складається з тисяч зображень, розділених на тисячі різних категорій. Набір даних CIFAR-10 має лише 10 класів, тому ми беремо лише 10 вихідних класів.

Ми використовували DATA AUGMENTATION для збільшення реєстрації даних. Ця стратегія дозволяє значно збільшити різноманітність даних, доступних для навчальних моделей, без збору нових даних.

Ми використали пакетну нормалізацію(Batch normalization), додану до кожного прихованого рівня. Це метод підвищення швидкості, продуктивності та стабільності штучних нейронних мереж. Він нормалізує вхідний шар шляхом повторного центрування та масштабування зображення.

Ми досягли 91% точності прогнозувань нашої мережі.

![image](https://user-images.githubusercontent.com/77249874/228022389-7fbac672-a66e-4967-a283-db49f284526f.png)


### Samantha була реалізованна в двох версіях: 
1. [Samantha Telegram Bot](https://t.me/Samantha_aibot) - що вміє приймати у користувача зображення, обробляти за допомогою нейроної мережі та повертати відповідь з інформацією що саме зображенно на картинці.

- Інструкція запуску telegram інтерфейсу:
- Натисніть на [посилання](https://t.me/Samantha_aibot)
- Перейшовши в Телеграм, натисніть **Start**
- Після цього натисніть **Почати роботу**
- Оберіть картинку та натисніть **Відправити**


2. WEB інтерфейс - за допомогою фреймворку **Pynecone**

- Інструкція запуску веб інтерфейсу:
- Клонуйте репозиторій `https://github.com/mrGarmr/Samantha.git`
- Перейдіть в директорію `cd Samantha/web_service`
- Ініціюйте проект `pc init`
- Запустіть проект `pc run --port 8090 --loglevel info`
- Перейдіть в браузер та наберіть в адресній строці `http://localhost:8090/`
- Натисніть кнопку **Завантажити**
- Натисніть кнопку **Generate answer**

---

[![Language](https://img.shields.io/badge/language-python-blue?&style=plastic)](https://www.python.org)
[![Language version](https://img.shields.io/badge/version-3.10-red?&style=plastic)](https://www.python.org/downloads/)
![GitHub repo size](https://img.shields.io/badge/repo%20size-239%20kB-pink?&style=plastic)

---

### Technology which used:
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

**We used the following technologies and packages**

- Python
- Pynecone
- Aiogram
- Keras
- NumPy
- TensorFlow
- Telegram
- Git
- Docker




---

### Author
[![GitHub Contributors Image](https://contrib.rocks/image?repo=mrGarmr/Samantha)](https://github.com/mrGarmr)
[![GitHub Contributors Image](https://contrib.rocks/image?repo=vlad-bb/Python-Data-Science)](https://github.com/vlad-bb)
[![GitHub Contributors Image](https://contrib.rocks/image?repo=5u8aru/5u8aru.github.io)](https://github.com/5u8aru)
