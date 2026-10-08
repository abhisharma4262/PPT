---
name: myridius-slide-decks
description: Create or revise Myridius and Evoq slide decks (client proposals, offering and POV decks) in the Myridius 2026 template, story-led, research-backed and agency quality.
---

# Myridius slide decks

Use this skill whenever the user asks for slides, a deck, a proposal, a pitch, an offering or solution presentation, or changes to any of these. It encodes how this user wants decks thought through, written, designed and delivered. Read all of it before starting; most rework in past projects came from skipping one of these rules.

Myridius is an IT services company that builds and runs agentic and AI-driven software for enterprise clients. Evoq is the brand of Myridius' AI accelerators, including Evoq AEO (Agentic Engineering Orchestrator) and Code to Clarity.

The user is a Myridius leader who sells Evoq to enterprise clients. The user also works on client proposals that may not involve Evoq at all; build those decks in exactly the same way. Past examples: a client proposal (Disney DCL GRATS migration) and an offering and point-of-view deck (Agent Assurance). Both are in the reference folder (see Assets).

**Everything in this skill that comes from past decks (story arcs, diagrams, components, titles) is a reference, not a template.** The message of each slide decides its visual, and the purpose, audience and content of each deck decide its structure. Claude, as the deck builder, makes those calls and is expected to design new structures, diagrams and components whenever they serve the message better.

---

## 1. Philosophy

1. **The deck is a story.** Top to bottom it reads as one argument: context, what it takes, our point of view, the choice, how we deliver it, proof, depth in the appendix. Every slide answers the question the previous slide raised.
2. **Thought leader first, seller second.** Write as a trusted advisor to the client's leadership while wearing the Myridius hat. Consultative, not salesy: frame the client's decision, show the honest options, then show why our approach wins for this case.
3. **The diagram is the message.** Each content slide has one visual idea that carries the point on its own. Text supports the visual, never the other way round. Design the visual from the message; invent a new diagram when nothing familiar says it as well.
4. **Agency polish.** Clean grids, generous white space, consistent spacing, icons on every list item or tile, one emphasis per slide, nothing cramped or busy.
5. **Research-backed and true.** Facts come from the user's documents or from current, verified research. Never invent facts, numbers, client details, product features or quotes. When unsure, say so and ask.
6. **Realistic.** Show trade-offs, including the costs of our own recommendation (set-up time, SME time, platform to run). A deck that makes everything look good is not credible.
7. **Executive tone.** Plain, confident, specific. No arrogance, no hype, no AI-sounding phrasing.

---

## 2. Workflow

### Step 0. Understand the brief
- Identify: deck type (client proposal, offering/POV, internal), audience (CXO, IT leadership, procurement), the decision the deck must drive, length, must-have content, reference documents, whether research is wanted.
- Read every reference document fully before writing (RFPs, solution strategies, walkthrough decks, screenshots, process notes). Use the client's own words and names (for example "Disney RA stack").
- The user dictates by voice. Fix likely transcription slips from context (for example "Go to Clarity" means "Code to Clarity", "Evo AEO" means "Evoq AEO") and mention any you were unsure of.
- If something core is missing (audience, purpose, scope), ask once, in one round of questions. Otherwise make a sensible assumption, state it, and proceed.

### Step 1. Research (when asked, or when the deck makes claims about the market, competitors or technology)
- Search before stating anything about the present-day world: competitor products and their real capabilities, market shifts, adoption data, standards. Use primary sources (vendor docs, analyst and survey publishers, research labs).
- Go deep enough to be current. Do not present an approach the market has moved past (for example, hand-written "traditional rewrite" as a modernization option).
- Keep a source list. Put sources in the reply, and on the slide as a small source line only when the slide shows third-party data.
- Statistics: in client proposals, default to point-of-view statements, not percentages, unless the user specifically wants statistics on a slide. In offering or market decks, statistics are fine when sourced on the slide. Ask if unsure.
- Enrich with specifics the reader recognises: named tools and platforms, standards, the client's systems, epics and stories, real screens. Richness comes from specifics, not from more words.

### Step 2. Storyline before visuals
Write the spine first: for each slide, the eyebrow, the message title and what the visual proves. For a new deck of five or more slides, show the spine in chat and get a go-ahead before building (if the user is away, proceed and put the spine at the top of the reply). Check the threading rules in section 3 against the spine.

