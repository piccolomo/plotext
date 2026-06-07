Future Plan
===========

Open ideas for `plotext` 6.x. Contributions welcome — open an `issue <https://github.com/piccolomo/plotext/issues/new>`_ or a `pull request <https://github.com/piccolomo/plotext/compare>`_.

Bug Fixes
---------
- Business-day datetime axis — optionally skip weekends (and holidays) so series don't show flat gaps (orig. `Issue 148 <https://github.com/piccolomo/plotext/issues/148>`_).

Ideas
-----

Looser, larger, or longer-term directions — kept here as inspiration rather than committed work.

- Network / graph primitive — nodes + edges layout (orig. `Issue 160 <https://github.com/piccolomo/plotext/issues/160>`_).
- Text tables — a formatted table primitive distinct from ``heatmap`` / ``confusion_matrix``.
- Clickable plots — mouse-event hooks for interactive selection (orig. `Issue 175 <https://github.com/piccolomo/plotext/issues/175>`_; non-trivial on raw terminals).
- Hi-res markers (``hd`` / ``fhd`` / ``braille``) on Windows and rare terminals — needs platform detection and fallback.
