def extract_content(block):
    cnt_start = block.find('<div class="details_content">')
    # Count opening and closing <div> tags from cnt_start to properly balance
    idx = cnt_start
    depth = 0
    while idx < len(block):
        if block[idx:idx+4] == '<div':
            depth += 1
            idx += 4
        elif block[idx:idx+6] == '</div>':
            depth -= 1
            idx += 6
            if depth == 0:
                return block[cnt_start:idx]
        else:
            idx += 1
    return None

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

sec_start = c.find('<section class="detail section-tag" id="detail">')
sec_end = c.find('</section>', sec_start)
sec = c[sec_start:sec_end]

pos_dl_1 = sec.find('<!-- Details Right -->')
pos_dl_2 = sec.find('<!-- Details Left -->', pos_dl_1 + 1)
pos_dl_3 = sec.find('<!-- Details Right -->', pos_dl_2 + 1)
pos_sp = sec.find('<!-- Special -->', pos_dl_3 + 1)

block_baoloc = sec[pos_dl_1:pos_dl_2].strip()
block_binhchau = sec[pos_dl_2:pos_dl_3].strip()
block_seasand = sec[pos_dl_3:pos_sp].strip()

cnt_bl = extract_content(block_baoloc)
cnt_bc = extract_content(block_binhchau)
cnt_ss = extract_content(block_seasand)

print("BL content start:", cnt_bl[:100], "... end:", cnt_bl[-50:])
print("BC content start:", cnt_bc[:100], "... end:", cnt_bc[-50:])
print("SS content start:", cnt_ss[:100], "... end:", cnt_ss[-50:])