### Step 3. Build
Design each slide's visual from its message (section 6), then build it in HTML with the mkit kit, preview, export to editable PPTX, then merge into the Myridius template (section 8). Every shape, text box and icon must stay editable in PowerPoint with no loss of quality.

### Step 4. QA
Run the linter and render every slide. Look at every image. Fix and re-render until the checklist in section 9 passes.

### Step 5. Deliver
- Save the PPTX into the user's project folder with a version suffix (`Client_Topic_v3.pptx`). Never overwrite a file the user has edited.
- Reply in a few lines: what changed, any judgement calls, anything the user must confirm (commercial or ownership claims, facts you could not verify), and a Sources list when research was used.
- When asked for a single slide, deliver only that slide.

---

## 3. Story architecture

The structure comes from the deck's purpose, audience and content, not from a fixed list. Build it this way:
1. Name the decision or belief the audience should leave with.
2. List the three to six messages they must accept to get there, in the order they would ask for them.
3. Give each message a slide (or a short sequence) and pick the opening: context first for a proposal, point of view first for an offering or thought-leadership deck, recommendation first for a decision-ready leadership audience.
4. Add only the slide types the content calls for. A demo slide belongs only when there is a product to show; credentials only when they help the argument; an appendix only when depth would interrupt the story.

The two arcs below are how two past decks were structured. Borrow from them, combine them or ignore them.

### Example: client proposal arc (Disney deck)
1. Cover: "Discussion with <Client>" / "Myridius <Programme name>" / month and year.
2. Background and the bigger picture: current vs target state, how we see the opportunity, how it extends beyond the first project, and "What this presentation covers" (three or four numbered chapters).
3. What it takes: the considerations that matter to the client (icon tiles), plus the three ways to do it.
4. Our POV: the options, each with a mini-illustration of how it works, where certainty comes from, when it is strongest, and what it means for this client. Recommended option in the dark card.
5. Comparison: options as columns, decision dimensions as rows (efficiency and speed, quality and traceability, repeatability and scale, cost of ownership, reusability after go-live).
6. Build approach: how we build it with the client and hand it over (assets we bring with approvals, built together, replicated, owned by the client) next to what the solution is made of.
7. The solution: how it works (people, the line, the learning loop, always-on controls).
8. Applied to the client (eyebrow "... (CLIENT - Illustrative example)"): the governed path on the client's own system, with what it drives for them.
9. Demo: product screenshots, brochure style, with "Demo available".
10. Trust: how quality is assured (guardrails, evals, human gates, audit).
11. Appendix divider, then depth: evals, testing including UAT, execution and hosting options.
12. End slide.

### Example: offering and POV arc (Agent Assurance deck)
Market shift (where it is happening) → why tools alone fail → our credentials (client examples) → section divider "Our point of view" → urgency (sourced statistics) → the mandate (2x2) → old world vs new world (comparison table with mini-diagrams) → failure modes (hub diagram, then cards) → what it requires → our framework (dimensions) → platform partner and what Myridius brings → workflow loops → demos → appendix: maturity curve, engagement models, tool landscape → end.

### Threading rules
- **Point of view first, then drill down.** Lead with the thesis, then prove it slide by slide.
- **Introduced once, reused everywhere.** Themes or dimensions or buckets introduced early (for example Understand, Govern, Prove, Scale) must be the same buckets used later. Never add a bucket on slide 4 that slide 1 did not introduce.
- **No duplication** across slides or within a slide. If two sections say the same thing, merge them.
- **Each slide earns its place.** If a slide re-explains what the previous one said, cut or merge it.
- **Anticipate the reader's practical question.** Example: "How do the accelerators get into the client's AWS? Do we rebuild them or bring them?" Answer it on the slide (installed, not rebuilt).
- **Depth goes to the appendix**, behind a divider.
- **Offer a non-controversial alternative** when a slide scores or judges options (for example scored comparison vs "what the client would need to add").

---

## 4. Headers and titles

