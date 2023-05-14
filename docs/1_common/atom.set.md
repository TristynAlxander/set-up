# Atom Text Editor Settings

Atom has been abandoned, but can still be downloaded. Instructions may need to be modified.
If atom is no longer working, try pulsar or community atom.

atom-amd64.tar.gz from the Atom releases page: https://github.com/atom/atom/releases/latest
Download the deb file.
Note: the Deb file adds the start up script, which is why it's preferred.

atom $(which atom)
Comment-Out nemo_action Block

  - Install Packages (Atom: apm or Pulsar: ppm)
    - `apm install duplicate-line-or-selection`
    - `apm install highlight-selected`
    - `apm install language-latex`
    - Check if `markdown-preview` is already installed. if not `apm install markdown-preview`
  - disable `whitespace` package
  - Disable `autocomplete-snippets` package
  - Disable snippets in `language-python` package
  - set default tab size in `language-python` (and global)
  - Preferences > Editor > Automatic Soft Tabs > Uncheck
  - Disable Line Wrapping
    - Preferences > Editor >  Max Screen Line Length > Add a zero or more if needed
    - Preferences > Editor > Soft Wrap > Unclick
    - Preferences > Packages > language-gfm > Soft Wrap > Unclick
    - Preferences > Packages > language-latex > latex Grammar > Soft Wrap > Unclick
  - `line-ending-selector` > Default Line Ending > LF
  - `bracket-matcher` > uncheck Autocomplete Brackets
  - `bracket-matcher` > uncheck Wrap Selections In Brackets
  
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
  Fix Opening Projects:
    File > Reopen Project > Clear Project History
    Restart Computer
    I think atom cannot open multiple ./ even if opened in different locations.
