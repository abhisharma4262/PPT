# Myridius deck kit

Everything Claude needs to build Myridius decks the way you like them. The rules live in the
**myridius-slide-decks** skill (saved in your Claude account; a copy is in `SKILL.md` here).
This folder holds the files the skill uses.

| Folder | What it is |
|---|---|
| `template/Myridius_Template_2026.pptx` | The 2026 template: cover, content sample, divider, end slide (keep this order) |
| `tools/mkit.py` | HTML slide kit: palette, header at template positions, icons, ring and arc helpers |
| `tools/html2pptx.py` | HTML deck to editable PPTX (shapes, text boxes, native SVG icons) |
| `tools/merge_into_template.py` | Puts the slides into the template with cover, dividers, end slide, logo and page numbers |
| `tools/lint_text.py` | Flags em dashes, emojis, hype words, long titles, and statistics on request |
| `tools/render_qa.py` | Renders every slide and a contact sheet for review |
| `examples/example_deck.py` | Three slide patterns, end to end |
| `SKILL.md` | Copy of the skill text, for versioning or packaging as a plugin later |

## How to use it
1. Start a **new Cowork task** for each new deck. A fresh task starts clean and loads the skill;
   long threads get compacted and lose detail.
2. Connect two folders: this `_Claude` folder (kit and reference decks) and the project folder that
   holds the documents for that deck. Saved output goes to the project folder.
3. Brief Claude as you normally would: deck type, audience, the decision it should drive, what to
   cover, which documents to read, and whether to research. You can say "use my Myridius deck skill"
   to be sure it is applied.
4. Claude agrees the storyline with you first, then builds, checks and saves the PPTX. Give feedback
   on the slides as usual; edit in PowerPoint whenever you like and tell Claude to work from your file.
5. When you notice a new preference or a repeated correction, say "update my deck skill with this".
   Claude proposes the updated skill for you to save and refreshes `SKILL.md` here.

## Sharing with colleagues (later)
- **Simplest:** share this folder from OneDrive and send colleagues the skill. Each of them saves the
  skill in their own Claude account and connects the shared folder. The skill's folder path points to
  your OneDrive, so they would need the same folder name or an edited path.
- **Better for a team:** package the skill and this kit as a Cowork plugin. A plugin carries its own
  files, so nobody needs to connect folders, and your Claude admin can publish it in the Myridius
  plugin catalog so colleagues install it in one click. A private GitHub repository in the Myridius
  organisation is a good home for the plugin's source and versions.
- **Avoid a public repository.** The template carries Myridius brand assets, and the reference decks
  and skill examples mention Disney. Before any wider sharing, replace client names in the skill with
  generic examples and keep client decks out of the shared package.

## Run it yourself (optional)
```
cd examples
python3 example_deck.py
python3 ../tools/html2pptx.py example.html example_raw.pptx "Example deck"
python3 ../tools/merge_into_template.py example_raw.pptx example_final.pptx --kicker "Discussion with Client" --title "Myridius|Example proposal" --date "October 2026" --divider "Appendix@3"
python3 ../tools/lint_text.py example_final.pptx
python3 ../tools/render_qa.py example_final.pptx qa
```
Needs Python 3 with python-pptx, playwright (Chromium) and Pillow; Node with pptxgenjs and sharp
(`npm install pptxgenjs sharp` inside `tools`); LibreOffice and poppler for rendering.
