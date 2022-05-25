# Atom Text Editor Settings
  - Disable snippets in `language-python`
  - set default tab size in `language-python` (and global)
  - disable `whitespace` package
  - Disable Line Wrapping
    - Preferences > Packages > Editor >  Max Screen Line Length > Add a zero or more if needed
    - Preferences > Packages > Editor > Soft Wrap > Unclick
    - Preferences > Packages > langauge-gfm > Soft Wrap > Unclick
  - `line-ending-selector` > Default Line Ending > LF
  - `bracket-matcher` > uncheck Autocomplete Brackets
  - `bracket-matcher` > uncheck Wrap Selections In Brackets 
  - `apm install duplicate-line-or-selection`
  - `apm install highlight-selected`
  - `apm install language-latex`
  - Check if `markdown-preview` is already installed. if not `apm install markdown-preview`
  - Preferences > Packages > `Spell Check` > Grammar > append `, text.tex.latex` > Restart program
  - append duplicate key to `~/.atom/keymap.cson`
  
        'atom-workspace atom-text-editor:not([mini])':
          'ctrl-d': 'duplicate-line-or-selection:duplicate'
          
  - bigger scrollbar append following to Edit > Stylesheet... > 
  
        .scrollbars-visible-always {
          ::-webkit-scrollbar {
            width: 12px;
            height: 12px;
            &-track {
                border: 0px;
                border-radius: 0px;
                background-color: #444 !important;
                }
            &-thumb {
                background-color: rgba(200,200,250,0.35) !important;
                border: 0px;
                border-radius: 9px;
                }
            }
          }
  
  
  - `spell-check` 
    - Known Words > "complexing, transmembrane, dimerization, mispairing, misfolding, histocompatibility, proteolyzed, surveilling, kinases, cytosolic, immunoreceptor, tyrosine, tyrosines, phosphorylated, phosphorylates, calcineurin, signalosome, adaptor, stimulatory, costimulatory, epitope, epitopes, linkers, phosphatase, phosphatases, actin, cytoskeleton, dimeric, dimerized, microcluster, allosteric, allostery, cooperativity, analyte, ligand, deconvoluting, sensorgram, sensorgrams, modularity, unstrained, rigidifying, conformational, directionality, disulfide, heterodimer, heterodimers, heterodimerize, heterodimerizes, homodimer, ectodomain, ectodomains, proline, prolines, microclusters, convolute, heterodimeric"
    - text.tex.latex, source.python
    - Sometimes this module breaks. Disable it, Restart, Enable it, Restart
  