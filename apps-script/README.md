# Lead capture — Google Apps Script

Backend for the scorecard's "download my report" gate. Stores every lead in a
Google Sheet and (optionally) emails a notification. No server, no cost.

## One-time setup

1. Create a Google Sheet (any Google account). Name it e.g. `Go Services — Leads`.
2. In the Sheet: **Extensions → Apps Script**.
3. Delete the boilerplate and paste the contents of [`Code.gs`](./Code.gs).
4. Edit two constants at the top:
   - `SHARED_TOKEN` — set to a random string. **Must match** `GAS_TOKEN` in
     `assets/js/calculators.js`.
   - `NOTIFY_EMAIL` — keep `hello@go-cleaning.com` for an email per lead, or set
     to `""` to disable emails.
5. **Deploy → New deployment → Type: Web app.**
   - Description: `lead capture`
   - Execute as: **Me**
   - Who has access: **Anyone**
   - Click **Deploy**, authorize when prompted.
6. Copy the **Web app URL** (ends in `/exec`).

## Wire it to the site

In `assets/js/calculators.js`, set:

```js
var GAS_ENDPOINT = "https://script.google.com/macros/s/XXXXXXXX/exec";
var GAS_TOKEN    = "the-same-string-you-put-in-SHARED_TOKEN";
```

That's it. The header CSP (`connect-src`) already allows `script.google.com`
and `script.googleusercontent.com`.

## Test

- Open the `/exec` URL in a browser → should return `{"ok":true,...}` (doGet).
- Fill the scorecard on the live site, complete the form → a row appears in the Sheet.

## Notes

- The browser sends the lead with `fetch(..., { mode: "no-cors" })`, so it can't
  read the response. The report still downloads even if the network call fails —
  lead capture never blocks the deliverable.
- Redeploying new `Code.gs` code: **Deploy → Manage deployments → edit (pencil) →
  Version: New version → Deploy.** The `/exec` URL stays the same.
- `SHARED_TOKEN` only stops casual bots. It's visible in client JS; it is not a
  real secret. For low-volume B2B leads that's fine.