Every content slide has three header elements at fixed template positions:
- **Eyebrow**: 1 to 3 words, caps, naming the chapter: OUR POV, COMPARISON, HARNESS BUILD APPROACH, HARNESS-LED, DEMO, TRUST, EVALS, TESTING. For worked examples: "HARNESS-LED (GRATS - Illustrative example)". For a series: "AI Agent failure modes (1/2)".
- **Title**: the message of the slide, written for a CXO. One line (about 65 characters at 28pt bold; the user's titles run 63 to 66). Sentence case. A teal accent on one key phrase is allowed sparingly. Two lines only when the user asks.
- **Subtitle**: one line of context or the supporting claim. When the title is descriptive, the subtitle carries the message (the user's own pattern: title "Three ways Disney could approach GRATS and the apps that follow", subtitle "When AI writes the code, the method decides the outcome").

Titles the user accepted: "Build the harness once and run every migration after GRATS on it"; "AI-generated code earns trust through guardrails, evals and people"; "Every change is proven against legacy GRATS before users sign off"; "Adoption is racing ahead of assurance"; "Agents fail in places traditional testing never had to look".

Titles the user rejected, and why:
- "The AI is the same in every option, the harness around it is not": childish, not CXO messaging.
- "We run modernization as an AI factory, not a one-off project": arrogant.
- Titles that explain the slide ("Overview of approaches") instead of stating its message.

---

## 5. Writing rules

**Never use em dashes.** Not in titles, body, labels, notes or replies. Rewrite with a semicolon, comma, colon or two sentences. The user has removed hundreds by hand. Also no en dash used as a dash, no double hyphens. The linter checks this. If semicolon or colon do not make sense in a sentence, make sure it is grammatically correct and uses business language. 

No AI markers or slop: no hype words (unleash, robust, cutting-edge, game-changer, transformative, elevate, empower, synergy, best-in-class, world-class, next-gen), no "in today's fast-paced", no "it's not just X, it's Y", no "not only... but also", no moreover / furthermore / in conclusion, no filler intensifiers (genuinely, honestly, truly, really, very), no emojis, no exclamation marks, no rhetorical questions as titles.

Style:
- Short phrases, not paragraphs. A tile has a 2 to 4 word heading and one line beneath. Bullets stay under about 15 words and two lines. Groups of three are ideal; four or five at most.
- Low text density. If a slide feels heavy, cut words before shrinking fonts.
- Specific beats generic: "Payouts must match to the cent" beats "ensure accuracy".
- No arrogance or absolutes ("only we", "guaranteed", "unmatched").
- Use client-provided facts verbatim; when given a slide or screenshot to polish, do not reinvent its facts or assumptions, only improve wording and layout.
- Explain jargon the first time, or avoid it (the user asked "what is RA standards?").
- Prefer neutral, descriptive comparisons to judgement labels. Labels such as "Included / Partly" can read as controversial; describe what each option does or what the client must add.
- Harvey balls or scores only when the user wants scoring, and label them as Myridius' assessment.
- Trade-offs: state the real cost of each option, including ours.
- People are "the Myridius team"; Evoq is the accelerator brand. Use product names exactly: Myridius, Evoq, Evoq AEO (Agentic Engineering Orchestrator), Code to Clarity, Context Engine, Intent2Delivery (I2D) engine, Agentic QE.
- The user often uses ";" as a joiner in short lines ("Fast to start; but..."). That is fine.

---

## 6. Visual design system

### Template and canvas
- Always the Myridius 2026 template (from the "Myridius_Disney_GRATS Migration_Oct2026" pack). 16:9, 13.333 x 7.5 in. White content slides.
- The template's content layout draws the Myridius logo (bottom left) and the page number (bottom right), plus the copyright line where the layout has one. Never draw your own logo, footer, brand mark or page number, and keep the bottom 0.75 in clear.
- Cover: beige layout with the large M graphic. Section dividers ("Our point of view", "Appendix"): dark layout with the teal M. End slide: beige "Learn more at myridius.com".

### Colour (only these)
| Token | Hex | Use |
|---|---|---|
| Carbon Moss | 0C2226 | dark panels, primary dark text, recommended card |
| Quantum Leaf | 194247 | titles, body text, secondary dark panels |
| Ocean Slate | 337077 | secondary text and labels; sparingly |
| Myridius Teal | 09A78D | eyebrows, one accent phrase in a title, small accents |
| Infinite Mint | D2F0C6 | light fills, icon tiles, chips; text on dark |
| Pulse Green | 52E081 | small highlights on dark only; sparingly |
| White | FFFFFF | background, text on dark |

Light surfaces use Moss, Leaf or Slate text. Dark surfaces use White or Mint text. Avoid other theme colours (lime, extra greens) unless the user asks. Keep box colours uniform within a group; the user rejected progressive or rainbow fills ("make them transparent like the first box").

### Typography
- Segoe UI only (Semibold allowed). Template sizes: eyebrow 10pt bold caps, teal, tracking 2.1pt; title 28pt bold Leaf; subtitle 12pt Leaf; section labels 10 to 11pt bold caps (teal or slate); card headings 11 to 13pt bold; body 8 to 11pt; never below 7pt.
- Left-aligned text. Titles and subtitles left-aligned at the template positions.

### Components
These are defaults that keep decks consistent, not a limit. The content decides what a slide needs: tables, timelines, maps, charts, screenshots, illustrations, quotes, org charts, or something new. Keep whatever you use inside the palette, typography and polish rules above.
- Cards: white with a thin border (Moss at 16%) or very light fill; radius about 0.1 in. One dark card (Moss) marks the recommendation or the hero element.
- Icon tiles: line icons (stroke, round caps) in mint circles; every list item and tile gets an icon.
- Bands: a dark Leaf or Moss strip for a takeaway ("Beyond go-live: ...", "Always on").
- Chips: small mint pills for named assets (Code to Clarity, Eval suites). Avoid status pills and tags that make a slide busy; put timing or status into the heading instead.
- Numbered steps and chevrons for sequences; connectors with arrowheads, always labelled (an unlabelled dotted line confused the user).
- No unexplained badges or numbers. Everything on the slide must be readable without a presenter.

### Designing the visual
1. Write the slide's message in one sentence.
2. Name the relationship it is about: a sequence, a choice, a comparison, layers, a cycle, a hierarchy, before and after, cause and effect, ownership moving from one party to another, maturity over time, parts of a whole.
3. Sketch two or three visual ideas that show that relationship, and pick the one where the picture alone carries the message. New and unusual forms are welcome when they are clearer.
4. Test it: hide the text; the shape of the diagram should still suggest the point. Then add only the words it needs.

### Reference diagrams from past decks (inspiration, not a menu)
- Options cards with mini-illustrations (people with agents; a platform with managed paths; a harness ring), recommended option dark.
- Columns x rows comparison: options as columns, decision dimensions as row bands with icons on the left; row labels once on the left, never repeated in cells.
- Harness ring: segmented donut (Understand, Govern, Prove, Scale) around an engine core, curved labels, callouts with leader lines and asset chips.
- Concentric layers of control (guardrails, evals, human gates, audit trail) with an exit path to "accepted".
- Governed path: chevron stages with human sign-off gates, an always-on band below, "what it drives" outcomes.
- Factory line: people row, migration line, learning loop, always-on controls.
- Staircase for layered testing ending in UAT and go-live sign-off.
- Hub and spoke for failure modes; 2x2 for mandates; maturity curve with three stages; stacked dimension layers with tool examples.
- Current to target state mapping (from, arrow, to) on a dark background card.
- Brochure screenshots: real product screens, cropped tight, rounded corners and soft shadow, no window dots or browser chrome, captions and numbered callouts outside the screen, never covering it; only screens relevant to the story.

---

## 7. Collaboration rules (learned from interventions)

- When the user has modified a slide, work from their latest file and keep their layout and wording. Change only what was asked. If you cannot access their file, rebuild their version exactly from the screenshot and say so.
- When a change on one slide affects others, tell the user which slides and give the replacement text; do not regenerate those slides unless asked.
- "Take a judgement call" means decide, do it, and explain the decision in one or two lines.
- When unsure of visual direction, offer two or three options of the same slide.
- Keep content changes minimal when the user says "do not make major tweaks".
- Remove anything the user flags as busy, repeated or confusing rather than restyling it.
- Validate the user's own draft content: keep what is right, correct what is not (with a reason and a source), and add what is missing.
- Answer side questions (for example "what is RA standards?") directly before continuing.

---

## 8. Building: the mkit kit

### Assets
Kit folder: `C:\Users\201637\OneDrive - RCG Global Services, Inc\Desktop\Desktop\_WORK\_Claude\myridius-deck-kit` (inside the device shell: `$HOME/mnt/_Claude/myridius-deck-kit`). If the `_Claude` folder is not connected in the session, ask the user to connect it. If the kit cannot be used at all, build directly on the template with python-pptx (use the layout of the template's content sample slide, with header text boxes at the positions in section 8) and still follow every rule here.
- `template/Myridius_Template_2026.pptx`: four sample slides in this order: cover, content sample, divider, end slide. The merge tool uses whatever layout the content sample uses, so the user can change the template in PowerPoint as long as that order stays.
- `tools/mkit.py` (HTML kit: palette, header at template positions, icons, ring and arc helpers), `tools/icons.py`, `tools/html2pptx.py`, `tools/extract.js`, `tools/build.js`, `tools/postproc.py`, `tools/round_pics.py`, `tools/merge_into_template.py`, `tools/lint_text.py`, `tools/render_qa.py`, `tools/fonts.conf`.
- `examples/example_deck.py`: three working slide patterns end to end.
- Reference decks in `_Claude`: "Myridius_Disney_GRATS Migration_Oct2026.pptx" (proposal) and "Agent Assurance_June2026.pptx" (offering). Render and look at them when starting a new deck type.

### Pipeline
Stage the kit into the cloud workspace (it needs Chromium, node and LibreOffice), then:
```
python3 slides.py                                    # your mkit script writes deck.html
python3 tools/html2pptx.py deck.html raw.pptx "Deck title"
python3 tools/merge_into_template.py raw.pptx Client_Topic_v1.pptx \
   --kicker "Discussion with <Client>" --title "Myridius|<Programme>" --date "<Month Year>" --divider "Appendix@9"
python3 tools/lint_text.py Client_Topic_v1.pptx --no-stats
python3 tools/render_qa.py Client_Topic_v1.pptx qa
```
Commit the final PPTX to the user's project folder.

### Kit rules
- Canvas 1920 x 1080 px; 144 px = 1 in; 1 pt = 2 px. Content zone x 59 to 1860, y 190 to 958 (160 when there is no subtitle). Use `header(eyebrow, title, sub, accent=...)`; never move it.
- The kit is a toolbox, not a set of slide templates: any layout built from positioned HTML and SVG within these rules converts to editable shapes, so new diagrams cost nothing extra.
- Everything absolutely positioned (`.slide > *`). Flex is fine inside a positioned element.
- SVG layers: `svg(...)`; paths with M, L, Q, C, Z only (use `arc_c` / `seg_path` for arcs). Put a background SVG layer before the HTML it sits under (`o.insert(1, svg(...))`), and an overlay after.
- Curved text with `curved_label` (exports as rotated letters). No CSS gradients, transforms or filters on exported elements; box shadows are fine.
- Icons: `icon()`, `ico()` (tile), `gicon()` (inside SVG). They export as native SVG pictures with PNG fallback.
- Screenshots: `<img>` with border-radius; exported as pictures with rounded corners.
- Preview furniture (`.tpl`) shows where the logo and footer will sit and is not exported.
- Inter stands in for Segoe UI when rendering in the cloud; it is wider, so if a line fits in the render it fits in PowerPoint.
- Small edits to an existing PPTX (text, a word in a title) are better done directly with python-pptx on the user's file than by rebuilding.

---

## 9. QA checklist (all must pass before delivery)

Story
- [ ] Each slide's title states its message; read only the titles and the story still holds.
- [ ] Buckets and terms are introduced before they are used and stay consistent; nothing is duplicated.
- [ ] Every fact is from the user's documents or a cited, current source; nothing invented.
- [ ] Trade-offs are shown honestly, including for our recommendation.

Writing
- [ ] `lint_text.py` reports 0 errors (no em dashes, emojis, exclamation marks); warnings reviewed.
- [ ] No percentages in client proposals unless the user asked; any statistic has a source line.
- [ ] No arrogant, absolute or hype phrasing; product names spelled exactly.

Design
- [ ] Titles on one line in the render; eyebrow, title and subtitle at template positions.
- [ ] Only palette colours; Segoe UI only; uniform box colours within a group; one dark emphasis.
- [ ] Icons on list items and tiles; each visual was designed from its message (not picked from a list); connectors labelled.
- [ ] No overflow, collisions or text touching edges; bottom 0.75 in clear for logo and footer.
- [ ] Opened render of every slide looked at, not just the contact sheet.
- [ ] Output is editable PPTX in the Myridius template, versioned, saved to the user's folder.
