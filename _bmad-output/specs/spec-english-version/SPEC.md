# Specification: English Version for MyGarden Villa Website

## 1. Why
MyGarden Villa welcomes international travelers, expatriates, and overseas Vietnamese seeking peaceful eco-luxury retreat experiences across its boutique villas (Bình Châu, Bảo Lộc, Phan Thiết, Sea Sand). An authentic, high-quality English version of the website elevates brand prestige, drives international direct inquiries, and supports international booking platforms (e.g. Airbnb).

## 2. Capabilities
- **CAP-1: Language Switcher UI**
  - Add an intuitive, elegant language selector (`[🇻🇳 VN | 🇬🇧 EN]`) in the header navbar and mobile slide-out drawer across all pages.
  - Active language state visually highlighted.
- **CAP-2: English Subdirectory Routing (`/en/`)**
  - Mirrored structure under `en/`:
    - `en/index.html` (Main Landing Page)
    - `en/baoloc.html` (Bảo Lộc Lakeview Villa)
    - `en/binhchau.html` (Bình Châu Hotspring Villa)
    - `en/phanthiet.html` (Phan Thiết Beachfront Villa)
    - `en/seasand.html` (Sea Sand Garden Villa)
    - `en/namphuong.html` (Nam Phương Lakeview Villa)
  - Relative asset links (`../images/`, `../styles/`, `../js/`, `../plugins/`) to avoid duplicating large media assets.
- **CAP-3: Luxury Hospitality Copywriting**
  - Poetic, warm, and inviting English translation capturing the "Forest - Mountain - Sea" story born out of 2021.
  - Clear translation of all villa amenities, bedroom/bathroom configurations, guest capacities, local attractions, and review testimonials.
- **CAP-4: SEO & Metadata**
  - Correct `html lang="en"` and `html lang="vi"` declarations.
  - Bi-directional `hreflang` link headers for search engines.

## 3. Constraints
- **100% Static HTML/CSS/JS**: Zero server-side runtime dependency to guarantee instant loading and flawless deployment to Mắt Bão hosting.
- **Visual Parity**: Maintain the exact typography, responsive grid, animations, and image carousels across both languages.
- **No Asset Duplication**: Reuse existing image and script assets via relative paths.

## 4. Non-Goals
- Automated external widget translation (e.g. Google Translate dropdown) which causes layout shifts, untranslated image overlays, and poor luxury branding.
- Dynamic backend database localization.

## 5. Success Signals
- Switching between VN and EN is immediate with zero broken links or missing assets on `http://localhost:8080`.
- All villa destination detail pages have complete English equivalents.
- Both desktop and mobile navigation include functioning language toggles.
