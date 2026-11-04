#!/usr/bin/env bash
# Deploy the static site to Cloudflare Pages (project: gocleanv1).
#
# `wrangler pages deploy` uploads EVERYTHING in the directory except a fixed
# ignore list (node_modules, .git, .DS_Store, functions, _worker.js, .wrangler).
# It does NOT read .assetsignore. So to keep server-side / tooling files out of
# production we stage a clean copy and deploy that instead of the repo root.
#
# Usage:
#   ./deploy.sh review   # client preview  -> https://review.gocleanv1.pages.dev
#   ./deploy.sh main     # PRODUCTION      -> https://www.go-cleaning.com
# Default branch is "review" (safe).
set -euo pipefail

BRANCH="${1:-review}"
SRC="$(cd "$(dirname "$0")" && pwd)"
STAGE="$(mktemp -d)/gocleanv1"
mkdir -p "$STAGE"

# Copy the deployable site only. _headers and _redirects ARE included on purpose.
rsync -a --delete \
  --exclude '.git' \
  --exclude '.claude' \
  --exclude 'apps-script' \
  --exclude 'README.md' \
  --exclude 'HANDOFF.md' \
  --exclude 'docs' \
  --exclude 'deploy.sh' \
  --exclude '.DS_Store' \
  "$SRC"/ "$STAGE"/

# `npx wrangler` resolves to the nearest node_modules up the directory tree, which
# may be an unrelated or broken install (in Nov 2026 the workerd binaries in both
# ~/node_modules and DATRUM projects/node_modules were wiped, breaking every npx
# invocation). Prefer a wrangler already on PATH; fall back to npx only if there is none.
if command -v wrangler >/dev/null 2>&1; then
  WRANGLER=(wrangler)
else
  WRANGLER=(npx wrangler)
fi

echo "Deploying staged copy to branch: $BRANCH"
"${WRANGLER[@]}" pages deploy "$STAGE" \
  --project-name=gocleanv1 \
  --branch="$BRANCH" \
  --commit-dirty=true

rm -rf "$(dirname "$STAGE")"
