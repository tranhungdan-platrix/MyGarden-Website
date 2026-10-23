import re

def extract_inners(block):
    # Find details_image
    img_match = re.search(r'(<div class="details_image">[\s\S]*?</div>\s*</div>)', block)
    # Actually let's locate <div class="details_image"> and find its matching closing div
    # Or locate between <div class="details_image"> and the corresponding </div>
    # Even simpler:
    img_start = block.find('<div class="details_image">')
    # It has <div class="background_image"...></div></div>
    img_end = block.find('</div>', block.find('</div>', img_start) + 1) + 6
    img_inner = block[img_start:img_end]
    
    cnt_start = block.find('<div class="details_content">')
    # details_content ends right before the closing of its column div
    # Let's find </div\s*>\s*</div\s*>\s*</div\s*>\s*</div\s*>$ or before the next column
    # Let's verify by checking where btn-group ends
    btn_grp_end = block.find('</div>', block.find('<div class="btn-group">') + 1)
    # The inner details_content ends after the next </div> (closing btn-group and closing details_content)
    # Let's find the closing tag for details_content
    # Let's test this in test script!
    return img_inner

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
block_phanthiet = sec[pos_sp:].strip()

print("Bao Loc img:\n", extract_inners(block_baoloc))
print("Binh Chau img:\n", extract_inners(block_binhchau))
print("Sea Sand img:\n", extract_inners(block_seasand))
