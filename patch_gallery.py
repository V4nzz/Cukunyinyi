import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start and end markers
start_marker = '  <!-- ============================\n       STICKY GALLERY SECTION'
end_marker   = '\n  <!-- ============================\n       INFORMATION SECTION'

start_idx = content.index(start_marker)
end_idx   = content.index(end_marker)

new_section = '''  <!-- ============================
       STICKY GALLERY SECTION
  ============================= -->
  <section class="gallery-section" id="gallery" aria-labelledby="gallery-heading">

    <div class="gallery-intro reveal">
      <span class="section-label">Galeri Kawasan</span>
      <h2 class="section-title gallery-title" id="gallery-heading">Flora, Fauna &amp;<br/>Pemandangan</h2>
    </div>

    <!-- Sticky Scroll Grid: kiri & kanan scroll, tengah sticky 3-baris -->
    <div class="sgal-grid">

      <!-- LEFT: 5 scrolling images -->
      <div class="sgal-col sgal-scroll">
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1448375240586-882707db888b?w=600&q=80&auto=format&fit=crop" alt="Mangrove Trekking" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Aktivitas</span><p>Mangrove Trekking</p><small>Menyusuri Jalur Kayu</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=600&q=80&auto=format&fit=crop" alt="Boat Tours" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Eksplorasi</span><p>Boat Tours</p><small>Menjelajah Fauna Pesisir</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600&q=80&auto=format&fit=crop" alt="Pantai Pesisir" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Santai</span><p>Fishing &amp; Swimming</p><small>Kenikmatan Air Pesisir</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1501854140801-50d01698950b?w=600&q=80&auto=format&fit=crop" alt="Aerial Hutan" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Konservasi</span><p>Aerial View Mangrove</p><small>12 Ha Kawasan Hijau</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=600&q=80&auto=format&fit=crop" alt="Program Konservasi" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Edukasi</span><p>Program Konservasi</p><small>Nursery &amp; Aksi Tanam</small></figcaption>
        </figure>
      </div>

      <!-- CENTER: sticky 3-row (stays pinned while sides scroll) -->
      <div class="sgal-col sgal-sticky">
        <figure class="sgal-fig sgal-fig--stretch">
          <img src="https://images.unsplash.com/photo-1518173946687-a4c8892bbd9f?w=700&q=85&auto=format&fit=crop" alt="Daun Mangrove Bokeh" class="sgal-img" loading="lazy"/>
        </figure>
        <figure class="sgal-fig sgal-fig--stretch">
          <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=700&q=85&auto=format&fit=crop" alt="Cahaya Hutan Bakau" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption">
            <span class="sgal-tag">Landmark Lokal</span>
            <p>Replika Menara Eiffel</p>
            <small>Bambu 12 meter - Ikon Sidodadi</small>
            <a href="#info" class="btn btn-primary btn-sm" style="align-self:flex-start;margin-top:0.5rem;">Rencanakan Kunjungan</a>
          </figcaption>
        </figure>
        <figure class="sgal-fig sgal-fig--stretch">
          <img src="https://images.unsplash.com/photo-1505118380757-91f5f5632de0?w=700&q=85&auto=format&fit=crop" alt="Panorama Alam Tropis" class="sgal-img" loading="lazy"/>
        </figure>
      </div>

      <!-- RIGHT: 5 scrolling images -->
      <div class="sgal-col sgal-scroll">
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=600&q=80&auto=format&fit=crop" alt="Pantai Sidodadi" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Seni Budaya</span><p>Kuda Kepang</p><small>Atraksi Tradisional</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=600&q=80&auto=format&fit=crop" alt="Pemandangan Alam" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Kearifan Lokal</span><p>Ragi Tapai</p><small>Produksi Tradisional Sidodadi</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=600&q=80&auto=format&fit=crop" alt="Pesisir Alam" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Seni</span><p>Tari Lampung &amp; Silat</p><small>Harmoni Gerak Warga</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=80&auto=format&fit=crop" alt="Danau Alam" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Alam</span><p>Ekowisata Pesisir</p><small>Teluk Pandan, Pesawaran</small></figcaption>
        </figure>
        <figure class="sgal-fig">
          <img src="https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=600&q=80&auto=format&fit=crop" alt="Hutan Tropis" class="sgal-img" loading="lazy"/>
          <figcaption class="sgal-caption"><span class="sgal-tag">Flora</span><p>Hutan Tropis Mangrove</p><small>Biodiversitas Pesisir</small></figcaption>
        </figure>
      </div>

    </div>
  </section>
'''

result = content[:start_idx] + new_section + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Done. New length: {len(result)} chars')
