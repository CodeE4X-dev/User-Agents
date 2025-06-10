def split_proxy_file(input_file, parts=7):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // parts
    remainder = total_lines % parts

    start = 0
    for i in range(parts):
        end = start + chunk_size + (1 if i < remainder else 0)
        with open(f'proxy_part_{i+1}.txt', 'w', encoding='utf-8') as out_file:
            out_file.writelines(lines[start:end])
        print(f"Created proxy_part_{i+1}.txt with {end - start} lines.")
        start = end

# Ganti 'your_proxy_file.txt' dengan nama file proxy kamu
split_proxy_file('proxies.txt')
