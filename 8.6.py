count = 0
letters = 'ЕГЭИНФ'

for p2 in letters:
    for p3 in letters:
        for p4 in letters:
            for p5 in letters:
                for p6 in ['Э', 'И']:
                    word = 'Е' + p2 + p3 + p4 + p5 + p6
                    
                    # Проверка на запрет ЕГЭ
                    if 'ЕГЭ' in word:
                        continue
                    
                    # Подсчёт сочетаний ФИ
                    fi_count = 0
                    for i in range(len(word) - 1):
                        if word[i] == 'Ф' and word[i+1] == 'И':
                            fi_count += 1
                    
                    if fi_count >= 2:
                        count += 1

print(count)