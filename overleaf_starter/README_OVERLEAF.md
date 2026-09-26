# Overleaf Starter

This is intentionally a **compile-oriented skeleton**, not the final manuscript.

Before drafting, read the root source-pack authority files.

Recommended workflow:
1. Copy `overleaf_starter/` into a Git repository or Overleaf project.
2. Let Codex expand the `sections/*.tex` files from `manuscript_blueprint/`.
3. Keep `references.bib` synchronized with the citation audit.
4. Keep the root source pack outside the generated manuscript tree as provenance.

The starter skeleton keeps `references.bib` in place but does not invoke BibTeX until real citations are inserted; this lets the skeleton compile even in minimal local TeX environments.
