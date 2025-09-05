def read_metrics_from_file():
    """Читает метрики из файла metrics.txt"""
    metrics = {}
    try:
        with open('metrics.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    key, value = line.split(':', 1)
                    metrics[key.strip()] = value.strip()
    except FileNotFoundError:
        metrics = {
            'Имя': 'Максим',
            'Опыт': 'Начинающий',
            'Язык': 'Русский', 
            'ID': '12345',
            'Курс': '21IS'
        }
    return metrics

def main():
    user_metrics = read_metrics_from_file()
    
    for i in range(1, 6):
        print("=" * 60)
        print(f"🌟 ПЕРСОНАЛИЗИРОВАННОЕ ПРИВЕТСТВИЕ #{i}")
        print("=" * 60)
        
        print(f"👤 Имя: {user_metrics.get('Имя', 'Не указано')}")
        print(f"📈 Опыт: {user_metrics.get('Опыт', 'Не указан')}")
        print(f"🌐 Язык: {user_metrics.get('Язык', 'Не указан')}")
        print(f"🔢 ID: {user_metrics.get('ID', 'Не указан')}")
        print(f"🎓 Курс: {user_metrics.get('Курс', 'Не указан')}")
        
        print("=" * 60)
        
        if user_metrics.get('Курс') == '21IS':
            print("🎯 Добро пожаловать, студент курса 21IS!")
            print("💡 Информационные системы - это перспективно!")
            print("🚀 Успехов в освоении программирования!")
        else:
            print("💻 Добро пожаловать в проект TIK-TAK!")
        
        print("=" * 60)
        print()

if __name__ == "__main__":
    main()