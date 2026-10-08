#!/usr/bin/env python3
"""
Hook de MkDocs para el Glosario de Ciberseguridad.
Sincroniza automáticamente los archivos de terminos/ y plantilla.md de la raíz,
genera el índice alfabético interactivo en index.md y la lista dinámica de colaboradores en colaboradores.md.
"""

import os
import re
import html
import shutil
import unicodedata
import yaml
from pathlib import Path

def get_repo_root(config):
    """Obtiene la ruta raíz del repositorio a partir de la ruta del archivo mkdocs.yml."""
    config_file = Path(config["config_file_path"]).resolve()
    return config_file.parent.parent

def normalize_letter(char):
    """Normaliza un caracter para agrupación alfabética eliminando tildes."""
    if not char:
        return "#"
    char = char.strip()[0].upper()
    nfkd = unicodedata.normalize('NFKD', char)
    base_char = "".join([c for c in nfkd if not unicodedata.combining(c)])
    if base_char.isalpha():
        return base_char
    return "#"

def clean_summary_text(text):
    """Elimina etiquetas HTML y sintaxis markdown residual para evitar roturas del DOM."""
    if not text:
        return ""
    cleaned = re.sub(r"<[^>]+>", "", text)
    cleaned = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", cleaned)
    cleaned = re.sub(r"[*_`#~]", "", cleaned)
    cleaned = " ".join(cleaned.split()).strip()
    return cleaned

