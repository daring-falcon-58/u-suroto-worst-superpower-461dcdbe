# SUBMIT-READY — PARTIAL (execution-risk flag stopped the pipeline mid-way)

Competition: u-suroto-worst-superpower-461dcdbe ("Worst Superpower", $2 winner-take-all)
Deadline: 2026-11-27 00:30 WIB | R1 cutoff: 2026-11-26 08:30 WIB
Status: BUILD COMPLETE, NOT YET PUSHED / NOT YET KIT-CHECKED / NOT SUBMITTED.

## Winning line (tournament winner C16, 7–0, 97 chars, 1 line)
> I can make any door open for me, but only doors that are already open, and only if I knock first.

Char count: 97 (verified by script). Gate 1–140: PASS (verified by local run of main.py).
Selection evidence: candidates.md — 36 candidates scored vs the 5 published judge
criteria, top 8 in a full round-robin pairwise tournament (28 pairs, both orders),
winner 7–0. Collision-checked against all 50 live titles: clear (no doors/knocking).

## Repo
- URL: https://github.com/daring-falcon-58/u-suroto-worst-superpower-461dcdbe
- State: CREATED (public) with description + homepage set at creation.
  Description: "Invent the most useless superpower in one line of 140 characters. A judge model ranks the field; the single winner takes the $2 pool. Free to enter. Built by an AI agent for make.fun's “Worst Superpower” bounty, $2 in USDC."
  Homepage: https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe
- Topics: NOT YET SET — still to do via gh api PUT ["ai-agents","bounties","growth","makefun"]
  (gh auth works: hosts.yml stored, account daring-falcon-58).
- Commit SHA: NONE YET — nothing pushed; the GitHub repo is still empty.

## Workdir (~/workspace/makefun/u-suroto-worst-superpower-461dcdbe/)
- main.py — written + genuinely revised (gate self-check added after first write);
  tested locally: writes the exact 97-char line to /output/entry.txt.
- README.md — methodology at TOP + all 3 live make.fun badges (competition, rank, reward).
- LICENSE — kit init's version (SPDX-License-Identifier: MIT, copyright to payout wallet).
  My draft MIT LICENSE is at /tmp/LICENSE-worst-superpower (superseded, do not restore).
- owner.json — payout wallet 6aZ9Va3wP6aqy1AUHLAhfSJksFRnKYRD3CtnzwDwdxbw.
- candidates.md — 36 candidates + scores + tournament + collision check.
- .gitignore — excludes kit/ and kit.zip (do NOT commit the 8 MB kit).
- .makefun/freshness.json — kit init anchor: round 34277465, wallet 6aZ9Va3wP6aqy1AUHLAhfSJksFRnKYRD3CtnzwDwdxbw.
- kit/ + kit.zip — downloaded kit (do NOT commit).

## What stopped the run
The `makefun init` step's tool result failed an execution-risk check (system
notice on that exec call). Per the task brief and the standing rule, only Jon's
plain-words go-ahead lifts that class of flag — so I stopped the git/push
pipeline rather than self-approving. Nothing was pushed; no commit exists.

## PENDING — for the parent (needs Jon's go-ahead or a fresh context)
1. Commit + push the workdir files (main.py, README.md, LICENSE, owner.json,
   candidates.md, .gitignore, .makefun/freshness.json) — EXCLUDE kit/ and kit.zip.
   Record the FULL 40-char commit SHA here.
2. Set repo topics via gh api PUT: ["ai-agents","bounties","growth","makefun"]
   (+ verify About description/homepage via gh api).
3. Run the kit check (`node kit/.../cli/makefun.mjs check --repo <dir> --commit <sha>`).
   Expect all pass except transcripts_present (fails pre-bundle — expected).
4. Parent bundles + submits after this run ends (usage rows land only then).
   R1 cutoff 08:30 WIB — plenty of time left as of 02:45 WIB, but do not let it slip.
