# Profile artwork

Run `python3 scripts/render_profile_assets.py` to regenerate the local SVGs using only the Python standard library.

The visual layout is inspired by [DenverCoder1](https://github.com/DenverCoder1): compact project grids and a typing intro. This profile uses its own cyan and midnight-blue palette, bordered repository cards and icon links. The artwork and animation are generated for this profile; there are no remote fonts, stats services, tracking pixels, or external image endpoints.

`intro-dark.svg` and `intro-light.svg` cycle through three lines with stepped type-and-delete animation. Reduced-motion mode selects the static intro through the README's picture sources and displays the first line without animation. A CSS fallback is also included inside the animated SVGs. The README selects the intro and link-icon colors using the visitor's preferred color scheme.

Cards use fixed internal colors and wrap naturally on narrow screens. Their status labels describe the linked work, not project ownership or star counts. Check the linked upstream PR before changing a merge label. All images have descriptive alt text in the README.