def parse_term_file(filepath):
    """Extrae el frontmatter YAML y el resumen de un archivo de término markdown de forma segura."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter = {}
    body = content

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if match:
        raw_yaml = match.group(1).expandtabs(2)
        try:
            frontmatter = yaml.safe_load(raw_yaml) or {}
        except Exception as e:
            print(f"[Hook Glosario] Error al parsear YAML en {filepath}: {e}")
        body = match.group(2)

    filename = os.path.basename(filepath)
    slug = filename[:-3] if filename.endswith(".md") else filename

    title = frontmatter.get("title")
    if not title:
        h1_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        if h1_match:
            title = clean_summary_text(h1_match.group(1).strip())
        else:
            title = slug.replace("-", " ").title()

    summary = frontmatter.get("summary")
    if summary:
        summary = clean_summary_text(str(summary))
    else:
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        valid_paragraphs = [
            clean_summary_text(p) for p in paragraphs
            if not p.strip().startswith(("#", "<div", "!!!", "===", ">", "```", "---"))
            and clean_summary_text(p)
        ]
        summary = valid_paragraphs[0] if valid_paragraphs else "Sin descripción disponible."

    if len(summary) > 200:
        summary = summary[:197] + "..."

    return {
        "slug": slug,
        "title": title,
        "category": frontmatter.get("category", "General"),
        "tags": frontmatter.get("tags", []),
        "author": frontmatter.get("author", "Comunidad"),
        "author_url": frontmatter.get("author_url", ""),
        "summary": summary,
        "rel_path": f"terms/{slug}/",
    }

def on_config(config):
    """Evento que se ejecuta antes de compilar: copia terminos/ y plantilla.md al docs_dir de MkDocs."""
    repo_root = get_repo_root(config)
    docs_dir = Path(config["docs_dir"])

    # 1. Sincronizar terminos/ -> .mkdocs/docs/terms/
    source_terms = repo_root / "terminos"
    dest_terms = docs_dir / "terms"
    dest_terms.mkdir(parents=True, exist_ok=True)

    if source_terms.exists():
        for f in source_terms.glob("*.md"):
            shutil.copy2(f, dest_terms / f.name)

    # 2. Sincronizar plantilla.md -> .mkdocs/docs/plantillas/plantilla-termino.md
    source_template = repo_root / "plantilla.md"
    dest_template_dir = docs_dir / "plantillas"
    dest_template_dir.mkdir(parents=True, exist_ok=True)
    if source_template.exists():
        shutil.copy2(source_template, dest_template_dir / "plantilla-termino.md")

    return config

def get_all_terms(docs_dir):
    """Obtiene y parsea todos los términos del glosario."""
    terms_dir = Path(docs_dir) / "terms"
    if not terms_dir.exists():
        repo_terms = Path(docs_dir).resolve().parent.parent / "terminos"
        if repo_terms.exists():
            terms_dir = repo_terms
        else:
            return []

    term_files = [
        terms_dir / f for f in os.listdir(terms_dir)
        if f.endswith(".md") and not f.startswith(("_", ".")) and f != "index.md"
    ]

    terms = []
    for tf in term_files:
        terms.append(parse_term_file(tf))
    return terms

def generate_index_markdown(docs_dir):
    """Genera el bloque Markdown del índice a partir de los archivos en terms/."""
    terms = get_all_terms(docs_dir)
    if not terms:
        return "\n*No se encontraron términos en el glosario.*\n"

    authors = set()
    categories = set()

    for term_data in terms:
        if term_data["author"]:
            authors.add(term_data["author"])
        if term_data["category"]:
            categories.add(term_data["category"])

    terms.sort(key=lambda t: unicodedata.normalize('NFKD', t["title"].lower()))

    grouped = {}
    for term in terms:
        letter = normalize_letter(term["title"])
        grouped.setdefault(letter, []).append(term)

    sorted_letters = sorted([k for k in grouped.keys() if k != "#"])
    if "#" in grouped:
        sorted_letters.append("#")

    lines = []

    # 1. Tarjetas de Estadísticas
    lines.append('<div class="glossary-stats-grid">')
    lines.append(f'  <div class="stat-card"><span class="stat-number">{len(terms)}</span><span class="stat-label">Términos definidos</span></div>')
    lines.append(f'  <div class="stat-card"><span class="stat-number">{len(categories)}</span><span class="stat-label">Categorías</span></div>')
    lines.append(f'  <div class="stat-card"><span class="stat-number">{len(authors)}</span><span class="stat-label">Colaboradores</span></div>')
    lines.append('</div>\n')

    # 2. Barra de Navegación Alfabética Rápida
    lines.append('<div class="alphabet-nav-wrapper">')
    lines.append('  <nav class="alphabet-nav" aria-label="Navegación alfabética">')
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter in grouped:
            lines.append(f'    <a href="#{letter.lower()}" class="alpha-link active" title="Ir a términos con {letter}">{letter}</a>')
        else:
            lines.append(f'    <span class="alpha-link disabled">{letter}</span>')
    if "#" in grouped:
        lines.append('    <a href="#otros" class="alpha-link active" title="Otros símbolos">#</a>')
    lines.append('  </nav>')
    lines.append('</div>\n')

    # 3. Secciones por letra con tarjetas
    for letter in sorted_letters:
        anchor_id = "otros" if letter == "#" else letter.lower()
        display_letter = letter if letter != "#" else "# (Símbolos / Números)"
        count = len(grouped[letter])
        count_str = f"{count} término" if count == 1 else f"{count} términos"

        lines.append(f'<div class="letter-group-header" id="{anchor_id}">')
        lines.append('  <div class="letter-title-wrap">')
        lines.append(f'    <h2 class="letter-title">{display_letter}</h2>')
        lines.append(f'    <span class="letter-count">({count_str})</span>')
        lines.append('  </div>')
        lines.append('  <a href="#top" class="back-to-top" title="Volver arriba">↑ Arriba</a>')
        lines.append('</div>\n')

        lines.append('<div class="terms-card-grid">')
        for term in grouped[letter]:
            cat_safe = html.escape(str(term["category"]))
            title_safe = html.escape(str(term["title"]))
            summary_safe = html.escape(str(term["summary"]))
            
            cat_badge = f'<span class="term-badge badge-category">{cat_safe}</span>' if term["category"] else ''
            
            author_html = ""
            if term["author"]:
                author_val = str(term["author"]).strip()
                if author_val.startswith("@"):
                    gh_user = author_val.lstrip("@")
                    author_html = f'<a href="https://github.com/{html.escape(gh_user)}" target="_blank" class="author-tag">👤 {html.escape(author_val)}</a>'
                else:
                    author_html = f'<span class="author-tag">👤 {html.escape(author_val)}</span>'

            tag_html = ""
            if term["tags"]:
                tags_formatted = [f'<span class="tag-pill">#{html.escape(str(t).strip())}</span>' for t in term["tags"]]
                tag_html = f'<div class="term-tags">{" ".join(tags_formatted)}</div>'

            lines.append('  <div class="term-card">')
            lines.append('    <div class="term-card-header">')
            lines.append(f'      <h3 class="term-card-title"><a href="{term["rel_path"]}">{title_safe}</a></h3>')
            if cat_badge:
                lines.append(f'      <div class="term-badges">{cat_badge}</div>')
            lines.append('    </div>')
            lines.append(f'    <p class="term-card-summary">{summary_safe}</p>')
            lines.append('    <div class="term-card-footer">')
            lines.append(f'      {author_html}')
            lines.append(f'      {tag_html}')
            lines.append('    </div>')
            lines.append('  </div>')

        lines.append('</div>\n')

    return "\n".join(lines)

def generate_contributors_markdown(docs_dir):
    """Genera la vista de colaboradores con sus avatares de GitHub y términos aportados."""
    terms = get_all_terms(docs_dir)
    if not terms:
        return "\n*No se encontraron colaboradores registrados.*\n"

    contributors_map = {}

    for term in terms:
        raw_author = str(term["author"]).strip() if term["author"] else "Comunidad"
        # Separar múltiples autores si vienen separados por comas, 'y', '&' o 'and' como palabras independientes
        author_tokens = re.split(r"\s*,\s*|\s+(?:y|and|&)\s+", raw_author)
        for auth in author_tokens:
            auth = auth.strip()
            if not auth:
                continue
            username = auth.lstrip("@") if auth.startswith("@") else auth
            handle = f"@{username}" if auth.startswith("@") else auth
            is_github = auth.startswith("@")

            if handle not in contributors_map:
                contributors_map[handle] = {
                    "handle": handle,
                    "username": username,
                    "is_github": is_github,
                    "terms": []
                }
            contributors_map[handle]["terms"].append(term)

    # Ordenar por cantidad de aportaciones (descendente) y luego alfabéticamente
    sorted_contributors = sorted(
        contributors_map.values(),
        key=lambda c: (-len(c["terms"]), c["handle"].lower())
    )

    lines = []

    # Estadísticas de colaboradores
    lines.append('<div class="glossary-stats-grid">')
    lines.append(f'  <div class="stat-card"><span class="stat-number">{len(sorted_contributors)}</span><span class="stat-label">Colaboradores activos</span></div>')
    lines.append(f'  <div class="stat-card"><span class="stat-number">{len(terms)}</span><span class="stat-label">Términos publicados</span></div>')
    lines.append('</div>\n')

    # Cuadrícula de tarjetas de colaboradores
    lines.append('<div class="contributors-grid">')
    for c in sorted_contributors:
        num_terms = len(c["terms"])
        terms_count_str = f"{num_terms} término" if num_terms == 1 else f"{num_terms} términos"
        
        avatar_html = ""
        profile_link_html = ""
        
        if c["is_github"]:
            avatar_url = f"https://github.com/{html.escape(c['username'])}.png?size=140"
            avatar_html = f'<img class="contributor-avatar-img" src="{avatar_url}" alt="{html.escape(c["handle"])}" loading="lazy" onerror="this.onerror=null; this.parentElement.innerHTML=\'<div class=&quot;contributor-avatar-fallback&quot;>👤</div>\';" />'
            profile_link_html = f'<a href="https://github.com/{html.escape(c["username"])}" target="_blank" class="contributor-name-link">👤 {html.escape(c["handle"])}</a>'
        else:
            avatar_html = '<div class="contributor-avatar-fallback">👤</div>'
            profile_link_html = f'<span class="contributor-name-link">{html.escape(c["handle"])}</span>'

        terms_pills = []
        for t in c["terms"]:
            term_title = html.escape(str(t["title"]))
            # En la página de colaboradores, el link relativo a los términos es ../terms/{slug}/
            term_link = f"../terms/{t['slug']}/"
            terms_pills.append(f'<a href="{term_link}" class="contributor-term-pill">{term_title}</a>')

        lines.append('  <div class="contributor-card">')
        lines.append('    <div class="contributor-header">')
        lines.append(f'      <div class="contributor-avatar-wrap">{avatar_html}</div>')
        lines.append('      <div class="contributor-info">')
        lines.append(f'        <h3 class="contributor-name">{profile_link_html}</h3>')
        lines.append(f'        <span class="contributor-badge-count">{terms_count_str}</span>')
        lines.append('      </div>')
        lines.append('    </div>')
        lines.append('    <div class="contributor-terms-section">')
        lines.append('      <span class="contributor-terms-label">Términos aportados:</span>')
        lines.append(f'      <div class="contributor-terms-list">{" ".join(terms_pills)}</div>')
        lines.append('    </div>')
        lines.append('  </div>')

    lines.append('</div>\n')

    return "\n".join(lines)

def on_page_markdown(markdown, page, config, files):
    """Hook que intercepta el contenido markdown antes de renderizar la página."""
    docs_dir = config["docs_dir"]
    if page.file.src_path == "index.md":
        index_html = generate_index_markdown(docs_dir)
        if "<!-- GLOSSARY_INDEX -->" in markdown:
            return markdown.replace("<!-- GLOSSARY_INDEX -->", index_html)
        else:
            return markdown + "\n\n## 📚 Explorador de términos\n\n" + index_html
    elif page.file.src_path == "colaboradores.md":
        contributors_html = generate_contributors_markdown(docs_dir)
        if "<!-- CONTRIBUTORS_LIST -->" in markdown:
            return markdown.replace("<!-- CONTRIBUTORS_LIST -->", contributors_html)
        else:
            return markdown + "\n\n" + contributors_html
    return markdown

if __name__ == "__main__":
    import sys
    base_dir = Path(__file__).resolve().parent.parent
    docs_path = base_dir / "docs"
    print("--- Test de Generación de Índice ---")
    print(generate_index_markdown(docs_path)[:300])
    print("\n--- Test de Generación de Colaboradores ---")
    print(generate_contributors_markdown(docs_path)[:500])
