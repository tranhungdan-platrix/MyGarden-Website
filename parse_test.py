with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

sec_start = c.find('<section class="detail section-tag" id="detail">')
sec_end = c.find('</section>', sec_start)
sec = c[sec_start:sec_end]
print('sec found, length:', len(sec))

pos_dl_1 = sec.find('<!-- Details Right -->')
pos_dl_2 = sec.find('<!-- Details Left -->', pos_dl_1 + 1)
pos_dl_3 = sec.find('<!-- Details Right -->', pos_dl_2 + 1)
pos_sp = sec.find('<!-- Special -->', pos_dl_3 + 1)

print('Positions:', pos_dl_1, pos_dl_2, pos_dl_3, pos_sp)

block_baoloc = sec[pos_dl_1:pos_dl_2].strip()
block_binhchau = sec[pos_dl_2:pos_dl_3].strip()
block_seasand = sec[pos_dl_3:pos_sp].strip()
block_phanthiet = sec[pos_sp:].strip()

print('Bao Loc len:', len(block_baoloc))
print('Binh Chau len:', len(block_binhchau))
print('Sea Sand len:', len(block_seasand))
print('Phan Thiet len:', len(block_phanthiet))
