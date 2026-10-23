import re
import sys

def extract_content(block):
    cnt_start = block.find('<div class="details_content">')
    if cnt_start == -1:
        return None
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

def extract_image(block):
    img_start = block.find('<div class="details_image">')
    if img_start == -1:
        return None
    # Find closing </div>
    idx = img_start
    depth = 0
    while idx < len(block):
        if block[idx:idx+4] == '<div':
            depth += 1
            idx += 4
        elif block[idx:idx+6] == '</div>':
            depth -= 1
            idx += 6
            if depth == 0:
                return block[img_start:idx]
        else:
            idx += 1
    return None

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    sec_start = content.find('<section class="detail section-tag" id="detail">')
    sec_end = content.find('</section>', sec_start)
    sec = content[sec_start:sec_end]

    # Split sec into individual blocks
    # In index.html and en/index.html:
    # 3 <div class="details"> blocks and 1 <div class="special"> block
    # Let's find each block
    divs = []
    # Find occurrences of '<div class="details">' or '<div class="special">'
    pos = 0
    while True:
        m = re.search(r'<div class="(details|special)">', sec[pos:])
        if not m:
            break
        start_idx = pos + m.start()
        # Find closing </div> for this block
        idx = start_idx
        depth = 0
        while idx < len(sec):
            if sec[idx:idx+4] == '<div':
                depth += 1
                idx += 4
            elif sec[idx:idx+6] == '</div>':
                depth -= 1
                idx += 6
                if depth == 0:
                    divs.append(sec[start_idx:idx])
                    pos = idx
                    break
            else:
                idx += 1

    print(f"{filepath}: Found {len(divs)} blocks")
    baoloc_block = None
    binhchau_block = None
    seasand_block = None
    phanthiet_block = None

    for d in divs:
        if 'baoloc' in d.lower():
            baoloc_block = d
        elif 'binhchau' in d.lower():
            binhchau_block = d
        elif 'seasand' in d.lower():
            seasand_block = d
        elif 'phanthiet' in d.lower():
            phanthiet_block = d

    assert baoloc_block and binhchau_block and seasand_block and phanthiet_block, "All 4 blocks must be identified"

    bl_img = extract_image(baoloc_block)
    bl_cnt = extract_content(baoloc_block)
    bc_img = extract_image(binhchau_block)
    bc_cnt = extract_content(binhchau_block)
    ss_img = extract_image(seasand_block)
    ss_cnt = extract_content(seasand_block)

    # 1. Binh Chau (Details Right)
    new_bc = f'''		<!-- Details Right -->

		<div class="details">
			<div class="container">
				<div class="row">
					
					<!-- Details Image -->
					<div class="col-xl-7 col-lg-6">
						{bc_img}
					</div>

					<!-- Details Content -->
					<div class="col-xl-5 col-lg-6">
						{bc_cnt}
					</div>

				</div>
			</div>
		</div>'''

    # 2. Bao Loc (Details Left)
    new_bl = f'''		<!-- Details Left -->

		<div class="details">
			<div class="container">
				<div class="row">

					<!-- Details Content -->
					<div class="col-xl-5 col-lg-6 order-lg-1 order-2">
						{bl_cnt}
					</div>

					<!-- Details Image -->
					<div class="col-xl-7 col-lg-6 order-lg-2 order-1">
						{bl_img}
					</div>

				</div>
			</div>
		</div>'''

    # 3. Phan Thiet (Special)
    new_pt = f'''		<!-- Special -->

		{phanthiet_block}'''

    # 4. Sea Sand (Details Right)
    new_ss = f'''		<!-- Details Right -->

		<div class="details">
			<div class="container">
				<div class="row">
					
					<!-- Details Image -->
					<div class="col-xl-7 col-lg-6">
						{ss_img}
					</div>

					<!-- Details Content -->
					<div class="col-xl-5 col-lg-6">
						{ss_cnt}
					</div>

				</div>
			</div>
		</div>'''

    new_sec_body = f'''<section class="detail section-tag" id="detail">

{new_bc}

{new_bl}

{new_pt}

{new_ss}

	'''
    
    content_new = content[:sec_start] + new_sec_body + content[sec_end:]

    # Now reorder footer-location
    # Locate <div class="footer-location"> ... </div>
    fl_start = content_new.find('<div class="footer-location">')
    fl_end = content_new.find('</div>', fl_start) + 6
    fl_text = content_new[fl_start:fl_end]

    # Find <a> tags inside footer-location
    a_tags = re.findall(r'(<a\s+target="_blank"[\s\S]*?</a>)', fl_text)
    if len(a_tags) == 4:
        bl_a = None
        bc_a = None
        pt_a = None
        ss_a = None
        for a in a_tags:
            if 'Bao+Loc' in a or 'Bảo Lộc' in a or 'Bao Loc' in a:
                bl_a = a
            elif 'B%C3%ACnh+Ch%C3%A2u' in a or 'Bình Châu' in a or 'Binh Chau' in a:
                bc_a = a
            elif 'Phan+Thiet' in a or 'Phan Thiết' in a or 'Phan Thiet' in a:
                pt_a = a
            elif 'Sea+Sand' in a or 'Sea Sand' in a:
                ss_a = a
        if bl_a and bc_a and pt_a and ss_a:
            heading = re.search(r'(<h5[^>]*>.*?</h5>)', fl_text).group(1)
            new_fl = f'''<div class="footer-location">
			{heading}
			{bc_a}
			{bl_a}
			{pt_a}
			{ss_a}
		</div>'''
            content_new = content_new[:fl_start] + new_fl + content_new[fl_end:]
            print(f"{filepath}: Footer locations reordered successfully.")
        else:
            print(f"{filepath}: Warning: could not map all 4 <a> tags in footer-location")
    else:
        print(f"{filepath}: Warning: found {len(a_tags)} <a> tags in footer-location, expected 4")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content_new)
    print(f"{filepath}: Updated successfully.")

process_file('index.html')
process_file('en/index.html')
