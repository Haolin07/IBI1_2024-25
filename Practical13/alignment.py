import blosum as bl
# 读取FASTA文件
def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    sequence = ''.join(line.strip() for line in lines[1:])  # 忽略首行描述
    return sequence



# 计算比对得分与同一性
human_seq = read_fasta("/Users/pro/Desktop/IBI1_2024-25/Practical13/P04179.fa")
mouse_seq = read_fasta("/Users/pro/Desktop/IBI1_2024-25/Practical13/P09671.fa")
random_seq = read_fasta("/Users/pro/Desktop/IBI1_2024-25/Practical13/random.fa")
blosum = bl.BLOSUM(62)

#Human vs Mouse
total_score_hm = 0
identical_hm = 0
for h_aa, m_aa in zip(human_seq, mouse_seq):
    total_score_hm += blosum[h_aa][m_aa]  
    if h_aa == m_aa:
        identical_hm += 1

percent_identity1 = (identical_hm / len(human_seq)) * 100
print("human vs mouse")
print(f"比对得分: {total_score_hm}")
print(f"百分比同一性: {percent_identity1:.2f}%")

#Human vs Random
total_score_hr = 0
identical_hr = 0
for h_aa, r_aa in zip(human_seq, random_seq):
    total_score_hr += blosum[h_aa][r_aa] 
    if h_aa == r_aa:
        identical_hr += 1

percent_identity2 = (identical_hr / len(human_seq)) * 100
print("human vs mouse")
print(f"比对得分: {total_score_hr}")
print(f"百分比同一性: {percent_identity2:.2f}%")

#MOuse vs Random
total_score_mr = 0
identical_mr = 0
for m_aa, r_aa in zip(mouse_seq, random_seq):
    total_score_mr += blosum[m_aa][r_aa] 
    if m_aa == r_aa:
        identical_mr += 1

percent_identity3 = (identical_mr / len(human_seq)) * 100
print("human vs mouse")
print(f"比对得分: {total_score_mr}")
print(f"百分比同一性: {percent_identity3:.2f}%")